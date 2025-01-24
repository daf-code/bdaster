# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from pygame.locals import *
from constants import *

def setup_screen():
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def test_loop():
	for event in pygame.event.get():
   		if event.type == pygame.QUIT:
        		return


def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	setup_screen()
	test_loop()
	
	
if __name__ == "__main__":
      main()
