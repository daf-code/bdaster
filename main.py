#hack to avoid ALSA issue on WSL
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame
from pygame.locals import *
from circleshape import *
from player import *
from constants import *

def setup_screen():
	return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def test_loop():
    game_clock = pygame.time.Clock()
    dt = 0
    screen = setup_screen()
    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = game_clock.tick(60)

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

#pygame init
	pygame.init()

#run test loop
	#test_loop()

#startup routine
	
	screen = setup_screen()
	game_clock = pygame.time.Clock()
	dt = 0
	
#define containers

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	
#create player outside loop
	player_1 = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
	
	 
#enter primary game loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			#elif event.type == pygame.KEYDOWN:
			#	print(f"Key pressed: {event.key}") #key debug
			#	if event.key == pygame.K_a:
			#		print("A key pressed")
			#	if event.key == pygame.K_d:
			#		print("D key pressed")

		#blank screen
		screen.fill("black")
	
		#draw objects
		for i in updatable:
			i.update(dt)
		
		for i in drawable:
			i.draw(screen)

	
	
	
		#update the display and delta time
		pygame.display.flip()
		dt = game_clock.tick(60) / 1000.0 # convert ms to s
	
if __name__ == "__main__":
      main()