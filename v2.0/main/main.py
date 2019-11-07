import pygame; pygame.init()
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

# Button lables
LOCAL_LABEL = "Local multiplayer"
MULTI_LABEL = "Online multiplayer"
SINGLE_LABEL = "Single player"
QUIT_LABEL = "Quit"

# Title strings
TITLE = 'Nine Men\'s Morris'
BY = 'By'
NAME = 'Nikolas Schuster'

# Won strings
WHITE_WIN ="WHITE WINS"
BLACK_WIN = "BLACK WINS"

# For the default look. The board image.
BOARD_IMG = pygame.image.load("../assets/ninemensboard.png")

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (190,45,45)
LIGHT_RED = (255,0,0)

# Font options
FONT = 'Monsterrat-Regular'
LARGE_TEXT = pygame.font.SysFont(FONT, 45) 
MEDIUM_TEXT = pygame.font.SysFont(FONT, 35) 
SMALL_TEXT = pygame.font.SysFont(FONT, 25) 

# Sets up the window
def setup():
    pygame.display.set_caption('Nine Men\'s Morris')
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    return display, clock

# Draws the title to display. 
#
# Returns nothing.
def drawTitle(display):
    title = LARGE_TEXT.render(TITLE, True, BLACK, WHITE) 
    titleRect = title.get_rect()  
    titleRect.center = (TITLE_X, TITLE_Y)

    by = LARGE_TEXT.render(BY, True, BLACK, WHITE)
    byRect = by.get_rect()
    byRect.center = (TITLE_X, TITLE_BY_Y)

    name = LARGE_TEXT.render(NAME, True, BLACK, WHITE)
    nameRect = name.get_rect()
    nameRect.center = (TITLE_X, TITLE_NAME_Y)

    display.blit(title, titleRect)
    display.blit(by, byRect)
    display.blit(name, nameRect)

# Draws the buttons to the display. Lights up the button
# the mouse is hovering over.
#
# Returns the button the mouse is currently hovering over.
def buttonInteractivity(display):
    # Drawing of button
    buttonLocal = pygame.Rect(BUTTON_X,BUTTON_LOCAL_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
    buttonSingle = pygame.Rect(BUTTON_X,BUTTON_SINGLE_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
    buttonMulti = pygame.Rect(BUTTON_X,BUTTON_MUTLI_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
    buttonQuit = pygame.Rect(BUTTON_X,BUTTON_QUIT_Y,BUTTON_WIDTH,BUTTON_HEIGHT)
    pygame.draw.rect(display, RED, buttonLocal)
    pygame.draw.rect(display, RED, buttonSingle)
    pygame.draw.rect(display, RED, buttonMulti)
    pygame.draw.rect(display, RED, buttonQuit)

    # Reocrding and highlighting of button
    button = 0
    mouse = pygame.mouse.get_pos()
    if BUTTON_X < mouse[X] < BUTTON_X+BUTTON_WIDTH:
        if BUTTON_LOCAL_Y < mouse[Y] < BUTTON_LOCAL_Y+BUTTON_HEIGHT:
            pygame.draw.rect(display, LIGHT_RED, buttonLocal)
            button = BUTTON_LOCAL
        if BUTTON_SINGLE_Y < mouse[Y] < BUTTON_SINGLE_Y+BUTTON_HEIGHT:
            pygame.draw.rect(display, LIGHT_RED, buttonSingle)
            button = BUTTON_SINGLE
        if BUTTON_MUTLI_Y < mouse[Y] < BUTTON_MUTLI_Y+BUTTON_HEIGHT:
            pygame.draw.rect(display, LIGHT_RED, buttonMulti)
            button = BUTTON_MULTI
        if BUTTON_QUIT_Y < mouse[Y] < BUTTON_QUIT_Y+BUTTON_HEIGHT:
            pygame.draw.rect(display, LIGHT_RED, buttonQuit)
            button = BUTTON_QUIT

    return button

def drawButtonLabels(display):   
    localText = MEDIUM_TEXT.render(LOCAL_LABEL, True, BLACK) 
    localTextRect = localText.get_rect()  
    localTextRect.center = (BUTTON_X+(BUTTON_WIDTH/2), BUTTON_LOCAL_Y+(BUTTON_HEIGHT/2))

    multiText = MEDIUM_TEXT.render(MULTI_LABEL, True, BLACK) 
    multiTextRect = localText.get_rect()  
    multiTextRect.center = (BUTTON_X+(BUTTON_WIDTH/2), BUTTON_MUTLI_Y+(BUTTON_HEIGHT/2))

    singleText = MEDIUM_TEXT.render(SINGLE_LABEL, True, BLACK) 
    singleTextRect = singleText.get_rect()  
    singleTextRect.center = (BUTTON_X+(BUTTON_WIDTH/2), BUTTON_SINGLE_Y+(BUTTON_HEIGHT/2))

    quitText = MEDIUM_TEXT.render(QUIT_LABEL, True, BLACK) 
    quitTextRect = quitText.get_rect()  
    quitTextRect.center = (BUTTON_X+(BUTTON_WIDTH/2), BUTTON_QUIT_Y+(BUTTON_HEIGHT/2))

    display.blit(localText, localTextRect)
    display.blit(multiText, multiTextRect)
    display.blit(singleText, singleTextRect)
    display.blit(quitText, quitTextRect)

# Draws the menu buttons to display. Records what button the mouse
# is on. 
#
# If click is true, returns the recorded button
def buttonHandeling(display, click=False):

    button = buttonInteractivity(display)
    drawButtonLabels(display)

    if click:
        return button

# Handles menu events. Draws menu items. Makes them interactive.
# Does framerate for program start. 
#
# Returns nothing.
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
                    intro = False
                    single = True
                    break
                elif buttonClicked == BUTTON_LOCAL:
                    #TODO
                    local = True
                elif buttonClicked == BUTTON_MULTI:
                    #TODO
                    multi = True
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

    #buttonHandeling(display)
    if single:
        newGame(display, clock)

def displayWin(win):
    winText = MEDIUM_TEXT.render(win+" WINS", True, WHITE) 
    winTextRect = winText.get_rect() 
    winTextRect.center = (WINDOW_HEIGHT/2, WINDOW_HEIGHT/2)
    display.blit(winText, winTextRect)

# Starts a new game of nine mens morris and
# passes the display to the Game to display on
#
# Returns nothing
def newGame(display, clock):
    # Hide menu on game start
    display = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_HEIGHT))
    game = Game(display, clock)
    win = game.start()
    displayWin(win)

    # Reset window when game done.
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Starts program execution
if __name__ == "__main__":
    display, clock = setup()
    menu(display, clock)
    