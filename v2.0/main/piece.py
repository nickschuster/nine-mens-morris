import pygame

class Piece:
	def __init__(self, posX, posY, ownedBy, sprite):
		self.sprite = sprite
		self.posX = posX
		self.posY = posY
		self.ownedBy = ownedBy