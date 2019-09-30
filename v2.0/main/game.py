import pygame
from board import Board
from player import Player

class Game:
    # Player identifiers
    WHITE = "white"
    BLACK = "black"
    PLAYER_ONE = 1
    PLAYER_TWO = 2

    def __init__(self, display):
        self.turn = 1
        self.display = display
        self.board = Board(display)
        self.playerOne = Player(self.PLAYER_ONE, self.WHITE)
        self.playerTwo = Player(self.PLAYER_TWO, self.BLACK)

    def start(self):
        self.board.create()
