import pygame
from game import Game

# Dimensions
WINDOW_WIDTH = 1050
WINDOW_HEIGHT = 750
BUTTON_WIDTH = 280
BUTTON_HEIGHT = 100
BUTTON_X = 760
BUTTON_LOCAL_Y = 300
BUTTON_SINGLE_Y = 410
BUTTON_MUTLI_Y = 520
BUTTON_QUIT_Y = 630
TITLE_X = 900
TITLE_Y = 100
TITLE_BY_Y = 150
TITLE_NAME_Y = 200

# Indexs for readability
X = 0
Y = 1

# Button Identifiers
BUTTON_LOCAL = 1
BUTTON_SINGLE = 2
BUTTON_MULTI = 3
BUTTON_QUIT = 4

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

#Draws the title to display. Returns nothing.
def drawTitle(display):
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

# Draws the menu buttons to display. Records what button the mouse
# is on. 
#
# If clicked is true, returns the recorded button
def buttonHandeling(display, click=False):
    # If clicked is true return this
    buttonClicked = 0

    # Drawing buttons
    buttonLocal = pygame.Rect(BUTTON_X,BUTTON_LOCAL_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
    buttonSingle = pygame.Rect(BUTTON_X,BUTTON_SINGLE_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
    buttonMulti = pygame.Rect(BUTTON_X,BUTTON_MUTLI_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
    buttonQuit = pygame.Rect(BUTTON_X,BUTTON_QUIT_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
    pygame.draw.rect(display, RED, buttonLocal)
    pygame.draw.rect(display, RED, buttonSingle)
    pygame.draw.rect(display, RED, buttonMulti)
    pygame.draw.rect(display, RED, buttonQuit)

    # Button interactivity
    mouse = pygame.mouse.get_pos()
    if BUTTON_X < mouse[X] < BUTTON_X+BUTTON_WIDTH:
        if BUTTON_LOCAL_Y < mouse[Y] < BUTTON_LOCAL_Y+BUTTON_HEIGHT:
            pygame.draw.rect(display, LIGHT_RED, buttonLocal)
            buttonClicked = BUTTON_LOCAL
        if BUTTON_SINGLE_Y < mouse[Y] < BUTTON_SINGLE_Y+BUTTON_HEIGHT:
            pygame.draw.rect(display, LIGHT_RED, buttonSingle)
            buttonClicked = BUTTON_SINGLE
        if BUTTON_MUTLI_Y < mouse[Y] < BUTTON_MUTLI_Y+BUTTON_HEIGHT:
            pygame.draw.rect(display, LIGHT_RED, buttonMulti)
            buttonClicked = BUTTON_MULTI
        if BUTTON_QUIT_Y < mouse[Y] < BUTTON_QUIT_Y+BUTTON_HEIGHT:
            pygame.draw.rect(display, LIGHT_RED, buttonQuit)
            buttonClicked = BUTTON_QUIT

    if click:
        return buttonClicked

# Handles menu events. Draws menu items. Makes them interactive.
# Does framerate for program start. Returns nothing.
def menu(display, clock):
    intro = True
    while intro:
        # Test for user action
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttonClicked = buttonHandeling(display, True)
                if buttonClicked == BUTTON_SINGLE:
                    newGame(display)
                elif buttonClicked == BUTTON_LOCAL:
                    #TODO
                    newGame(display)
                elif buttonClicked == BUTTON_MULTI:
                    #TODO
                    newGame(display)
                elif buttonClicked == BUTTON_QUIT:
                    pygame.quit()
                    quit()

        # Emtpty the board and load a default bakcgorund color
        display.fill(WHITE)
        display.blit(BOARD_IMG, (0,0))

        # Draw menu elements
        buttonHandeling(display)
        drawTitle(display)

        # Update display and tick framerate
        pygame.display.update()
        clock.tick(30)


# Starts a new game of nine mens morris and
# passes the display to the Game to display on
def newGame(display):
    game = Game(display)
    game.start()

# Starts program execution
if __name__ == "__main__":
    display, clock = setup()
    menu(display, clock)

    #newGame(display)
    