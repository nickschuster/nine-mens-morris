import pygame
import random
from player import Player


class Agent(Player):
    # Represents all clickable positions on the game
    # board.
    POSSIBLE_ACTIONS = [0,1,2,3,4,5,6,7,
                        8,9,10,11,12,13,14,
                        15,16,17,18,19,20,21,
                        22,23]

    def __init__(self, number, sprite):
        super().__init__(number, sprite)

    def getAction(self):
        moves = []
        if self.phase == self.PLACEMENT_PHASE:
            moves.append(random.randint(0,23))
        elif self.phase == self.MOVING_PHASE:
            moves.append(random.randint(0,23))
            moves.append(random.randint(0,23))

        print(moves)
        return moves