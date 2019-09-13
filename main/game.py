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

        # Keeps track of current mills so that they can not be 
        #  reused indefinitely.
        self.piecesInMill = []

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
                    # Phase 1 placement check
                    newLocation = i;
                    if self.validMovement(newLocation, phase):
                        location = newLocation
                        validPos = pos
                        valid = True
                else:
                    # Phase 2 and 3 placement check
                    newLocation = i;
                    if newLocation == oldLocation:
                        # Briefly swap turns so that on method exit they swapped back
                        # as picking up a piece and putting it back down should not
                        # count as a move
                        if(turn == "white"):
                            self.turn = "black";
                        else:
                            self.turn = "white"
                        valid = True
                    else:
                        if self.validMovement(newLocation, phase, oldLocation):
                            for piece in self.gameBoard.Pieces:
                                if piece.location == oldLocation:
                                    piece.location = newLocation;
                            valid = True

            # Index of positon/piece location (Look at Board for reference.)              
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
                    if piece.location == i and piece.color == turn:

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
                                pygame.display.flip();

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

        # Phase 2 can only move to adjacent points        
        elif phase == 2:
            # Getting current and new location values on grid
            for i in range(len(self.gameBoard.NumPoints)):
                for j in range(len(self.gameBoard.NumPoints)):
                    if self.gameBoard.NumPoints[i][j] == oldLocation:
                        oldPoint = [i, j];
                    if self.gameBoard.NumPoints[i][j] == newLocation:
                        newPoint = [i, j];

            # Comparring current and new location values
            colDifference = oldPoint[0] - newPoint[0];
            rowDifference = oldPoint[1] - newPoint[1];

            # Valid movement configurations (Board for reference)
            if colDifference != 0 and rowDifference != 0:
                valid = False;
            elif colDifference != 0:
                if oldPoint[1] == 0 or oldPoint[1] == 6:
                    if colDifference == 3 or colDifference == -3:
                        valid = True;
                if oldPoint[1] == 1 or oldPoint[1] == 5:
                    if colDifference == 2 or colDifference == -2:
                        valid = True;
                if oldPoint[1] == 2 or oldPoint[1] == 3 or oldPoint[1] == 4:
                    if colDifference == 1 or colDifference == -1:
                        valid = True;
            elif rowDifference != 0:
                if ((oldLocation - newLocation == 1) or 
                   (oldLocation - newLocation == -1)):
                    if not ((oldLocation == 11 or newLocation == 11) and 
                            (oldLocation == 12 or newLocation == 12)):
                        valid = True

            # Occupied check
            for piece in self.gameBoard.Pieces:
                if piece.location == newLocation:
                    valid = False;

        return valid

    # Returns the amount of mills for a given player
    def checkForMills(self, turn):
        currentPiecesInMills = []
        millCount = 0;
        for i in range(len(self.gameBoard.NumPoints)):
            columnMill = []
            rowMill = []
            for j in range(len(self.gameBoard.NumPoints)):
                columnMill.append(self.gameBoard.NumPoints[i][j])
                rowMill.append(self.gameBoard.NumPoints[j][i])
            
            # Mills in columns
            columnCount = 0;
            for k in columnMill:
                if k != -1:
                    for piece in self.gameBoard.Pieces:
                        if piece.color == turn and piece.location == k:
                            columnCount += 1 ;

            # Mills in rows
            rowCount = 0
            for j in rowMill:
                if j != -1:
                    for piece in self.gameBoard.Pieces:
                        if piece.color == turn and piece.location == j:
                            rowCount += 1


            if columnCount == 3:
                millCount += 1;
                currentPiecesInMills.append(columnMill)

        self.piecesInMill = currentPiecesInMills;
        return millCount

    # Returns true if a valid piece has been removed from the board
    #  called if there are mills 
    def takePiece(self, turn, count):
        print(count)
        return True

    # Checks win condition. If one player has less than 3 pieces on the board.
    #  Sets class variable accordingly.
    def checkForWin(self):
        self.win = False;

    # Draws the pieces on the board in their current position
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
