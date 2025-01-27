import pygame
import math
from pygame.locals import *  # This is important for key constants
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
	
	def __init__(self,x, y, radius):
		
		
		self.radius = radius
		self.position = x, y
		self.velocity = 1


	def draw(self):
		pygame.draw.circle(screen, "darkslategray1", self.position, self.radius, width=2)
		
	def update(self,dt):
		self.position += (self.velocity * dt)
		
		