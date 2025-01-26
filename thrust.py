import pygame
import math
from player import Player

class Thrust(pygame.sprite.Sprite):

	def __init__(self, player):
	
		if hasattr(self, "containers"):
        
			super().__init__(self.containers)
        
		else:
            		super().__init__()
		
		self.player = player
		
		thrust_size = player.radius * 1.5
		self.original_image = pygame.Surface((thrust_size, thrust_size), pygame.SRCALPHA)
		self.rect = self.original_image.get_rect(center=self.player.rect.center)
		self.blank_image = pygame.Surface((0, 0), pygame.SRCALPHA)
		pygame.draw.polygon(
			self.original_image,
			(255, 100, 50),
			[
				(thrust_size // 2, thrust_size), #bottom point
				(thrust_size // 4, 0), #top left
				(thrust_size * 3 // 4, 0), #top right
			],
		)
	
	def update(self, dt):
    		# Check if the player is actively thrusting (public attribute of Player)
		if self.player.is_thrusting:
        		# Make the Thrust sprite visible
			self.image = self.original_image
			
         		# Align rotation: Match the Player's rotation
			self.image = pygame.transform.rotate(self.original_image, -self.player.rotation)
			self.rect = self.image.get_rect(center=self.rect.center)       
			
			radius = self.player.radius
			base_x = 0  # Horizontally centered
			player_height = self.player.image.get_height()  # Height of the bounding rect
			offset_to_apex = player_height / 2  # Distance to the apex of the triangle
			base_y = radius + offset_to_apex * .8
			#base_global_x = self.player.rect.centerx + base_x * math.cos(math.radians(-self.player.rotation)) - base_y * math.sin(math.radians(-self.player.rotation))
			#base_global_y = self.player.rect.centery + base_x * math.sin(math.radians(-self.player.rotation)) + base_y * math.cos(math.radians(-self.player.rotation))
			global_x = ( 
    				self.player.rect.centerx
				+ base_x * math.cos(math.radians(self.player.rotation))  # Rotate horizontally
    				- base_y * math.sin(math.radians(self.player.rotation))  # Rotate vertically
			)

			global_y = (
				 self.player.rect.centery
				+ base_x * math.sin(math.radians(self.player.rotation))  # Rotate horizontally
				+ base_y * math.cos(math.radians(self.player.rotation))  # Rotate vertically
			)
			
        		#Find  position: Place it slightly behind the Player's center
			#forward_x = math.cos(math.radians(self.player.rotation))
			#forward_y = -math.sin(math.radians(self.player.rotation))  # Adjust for Pygame's y-axis
			#offset_x = 0 
			#nope: offset_x =  -1.5 * self.player.radius * forward_x
			#offset_y = -1.85 * self.player.radius * forward_y
			
			
			
			#bad code - causes object to rotate around player - keep for powerups
			#offset_x = -1.5 * self.player.radius * math.cos(math.radians(self.player.rotation))
			#offset_y = -1.5 * self.player.radius * math.sin(math.radians(self.player.rotation))
			
			
			
			#update placement
			self.rect.center = (global_x, global_y)
        		
			
			print(f"Player radius: {self.player.radius} Player Rotation: {self.player.rotation}")
			#print(f"Thrust rotation applied is {-self.player.rotation}, thrust offset is {offset_x}, {offset_y}")
			

		else:
			# Hide the Thrust sprite (make it invisible or skip drawing)
			self.image = self.original_image #for testing
			radius = self.player.radius
			base_x = 0  # Horizontally centered
			player_height = self.player.image.get_height()  # Height of the bounding rect
			offset_to_apex = player_height / 2  # Distance to the apex of the triangle
			base_y = radius + offset_to_apex * .8
			base_global_x = self.player.rect.centerx + base_x * math.cos(math.radians(-self.player.rotation)) - base_y * math.sin(math.radians(-self.player.rotation))
			base_global_y = self.player.rect.centery + base_x * math.sin(math.radians(-self.player.rotation)) + base_y * math.cos(math.radians(-self.player.rotation))
			self.rect.center = (base_global_x, base_global_y) #for testing
			#self.image = self.blank_image