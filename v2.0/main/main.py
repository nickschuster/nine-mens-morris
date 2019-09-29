import pygame
from game import Game

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750

# Sets up the window
def setup():
	pygame.init()
	pygame.display.set_caption('Nine Men\'s Morris')
	display = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
	return display

# Starts a new game of nine mens morris
def newGame(display):
	game = Game(display)
	game.start()

if __name__ == __main__:
	display = setup()
	newGame(display)
	