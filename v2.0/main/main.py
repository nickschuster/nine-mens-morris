import pygame
from game import Game

WINDOW_WIDTH = 1050
WINDOW_HEIGHT = 750

# For default look
BOARD_IMG = pygame.image.load("../assets/ninemensboard.png")

# Sets up the window
def setup():
    pygame.init()
    pygame.display.set_caption('Nine Men\'s Morris')
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    display.blit(BOARD_IMG, (0,0))
    pygame.display.flip()
    return display

# Starts a new game of nine mens morris
def newGame(display):
    game = Game(display)
    game.start()

if __name__ == "__main__":
    display = setup()
    newGame(display)
    