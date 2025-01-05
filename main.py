# this allows us to code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  while 1:
    
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

if __name__ == "__main__":
  main()