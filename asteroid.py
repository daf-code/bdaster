import pygame
import math
from pygame.locals import *  # This is important for key constants
from constants import *
from circleshape import CircleShape
import random 


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        # Call parent constructor, ensuring it doesn’t interfere with image or rect
        super().__init__(x, y, radius)

        # Create a transparent surface for the asteroid's circle
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius, 2)

        # Define the rect property based on the position and radius
        self.rect = self.image.get_rect(center=(x, y))

        # Initialize asteroid-related properties
        self.radius = radius
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)  # Default stationary velocity
    


    def draw(self, surface):
        # This draws directly to the screen surface (alternative to using `image`)
        pygame.draw.circle(surface, "darkslategray1", self.position, self.radius, width=2)


    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position  # Sync rectangle to position



    def split(self):
        old_pos = self.position
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        #split into two smaller asteroids
        r_angle_adj = random.uniform(-20, 50)
        vec_rot_1 = self.velocity.rotate(r_angle_adj)
        vec_rot_2 = self.velocity.rotate(-r_angle_adj)
        asteroid_1 = Asteroid(old_pos.x, old_pos.y, new_radius)
        asteroid_2 = Asteroid(old_pos.x, old_pos.y, new_radius) 
        #asteroid_1.rotation = pygame.Vector2(0, -1).rotate(vec_rot_1)
        #asteroid_2.rotation = pygame.Vector2(0, -1).rotate(vec_rot_2)
        asteroid_1.velocity = vec_rot_1 * 1.2
        asteroid_2.velocity = vec_rot_2 * 1.2       