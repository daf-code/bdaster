#hack to avoid ALSA issue on WSL
import os 
os.environ['SDL_AUDIODRIVER'] = 'dsp'

import pygame
from pygame.locals import *
from constants import *

def setup_screen():
	return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def test_loop():
	screen = setup_screen()
	while 1 == 1:
		for event in pygame.event.get():
   			if event.type == pygame.QUIT:
        			return
		screen.fill("black")
		pygame.display.flip()
		



def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	test_loop()
	
	
if __name__ == "__main__":
      main()
