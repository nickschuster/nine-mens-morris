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
            if self.turn == self.PLAYER_ONE:
                if self.playerOne.phase == self.playerOne.PLACEMENT_PHASE:
                    self.board.placePiece(self.playerOne)
                    print("Here")
            self.board.updateBoard(self.playerOne, self.playerTwo)
