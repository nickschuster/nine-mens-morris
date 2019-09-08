#game logic
import pygame
from board import Board
from piece import Piece

class Game:

    def __init__(self, display, clock, whitePiece, blackPiece, boardImg):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

        # The distance from the center of a valid location 
        #  the player has to click for it to be a valid move (pixels).
        self.hitBoxRadius = 15

        # A maximum of 18 pieces, 9 per player, can be on the board.
        self.maxPieces = 18

        # If a player has less than 3 pieces of the board they lose.
        self.minPieces = 3

        self.win = False

        # Three phases in nine mens morris. 
        #  Placement, moving and roving. Represented by 1, 2 and 3 respectively
        self.phase = 1

        # Piece sprites are exactly 50 x 50 pixels. 
        #  Images are drawn from top corner. Minus this to draw at middle.
        self.pieceMiddle = 25

        self.turn = "white"

        self.gameBoard = Board()

        self.display = display

        self.clock = clock

        self.whitePiece = whitePiece

        self.blackPiece = blackPiece

        self.boardImg = boardImg

    # Handels the placement of the pieces on to the board. Either in phase 1 or phase 2.
    def placePiece(self, turn, placement, phase, oldLocation=-1): 
        i = 0
        valid = False
        mouseX, mouseY = placement

        # For position pos if the cursor is at a valid position, 
        #  the position is not occupied or its the first piece being placed, 
        #  place or create a piece (depending on phase).
        for pos in self.gameBoard.XYPoints:
            if ((mouseX <= pos[0]+self.hitBoxRadius and mouseX >= pos[0]-self.hitBoxRadius) and
                (mouseY <= pos[1]+self.hitBoxRadius and mouseY >= pos[1]-self.hitBoxRadius)):

                if phase == 1:
                    #phase 1 placement check
                    newLocation = i;
                    if self.validMovement(newLocation, phase):
                        location = newLocation
                        validPos = pos
                        valid = True
                else:
                    # phase 2 and 3 placement check
                    newLocation = i;
                    if newLocation == oldLocation:
                        valid = True;
                    else:
                        if self.validMovement(newLocation, phase, oldLocation):
                            self.gameBoard.Pieces[oldLocation].location = newLocation
                            valid = True

            # index of positon/piece location (Look at Board for reference.)              
            i = i + 1

        if valid and phase == 1:
            newPiece = Piece(turn, location)
            self.gameBoard.Pieces.append(newPiece)
            
        self.drawCurrentBoard()

        return valid

    # Attaches piece to cursor in phase 2.
    def movePiece(self, turn, mousePosition):
        i = 0
        j = 0
        valid = False
        mouseX, mouseY = mousePosition

        # Get the piece at position pos if the cursor is at a valid position
        for pos in self.gameBoard.XYPoints:
            if ((mouseX <= pos[0]+self.hitBoxRadius and mouseX >= pos[0]-self.hitBoxRadius) and
                (mouseY <= pos[1]+self.hitBoxRadius and mouseY >= pos[1]-self.hitBoxRadius)):
                for piece in self.gameBoard.Pieces:
                    if piece.location == i:

                        # Attach piece to mouse cursor
                        placed = False
                        while not placed:
                            for event in pygame.event.get():
                                currentMouseX, currentMouseY = pygame.mouse.get_pos()

                                # Drawing of piece attached to mouse cursor
                                self.drawCurrentBoard(piece.location)
                                if(piece.color == "white"):
                                    self.display.blit(self.whitePiece,
                                                     (currentMouseX-self.pieceMiddle,
                                                      currentMouseY-self.pieceMiddle))
                                else:
                                    self.display.blit(self.blackPiece,
                                                     (currentMouseX-self.pieceMiddle,
                                                      currentMouseY-self.pieceMiddle))
                                self.clock.tick(60)
                                pygame.display.flip()

                                # Placement of piece after a completed movement
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    if event.button == 1:
                                        oldLocation = i
                                        if(self.placePiece(piece.color, (event.pos), self.phase, oldLocation)):
                                            valid = True
                                            placed = True

            i = i + 1

        return valid

    # Checks if the move is valid based on phase
    def validMovement(self, newLocation, phase, oldLocation=-1):
        valid = False
        # phase 1 and 3 can move anywhere except an occupied spot
        if phase == 1 or phase == 3:
            if len(self.gameBoard.Pieces) > 0:
                for piece in self.gameBoard.Pieces:
                    if piece.location == newLocation:
                        valid = False;
                        break
                    else:
                        valid = True
            else:
                valid = True;

        # phase 2 can only move to adjacent points        
        elif phase == 2:
            for i in range(len(self.gameBoard.NumPoints)):
                for j in range(len(self.gameBoard.NumPoints)):
                    if self.gameBoard.NumPoints[i][j] == oldLocation:
                        oldPoint = [i, j];
                    if self.gameBoard.NumPoints[i][j] == newLocation:
                        newPoint = [i, j];

            colDifference = oldPoint[0] - newPoint[0];
            rowDifference = oldPoint[1] - newPoint[1];

            if colDifference != 0 and rowDifference != 0:
                valid = False;
            elif colDifference != 0:
                if ((oldLocation - newLocation == 1) or 
                   (oldLocation - newLocation == -1)):
                    valid = True;
            elif rowDifference != 0:
                valid = False;
            else:
                valid = False;

        return valid

    # draws the pieces on the board in their current position
    def drawCurrentBoard(self, pieceToExclude=-1):
        i = 0

        # For position pos check if their is a piece on its location and then draw it
        self.display.blit(self.boardImg, (0,0))
        for pos in self.gameBoard.XYPoints:
            for piece in self.gameBoard.Pieces:
                if piece.location == i:

                    # During movement do not draw the piece that is being moved.
                    if pieceToExclude != -1:
                        if piece.location != pieceToExclude:
                            if piece.color == "white":
                                self.display.blit(self.whitePiece,
                                                 (pos[0]-self.pieceMiddle,
                                                  pos[1]-self.pieceMiddle))
                            else:
                                self.display.blit(self.blackPiece,
                                                 (pos[0]-self.pieceMiddle,
                                                  pos[1]-self.pieceMiddle))
                    else:
                        if piece.color == "white":
                            self.display.blit(self.whitePiece,
                                             (pos[0]-self.pieceMiddle,
                                              pos[1]-self.pieceMiddle))
                        else:
                            self.display.blit(self.blackPiece,
                                             (pos[0]-self.pieceMiddle,
                                              pos[1]-self.pieceMiddle))
            i = i + 1
