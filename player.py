import pygame
from pygame.locals import *  # This is important for key constants
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		
		#self image			
		self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)  # Transparent surface
		pygame.draw.polygon(self.original_image, (255, 255, 255), [(25, 0), (0, 50), (50, 50)])
		self.image = self.original_image
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

		self.is_thrusting = False
		self.rotation = 0
		self.velocity = pygame.Vector2(0, 0)  # Start with no velocity
		
		self.thrust_max_size = self.radius * THRUST_RADIUS_MULTIPLIER # calculate max and min thrust size once
		self.thrust_min_size = self.thrust_max_size * 0.2
	
		
		#if self.velocity.length() > 0.1: #draw thrust if we have velocity
		#	thrust_size = self.get_thrust_size() # call the thrust size function
		#	thrust_pos = self.position + self.get_forward_vector() * -20 # position the thrust graphic
		#	pygame.draw.circle(screen, (255, 100, 0), thrust_pos, thrust_size) # draw the thrust graphic
		
	def get_forward_vector(self):
		return pygame.Vector2(0, -1).rotate(self.rotation)
		
		
	#def triangle(self):
		#forward = self.get_forward_vector()
		#right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		#a = self.position + forward * self.radius
		#b = self.position - forward * self.radius - right
		#c = self.position - forward * self.radius + right
		#return [a, b, c]
	
	#using mathematical normalization instead of shifting floor mod
	#def floor_mod(value, mod): 
		#return  value - (value // mod) * mod
	
	def rotate(self, dt):
		print(f"rotation before: {self.rotation}")
		self.rotation += (PLAYER_TURN_SPEED * dt)
		self.rotation = (self.rotation + 180) % 360 - 180
		print(f"rotation after: {self.rotation} with normalization")
		
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
		
	
		
	def get_thrust_size(self):
	# Get current velocity magnitude (speed)
		speed = self.velocity.length()
		# Map it to a reasonable visual size (you can adjust these values)
		return min(self.thrust_max_size, max(self.thrust_min_size, speed / 50))
	
	def update(self, dt):
		#print("Update is running!")  # debug update
		keys = pygame.key.get_pressed()
		
		# Debug all key states
		if keys[pygame.K_a] or keys[1073741903]:
			print("A key is pressed")
		if keys[pygame.K_d] or keys[1073741904]:
			print("D key is pressed")

		if keys[pygame.K_a] or keys[1073741904]:
			self.rotate(dt)# rotate left
		if keys[pygame.K_d] or keys[1073741903]:
            		self.rotate(-1*dt)# rotate rt
			
		if keys[pygame.K_w] or keys[1073741906]:
			self.is_thrusting = True
			self.move(dt)
			
		elif keys[pygame.K_s] or keys[1073741905]:
			self.is_thrusting = True
			self.move(-dt)
		else:
			self.is_thrusting = False
			
		#print(f"DT: {dt}")
		#print(f"Current velocity: {self.velocity}")
		
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