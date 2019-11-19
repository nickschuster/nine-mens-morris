import pygame
import random
from player import Player


class Agent(Player):
    # Context of action for agent
    PLACE_PICKUP = 0
    TAKE = 1
    PUTDOWN = 2
    PLACE = 3
    PICKUP = 4

    # Represents all clickable positions on the game
    # board.
    POSSIBLE_ACTIONS = [0,1,2,3,4,5,6,7,
                        8,9,10,11,12,13,14,
                        15,16,17,18,19,20,21,
                        22,23]

    # Constructor
    def __init__(self, number, sprite, board):
        super().__init__(number, sprite)
        self.isAgent = True
        self.context = self.PLACE
        self.currentBoard = board

    def updateContext(self, context):
        if context == self.PLACE_PICKUP:
            if self.phase == self.MOVING_PHASE:
                self.context = self.PICKUP
            else:
                self.context = self.PLACE
        else:
            self.context = self.context

    # Gets the position on the board the agent wants to click
    def getAction(self, context):
        print(self.currentBoard)
        self.updateContext(context)
        action = random.randint(0,23)
        return action