import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):

  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)
  
  def update(self, dt):
    # self.position += self.velocity * (25 / self.radius) * dt
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if  self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      angle = random.uniform(20, 50)
      vel1 = self.velocity.rotate(angle)
      vel2 = self.velocity.rotate(angle * -1)
      new_radii = self.radius - ASTEROID_MIN_RADIUS
      asteroid1 = Asteroid(self.position.x, self.position.y, new_radii)
      asteroid2 = Asteroid(self.position.x, self.position.y, new_radii)
      asteroid1.velocity = vel1 * 1.2
      asteroid2.velocity = vel2 * 1.2
      