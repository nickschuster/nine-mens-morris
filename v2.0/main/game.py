import pygame
import networkmanager
import time
from networkmanager import OnlinePlayer
from board import Board
from player import Player
from agent import Agent

class Game:
    # Game type identifiers
    LOCAL_MULTI = "localMulti"
    SINGLE = "single"
    MULTI = "multi"

    # Player identifiers
    PLAYER_ONE = 1
    PLAYER_TWO = 2
    PLAYER_ONE_STRING = "WHITE"
    PLAYER_TWO_STRING = "BLACK"

    # Game constant
    MAX_PIECES = 18

    # Sprites
    BOARD_IMG = pygame.image.load("../assets/ninemensboard.png")
    PLAYER_ONE_IMG = pygame.image.load("../assets/whitepiece.png")
    PLAYER_TWO_IMG = pygame.image.load("../assets/blackpiece.png")

    def __init__(self, display, clock, gameType):
        self.display = display
        self.board = Board(display, self.BOARD_IMG)

        # Determine what type of game it is going to be
        if gameType == self.LOCAL_MULTI:
            self.playerTwo = Player(self.PLAYER_TWO, self.PLAYER_TWO_IMG)
            self.playerOne = Player(self.PLAYER_ONE, self.PLAYER_ONE_IMG)
        elif gameType == self.SINGLE:
            # Loop to ensure getAction is checked often
            pygame.time.set_timer(pygame.USEREVENT, 100)
            self.playerTwo = Agent(self.PLAYER_TWO, self.PLAYER_TWO_IMG, self.board.piecesOnBoard)
            self.playerOne = Player(self.PLAYER_ONE, self.PLAYER_ONE_IMG)
        elif gameType == self.MULTI:
            self.playerTwo = networkmanager.getPlayerTwo(self.PLAYER_TWO, self.PLAYER_TWO_IMG)
            self.playerOne = networkmanager.getPlayerOne(self.PLAYER_ONE, self.PLAYER_ONE_IMG)

        self.turn = self.playerOne
        self.clock = clock
        self.gameType = gameType

    # Starts game execution.
    def start(self):
        self.board.create()
        win = self.runGame()
        return win

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

    # Dtermines the congratulatory message
    def getWin(self, player):
        if player.number == self.PLAYER_ONE:
            return self.PLAYER_ONE_STRING
        else:
            return self.PLAYER_TWO_STRING

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

                    if self.turn.phase == self.turn.MOVING_PHASE or self.turn.phase == self.turn.ROVING_PHASE:
                        validAction = self.board.movePiece(self.turn, event.pos, self.display, self.notTurn())

                    if validAction:
                        self.board.updateBoard()
                        totalMills = self.board.checkForMill(self.turn)
                        count = self.board.calculateNewMills(totalMills, self.turn)
                        self.board.takePiece(count, self.notTurn(), self.turn)
                        self.board.updateBoard()
                        self.changeTurn()
                        self.turn.checkWin()

                        # If its an online game send the previous move.
                        if self.gameType == self.MULTI:
                            if hasattr(self.turn, 'isOnline'):
                                self.turn.sendMove(event.pos)
                                self.notTurn().processed = True

                        # Update game phase
                        if self.board.numPieces == self.MAX_PIECES:
                            self.playerOne.updatePhase(self.turn.MOVING_PHASE)
                            self.playerTwo.updatePhase(self.turn.MOVING_PHASE)

                        # Update player phase and check if a valid move exists
                        if self.turn.phase == self.turn.MOVING_PHASE:
                            self.turn.lost = not self.board.canMove(self.turn)
                            self.turn.updatePhase()

                        # Check if the game is over.
                        if self.turn.lost == True:
                            winner = self.notTurn()
                            winString = self.getWin(winner)
                            return winString

                # Specific game type actions.
                if self.gameType == self.SINGLE:
                    if self.turn == self.playerTwo:
                        move = self.playerTwo.getAction(self.turn.PLACE_PICKUP)
                        pygame.event.clear()
                        action = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=self.board.XY_POINTS[move])
                        pygame.event.post(action)
                elif self.gameType == self.MULTI:
                    if hasattr(self.turn, 'isOnline'):
                        if self.turn.processed:
                            move = self.turn.getAction()
                            action = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=move)
                            pygame.event.post(action)
                            self.turn.processed = False



