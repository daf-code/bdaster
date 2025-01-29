#hack to avoid ALSA issue on WSL
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame
from pygame.locals import *
from circleshape import *
from player import *
#from thrust import *
from asteroidfield import *
from constants import *
import sys
from shot import *

def setup_screen():
	return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

#pygame init
	pygame.init()

#startup routine
	
	screen = setup_screen()
	game_clock = pygame.time.Clock()
	dt = 0
	
#define containers

	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

#add classes to containers in order of program flow	
	Player.containers = (updatables, drawables)
#	Thrust.containers = (updatables, drawables)
	Asteroid.containers = (asteroids, drawables, updatables)
	AsteroidField.containers = (updatables,)
	Shot.containers = (shots, updatables, drawables)

	
	print("Player.containers set:")
	print(Player.containers)
#	print("Thrust.containers set:")
#	print(Thrust.containers)
	print("Drawable group is:")
	print(drawables)
	print("Updatable group is:")
	print(updatables)
	
#create asteroid field outside loop

	asteroid_field = AsteroidField()

#create player and thrust outside loop
	player_1 = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
#	player_1.thrust = Thrust(player_1)
	#print(player_1.mro())	
	#print(player_1.thrust.mro())

#enter primary game loop

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			###keyboard debugging###
			#elif event.type == pygame.KEYDOWN: 
			#	print(f"Key pressed: {event.key}") 
			#	if event.key == pygame.K_a:
			#		print("A key pressed")
			#	if event.key == pygame.K_d:
			#		print("D key pressed")
		#accept input
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a] or keys[1073741904]:
			player_1.rotate_lt(dt)	# rotate left
		
		if keys[pygame.K_d] or keys[1073741903]:
			player_1.rotate_rt(dt)	# rotate rt
			
		if keys[pygame.K_w] or keys[1073741906]:
			player_1.move_fwd(dt)	# fwd
			
		elif keys[pygame.K_s] or keys[1073741905]:
			player_1.move_back(dt)	# back
		
		if keys[pygame.K_SPACE]:
			player_1.shoot(player_1.position.x, player_1.position.y)

		else:
			player_1.no_move()	# no input				
		
		#perform updates
		#for updatable in updatables:
		updatables.update(dt)
		#check collision
		for object in asteroids:
			for shot in shots:
				if object.col_check(shot):
					print("===============ASTEROID DESTROYED===============")
					object.split()
					shot.kill()

		for object in asteroids:
			if object.col_check(player_1):
				print("===============COLLISION===============")
				#print("===============GAME OVER===============")
				#sys.exit()
						
		#blank screen
		screen.fill("black")		 
		#draw objects
		#for drawable in drawables:
		drawables.draw(screen)
		#update the display and delta time
		pygame.display.flip()
		dt = game_clock.tick(60) / 1000.0 # FPS limit

if __name__ == "__main__":
      main()