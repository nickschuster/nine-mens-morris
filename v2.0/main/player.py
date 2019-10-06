import pygame

class Player:
    # Phase identifiers
    PLACEMENT_PHASE = 0
    MOVING_PHASE = 1
    ROVING_PHASE = 2

    def __init__(self, number):
        self.number = number
        self.phase = self.PLACEMENT_PHASE
        self.numPieces = 0
        self.hasWon = False
