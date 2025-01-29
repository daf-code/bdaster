import pygame
import math
from pygame.locals import *  # This is important for key constants
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):

    def __init__(self, x, y, radius):
        # Call parent constructor, ensuring it doesn’t interfere with image or rect
        super().__init__(x, y, radius)

        # Create a transparent surface for the asteroid's circle
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius, 2)

        # Define the rect property based on the position and radius
        self.rect = self.image.get_rect(center=(x, y))

        # Initialize shot-related properties
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)  # Default stationary velocity

    def draw(self, surface):
        # This draws directly to the screen surface (alternative to using `image`)
        pygame.draw.circle(surface, "darkslategray1", self.position, self.radius, width=2)

    def update(self, dt):
        # Update position with velocity and delta time
        self.position += (self.velocity * dt)
        self.rect.center = self.position  # Sync rectangle to position