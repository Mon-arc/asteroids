import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
  def __init__(self, x, y, radius):
    # we will be using this later
    if hasattr(self, "containers"):
      super().__init__(self.containers)
    else:
      super().__init__()

    self.position = pygame.Vector2(x, y)
    self.velocity = pygame.Vector2(0,0)
    self.radius = radius
  
  def draw(self, screen):
    # subclasses must override
    pass
  def update(self, dt):
    # subclasses must override
    pass

  def collision(self, circle):
      distance = self.position.distance_to(circle.position)
      radius_sum = self.radius + circle.radius

      return not (distance > radius_sum)