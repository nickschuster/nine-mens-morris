import pygame
from board import Board
from player import Player

class Game:
    # Player identifiers
    PLAYER_ONE = 1
    PLAYER_TWO = 2

    # Sprites
    BOARD_IMG = pygame.image.load("../assets/ninemensboard.png")
    PLAYER_ONE_IMG = pygame.image.load("../assets/whitepiece.png")
    PLAYER_TWO_IMG = pygame.image.load("../assets/blackpiece.png")

    def __init__(self, display):
        self.turn = self.PLAYER_ONE
        self.display = display
        self.board = Board(display, self.BOARD_IMG)
        self.playerOne = Player(self.PLAYER_ONE, self.PLAYER_ONE_IMG)
        self.playerTwo = Player(self.PLAYER_TWO, self.PLAYER_TWO_IMG)

    def start(self):
        self.board.create()
        self.runGame()

    def runGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.turn == self.playerOne.number:
                        if self.playerOne.phase == self.playerOne.PLACEMENT_PHASE:
                            self.board.placePiece(self.playerOne, event.pos)
                        count = self.board.checkForMill(self.playerOne)
                        
                    elif self.turn == self.playerTwo.number:
                        if self.playerTwo.phase == self.playerOne.PLACEMENT_PHASE:
                            self.board.plcaePiece(self.playerOne, event.pos)
                        self.board.checkForMill(self.playerTwo)

                    self.board.updateBoard(self.playerOne, self.playerTwo)