import pygame
from board import Board
from player import Player

class Game:
    # Player identifiers
    PLAYER_ONE = 1
    PLAYER_TWO = 2

    def __init__(self, display):
        self.turn = PLAYER_ONE
        self.display = display
        self.board = Board(display)
        self.playerOne = Player(self.PLAYER_ONE)
        self.playerTwo = Player(self.PLAYER_TWO)

    def start(self):
        self.board.create()
        self.runGame()

    def runGame():
        while True:
            if self.turn == PLAYER_ONE:
                if self.playerOne.phase = self.playerOne.PLACEMENT_PHASE:
                    self.board.placePiece(self.playerOne)
