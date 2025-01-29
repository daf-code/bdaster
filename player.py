import pygame
import math
from pygame.locals import *  # This is important for key constants
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		
		#self image			
		self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)  # Transparent surface
		#tri_pts = [(25, 25 - 25), (0, 25 + 25), (50, 25 + 25)]
		tri_pts = [(25, 0), (0, 50), (50, 50)]
		mini_tri_pts = [(25, 0), (15, 12.5), (35, 12.5)]
		self.rotation = 0
		pygame.draw.polygon(self.original_image, (255, 255, 255), tri_pts)
		pygame.draw.polygon(self.original_image, (255, 0, 255), mini_tri_pts)
		self.image = self.original_image
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		# Draw line relative to the surface's center (25, 25)
		rotation_line_len = 400
		surface_center = (25, 25)  # Center of the 50x50 surface
		rotation_line_end = (25, 25 - rotation_line_len)  # Go up from center
		pygame.draw.line(self.original_image, (0, 255, 255), surface_center, rotation_line_end, 3)
		self.is_thrusting = False
		self.velocity = pygame.Vector2(0, 0)  # Start with no velocity
		self.thrust_max_size = self.radius * THRUST_RADIUS_MULTIPLIER # calculate max and min thrust size once
		self.thrust_min_size = self.thrust_max_size * 0.2
		self.height = self.image.get_height()
		self.shot_timer = 0
		
		
	def get_forward_vector(self):
		# Convert to counterclockwise rotation for Pygame's Vector2.rotate()
		return pygame.Vector2(0, -1).rotate(-self.rotation)
			
	
	def rotate(self, dt):
		# Remove the normalization that was causing issues
		self.rotation += (PLAYER_TURN_SPEED * dt)
		self.rotation %= 360  # Keep rotation between 0 and 360 degrees
		

	def handle_boundaries(self):
		if WRAP_AROUND:
			if self.position.x > SCREEN_WIDTH:
			# If ship goes off right side, appear on left side
				self.position.x = 0
			if self.position.x < 0:
			#If ship goes off left, then appearon right
				self.position.x = SCREEN_WIDTH	
			if self.position.y > SCREEN_HEIGHT:
				self.position.y = 0
			if self.position.y < 0:
				self.position.y = SCREEN_HEIGHT
        		# Same for top and bottom
			
		else:
			# Keep ship position within screen bounds
			if self.position.x > SCREEN_WIDTH:
			# If ship hits right side, stay theree
				self.position.x = SCREEN_WIDTH
			elif self.position.x < 0:
			#If ship goes off left, stay there
				self.position.x = 0	
			if self.position.y > SCREEN_HEIGHT:
				self.position.y = SCREEN_HEIGHT
			elif self.position.y < 0:
				self.position.y = 0
        		# Same for top and bottom
		
	def move(self, dt):
		
		#get the movement vector
		forward = self.get_forward_vector()
		print(f"Forward vector: {forward}")
		print(f"Before velocity: {self.velocity}")
		
		#acceleration/deceleration
		self.velocity += forward * PLAYER_ACCELERATION * dt
		print(f"After velocity: {self.velocity}")
	
	
	def shoot(self, position_x, position_y,):
		if self.shot_timer == 0:
			shot = Shot(position_x, position_y, SHOT_RADIUS)
			#displaced vector tracking orbiter
			#shot.velocity = pygame.Vector2(0, -1).rotate(self.player.rotation) * PLAYER_SHOT_SPEED
			shot.velocity = self.get_forward_vector() * PLAYER_SHOT_SPEED
			self.shot_timer = SHOT_COOLDOWN
			return shot
		else:
			return None
		
	def get_thrust_size(self):
	# Get current velocity magnitude (speed)
		speed = self.velocity.length()
		# Map it to a reasonable visual size (you can adjust these values)
		return min(self.thrust_max_size, max(self.thrust_min_size, speed / 50))
	
	
	def get_thrust_anchor(self):
		anchor_offset = self.height/2
		p_center_x, p_center_y = self.rect.center
		#radian rotation if needed here
		rad_rot = math.radians(self.rotation)
		#offset_x = #should not be needed
		offset_y = math.cos(rad_rot) * -anchor_offset  
		return p_center_x, p_center_y + offset_y
	
	
	
	def rotate_lt(self, dt):
		self.rotate(dt)# rotate left
	
	def rotate_rt(self, dt):
		self.rotate(-1*dt)# rotate rt
			
	def move_fwd(self, dt):
		self.is_thrusting = True
		self.move(dt)
			
	def move_back(self, dt):
		self.is_thrusting = True
		self.move(-dt)
		
	def no_move(self):
		self.is_thrusting = False
	
	
	
	def update(self, dt):
		print("Update Player is running!")  # debug update	
		#print(f"DT: {dt}")
		#print(f"Current velocity: {self.velocity}")
		#check for shot timer
		if self.shot_timer > 0:
			self.shot_timer = max(0, self.shot_timer - dt)
		print(f"Shot timer: {self.shot_timer}")
		#apply velocity to position
		self.position += self.velocity * dt
		self.rect.center = self.position
		
		#apply rotation to orientation
		old_center = self.rect.center  # Save the current rect's center
		self.image = pygame.transform.rotate(self.original_image, self.rotation)
		self.rect = self.image.get_rect(center=old_center)  # Re-center the rect
		
		#apply friction to velocity
		self.velocity *= PLAYER_FRICTION
		#handle boundaries per setting
		self.handle_boundaries()	
		

########################
### OLD CODE BELOW ####	
#old circle thrust graphic code
		#if self.velocity.length() > 0.1: #draw thrust if we have velocity
			#thrust_size = self.get_thrust_size() # call the thrust size function
			#circle_thrust_pos = self.position + self.get_forward_vector() * -20 # position the thrust graphic
			#pygame.draw.circle(screen, (255, 100, 0), circle_thrust_pos, thrust_size) # draw the thrust graphic
	