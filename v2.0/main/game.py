import pygame
from board import Board
from player import Player

class Game:
    # Player identifiers
    PLAYER_ONE = 1
    PLAYER_TWO = 2

    # Title
    # SINGLE_TITLE = "Single Player Game"

    # Sprites
    BOARD_IMG = pygame.image.load("../assets/ninemensboard.png")
    PLAYER_ONE_IMG = pygame.image.load("../assets/whitepiece.png")
    PLAYER_TWO_IMG = pygame.image.load("../assets/blackpiece.png")

    def __init__(self, display, clock):
        self.display = display
        self.board = Board(display, self.BOARD_IMG)
        self.playerOne = Player(self.PLAYER_ONE, self.PLAYER_ONE_IMG)
        self.playerTwo = Player(self.PLAYER_TWO, self.PLAYER_TWO_IMG)
        self.turn = self.playerOne
        self.clock = clock

    # Starts game execution.
    def start(self):
        self.board.create()
        self.runGame()

    # Changes the game turn.
    def changeTurn(self):
        if self.turn == self.playerOne:
            self.turn = self.playerTwo
        else:
            self.turn = self.playerOne

    # Returns the player opposite to 
    # the current turn.
    def notTurn(self):
        if self.turn == self.playerOne:
            return self.playerTwo
        else:
            return self.playerOne

    # Main game loop.
    def runGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.turn.phase == self.turn.PLACEMENT_PHASE:
                        validAction = self.board.placePiece(self.turn, event.pos)

                    if self.turn.phase == self.turn.MOVING_PHASE:
                        validAction = self.board.movePiece(self.turn, event.pos, self.display)

                    if validAction:
                        self.board.updateBoard()
                        totalMills = self.board.checkForMill(self.turn)
                        print(len(totalMills))
                        count = self.board.calculateNewMills(totalMills, self.turn)
                        print(count)
                        self.board.takePiece(count, self.notTurn())
                        self.board.updateBoard()
                        self.changeTurn()

                        # Update player phase
                        if self.turn.phase == self.turn.MOVING_PHASE:
                            self.turn.updatePhase

                        # Update game phase
                        if self.board.numPieces == 18:
                            self.playerOne.updatePhase(1)
                            self.playerTwo.updatePhase(1)