import pygame
from game import Game

# Dimensions
WINDOW_WIDTH = 1050
WINDOW_HEIGHT = 750
BUTTON_WIDTH = 280
BUTTON_HEIGHT = 100
BUTTON_X = 760
BUTTON_ONE_Y = 300
BUTTON_TWO_Y = 410
BUTTON_THREE_Y = 520
BUTTON_FOUR_Y = 630
TITLE_X = 900
TITLE_Y = 100
TITLE_BY_Y = 150
TITLE_NAME_Y = 200

# Indexs for readability
X = 0
Y = 1

# Title strings
TITLE = 'Nine Men\'s Morris'
BY = 'By'
NAME = 'Nikolas Schuster'

# For default look
BOARD_IMG = pygame.image.load("../assets/ninemensboard.png")

# Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (190,45,45)
LIGHT_RED = (255,0,0)

# Font options
FONT = 'Monsterrat-Regular'
FONT_SIZE = 45

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

        # Background
        display.fill(WHITE)

        # Empty board
        display.blit(BOARD_IMG, (0,0))

        # Title
        font = pygame.font.SysFont(FONT, FONT_SIZE) 
        title = font.render(TITLE, True, BLACK, WHITE) 
        titleRect = title.get_rect()  
        titleRect.center = (TITLE_X, TITLE_Y)
        by = font.render(BY, True, BLACK, WHITE)
        byRect = by.get_rect()
        byRect.center = (TITLE_X, TITLE_BY_Y)
        name = font.render(NAME, True, BLACK, WHITE)
        nameRect = name.get_rect()
        nameRect.center = (TITLE_X, TITLE_NAME_Y)
        display.blit(title, titleRect)
        display.blit(by, byRect)
        display.blit(name, nameRect)

        # Menu buttons
        buttonLocal = pygame.Rect(BUTTON_X,BUTTON_ONE_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
        buttonSingle = pygame.Rect(BUTTON_X,BUTTON_TWO_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
        buttonMulti = pygame.Rect(BUTTON_X,BUTTON_THREE_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
        buttonQuit = pygame.Rect(BUTTON_X,BUTTON_FOUR_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
        pygame.draw.rect(display, RED, buttonLocal)
        pygame.draw.rect(display, RED, buttonSingle)
        pygame.draw.rect(display, RED, buttonMulti)
        pygame.draw.rect(display, RED, buttonQuit)

        # Button interactivity
        mouse = pygame.mouse.get_pos()
        if BUTTON_X < mouse[X] < BUTTON_X+BUTTON_WIDTH:
            if BUTTON_ONE_Y < mouse[Y] < BUTTON_ONE_Y+BUTTON_HEIGHT:
                pygame.draw.rect(display, LIGHT_RED, buttonLocal)
            if BUTTON_TWO_Y < mouse[Y] < BUTTON_TWO_Y+BUTTON_HEIGHT:
                pygame.draw.rect(display, LIGHT_RED, buttonSingle)
            if BUTTON_THREE_Y < mouse[Y] < BUTTON_THREE_Y+BUTTON_HEIGHT:
                pygame.draw.rect(display, LIGHT_RED, buttonMulti)
            if BUTTON_FOUR_Y < mouse[Y] < BUTTON_FOUR_Y+BUTTON_HEIGHT:
                pygame.draw.rect(display, LIGHT_RED, buttonQuit)


        # Update
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
    