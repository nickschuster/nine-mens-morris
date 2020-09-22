import pygame

class Piece:
    def __init__(self, col, row, ownedBy, sprite):
        self.sprite = sprite
        self.col = col
        self.row = row
        self.ownedBy = ownedBy