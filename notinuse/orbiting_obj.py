import pygame
import math
from player import Player

class Thrust(pygame.sprite.Sprite):

	def __init__(self, player):
		if hasattr(self, "containers"):#gygame containerization
			super().__init__(self.containers)
		else:
            		super().__init__()
			
		#initial setup
		self.player = player
		self.p_radius = self.player.radius
		self.p_height = self.player.height  # Height of the player bounding rect		
		self.thrust_size = self.p_radius * 1.5
		
		#sprite image/surface
		self.original_image = pygame.Surface((self.thrust_size, self.thrust_size), pygame.SRCALPHA)
		self.image = self.original_image
		self.next_image = self.original_image
		self.blank_image = pygame.Surface((0, 0), pygame.SRCALPHA)
		self.rect = self.original_image.get_rect(center=self.player.rect.center)
		#sprite will be a triangle
		pygame.draw.polygon(
			self.original_image,
			(255, 100, 50),
			[
				(self.thrust_size // 2, self.thrust_size), #bottom point
				(self.thrust_size // 4, 0), #top left
				(self.thrust_size * 3 // 4, 0), #top right
			],
		)
		#sprite positioning values
		self.offset_to_apex = self.p_height / 2  # Distance to the apex of the triangle
		self.y_offset = self.p_radius + self.offset_to_apex * 0.9 # tweak thrust Y offset here
	
	###############################	
	#[THRUST GRAPHIC  FUNCTIONS]] #
	###############################		
	
	def update(self, dt): #called in pygame update loop
    		# Check if the player is actively thrusting (public attribute of Player)
		# Align rotation: Upate to match the Player's rotation before drawn
		self.next_image = pygame.transform.rotate(self.original_image, self.player.rotation)
		rad_rot = math.radians(self.player.rotation)
		thrust_anchor_x, thrust_anchor_y = self.player.get_thrust_anchor()
		thrust_gspace_x = thrust_anchor_x + math.sin(rad_rot) * self.y_offset
		thrust_gspace_y = thrust_anchor_y - math.cos(rad_rot) * self.y_offset
		self.rect = self.image.get_rect(center=self.rect.center)
		#self.rect = self.image.get_rect(center = thrust_gspasce_x, thrust_gspace_y)		
		self.rect.center = (thrust_gspace_x, thrust_gspace_y)
        		
			
		print(f"Player radius: {self.player.radius} Player Rotation: {self.player.rotation}")
		#print(f"Thrust rotation applied is {-self.player.rotation}, thrust offset is {offset_x}, {offset_y}")
		
		if self.player.is_thrusting: #then make the Thrust sprite image appear when drawn
			self.image = self.next_image
		else: #hide it if not thrusting
			self.image = self.next_image #for testing
			#self.image = self.blank_image