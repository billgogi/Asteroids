import pygame
from circleshape import CircleShape
from constants import *
import random

# In asteroid.py
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent constructor with all required parameters
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        # Use position from the parent class
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
        
    def update(self, dt, *args, **kwargs):
        # Move the asteroid by velocity * dt
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return []
    
    # Store position and velocity before killing
        current_pos = pygame.math.Vector2(self.position)
        current_velocity = pygame.math.Vector2(self.velocity) if hasattr(self, 'velocity') else None
        new_radius = self.radius - ASTEROID_MIN_RADIUS
    
        self.kill()
    
        rand_angle = random.uniform(20, 50)  # Range as specified in instructions
    
    # If velocity doesn't exist or is zero, create a random velocity
        if current_velocity is None or current_velocity.length() <= 0.001:
            current_velocity = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
            current_velocity.scale_to_length(50)  # Default speed
    
    # Create two new velocity vectors as per instructions
        new_velocity1 = current_velocity.rotate(rand_angle) * 1.2
        new_velocity2 = current_velocity.rotate(-rand_angle) * 1.2
    
    # Create new asteroids at the same position but with new velocity/radius
        asteroid1 = Asteroid(current_pos.x, current_pos.y, new_radius)
        asteroid2 = Asteroid(current_pos.x, current_pos.y, new_radius)
    
    # Set velocities for the new asteroids
        asteroid1.velocity = new_velocity1
        asteroid2.velocity = new_velocity2
    
    # Add them to the group
        Asteroid.add(asteroid1)
        Asteroid.add(asteroid2)
    
        return [asteroid1, asteroid2]
        
            