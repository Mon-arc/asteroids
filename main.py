# this allows us to code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *




def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  


  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  dt = 0
  clock = pygame.time.Clock()
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots_collection = pygame.sprite.Group()
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  asteroid_field = AsteroidField()
  Shot.containers = (updatable, drawable)
  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  

  while 1:
    
    screen.fill("black")
    for thing in updatable:
      thing.update(dt)
    
    for thing in asteroids:
      if player.collision(thing):
        print("Game over!")
        return 

    for thing in drawable:
      thing.draw(screen)
    
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    dt = clock.tick() / 1000
    clock.tick()

if __name__ == "__main__":
  main()