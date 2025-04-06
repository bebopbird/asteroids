# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()



    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    

        updatable.update(dt)

        screen.fill("black")

        for asteroid in asteroids:
            if asteroid.collide_with(player):
                print("Game over!")
                sys.exit()

        for obj in drawable:
            obj.draw(screen)
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide_with(shot):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()

        # limit to 60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()