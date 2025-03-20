import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():

    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
    # delta time
        dt = clock.tick(60) / 1000
        keys = pygame.key.get_pressed()
    # player input
        updatable.update(dt, keys, shots)  
        
        for shot in shots:
            shot.update(dt)
        for asteroid in asteroids:
            asteroid.position += asteroid.velocity * dt
        player.update(dt, keys, shots)
        
    # draw world
        screen.fill((0, 0, 0))

        for shot in shots:
            shot.draw(screen)      

        for entity in drawable:
            entity.draw(screen)

                
        new_asteroids = []
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    new_asteroids.extend(asteroid.split())  # Collect new asteroids
                    shot.kill()
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()        
                     
        pygame.display.flip()
               
        

if __name__ == "__main__":
    main()