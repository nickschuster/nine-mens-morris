import pygame
from board import Board
from player import Player

class Game:
	WHITE = "white"
	BLACK = "black"
	PLAYER_ONE = 1
	PLAYER_TWO = 2

	def __init__(self):
		self.turn = 1
		self.board = Board()
		self.playerOne = Player(self.PLAYER_ONE, self.WHITE)
		self.playerTwo = Player(self.PLAYER_TWO, self.BLACK)

