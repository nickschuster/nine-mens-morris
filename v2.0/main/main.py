import pygame
from game import Game

# Dimensions
WINDOW_WIDTH = 1050
WINDOW_HEIGHT = 750

# For default look
BOARD_IMG = pygame.image.load("../assets/ninemensboard.png")

# Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (190,45,45)
LIGHT_RED = (255,0,0)

# Sets up the window
def setup():
    pygame.init()
    pygame.display.set_caption('Nine Men\'s Morris')
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    return display, clock

# Handles menu events
def menu(display, clock):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(WHITE)

        font = pygame.font.Font('freesansbold.ttf', 32) 
        text = font.render('GeeksForGeeks', True, BLACK, BLACK) 
        textRect = text.get_rect()  
        textRect.center = (500, 500) 

        mouse = pygame.mouse.get_pos()
        print(mouse)

        #pygame.draw.rect()

        
        pygame.display.update()
        clock.tick(30)


# Starts a new game of nine mens morris
def newGame(display):
    game = Game(display)
    game.start()

if __name__ == "__main__":
    display, clock = setup()
    menu(display, clock)

    #newGame(display)
    