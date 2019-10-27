import pygame;
from piece import Piece

class Board:
    # Coordinates for visual placement
    XY_POINTS = [[54,52],[375,52],[697,52],
                 [160,160],[375,160],[590,160],
                 [268,265],[375,265],[483,265],
                 [54,372],[163,372],[269,372],
                 [482,372],[590,372],[697,372],
                 [269,480],[375,480],[482,480],
                 [162,586],[375,586],[589,586],
                 [54,694],[375,694],[696,694]]

    # An index of a sublist XY_POINTS (XY_POINTS[6]) cooresponds to a number in NUM_POINTS 
    # which identifies the X and Y position of a piece on the board
    # relative to other pieces on the board (6 in NUM_POINTS is [2, 2])
    NUM_POINTS = [[0,-1,-1,1,-1,-1,2],
                  [-1,3,-1,4,-1,5,-1],
                  [-1,-1,6,7,8,-1,-1],
                  [9,10,11,-1,12,13,14],
                  [-1,-1,15,16,17,-1,-1],
                  [-1,18,-1,19,-1,20,-1],
                  [21,-1,-1,22,-1,-1,23]]

    # Sizes
    BOARD_WIDTH = 750
    BOARD_HEIGHT = 750
    PIECE_WIDTH = 50
    PIECE_HEIGHT = 50
    PIECE_HITBOX = 25

    # Constructor
    def __init__(self, display, boardImg):
        self.display = display
        self.piecesOnBoard = {}
        self.numPieces = 0
        self.boardImg = boardImg

    # Create the initial board.
    #
    # Returns nothing
    def create(self):
        self.display.blit(self.boardImg, (0,0))
        pygame.display.flip()

    # In phase one place a piece on the board.
    #
    # Returns true or false depending on if a piece was placed.
    def placePiece(self, player, clickPos):
        valid, index, piece = self.getValid(clickPos)
        if valid and piece == None:
            self.newPiece(index, player)
            self.numPieces += 1
            player.numPieces += 1
            return True
        return False

    # Checks if the clicked position is:
    # valid, has an index, has a piece at its index
    #
    # Returns valid, index and the piece (or None)
    def getValid(self, clickPos):
        valid = False
        XYIndex = self.validXY(clickPos)
        piece = None
        if XYIndex != -1:
            piece = self.piecesOnBoard.get(XYIndex, None)
            valid = True
        return valid, XYIndex, piece

    # Determins if the click was at a valid location
    # 
    # Returns the index of the valid location (or -1)
    def validXY(self, clickPos):
        index = 0
        for XYPos in self.XY_POINTS:
            if (clickPos[0] + 25 >= XYPos[0] and clickPos[1] + 25 >= XYPos[1] and
                clickPos[0] - 25 <= XYPos[0] and clickPos[1] - 25 <= XYPos[1]):
                return index
            index += 1
        index = -1
        return index

    # Goes through the relative NUM_POINTS array to find
    # the location of a particular index
    # 
    # Returns that location (-1, -1 if it doesnt exist)
    def getRelativePosition(self, index):
        rowIndex = 0
        colIndex = 0
        for row in self.NUM_POINTS:
            for item in row:
                if item == index:
                    return rowIndex, colIndex
                colIndex += 1
            colIndex = 0    
            rowIndex += 1

    # Creates a new piece that is owned by the player
    # and adds that piece to the board dictionary of pieces
    #
    # Returns nothing
    def newPiece(self, index, player):
        row, col = self.getRelativePosition(index)
        newPiece = Piece(col, row, player.number, player.sprite)

        self.piecesOnBoard[index] = newPiece

    # Updates the board on the screen
    #
    # Returns nothing
    def updateBoard(self, playerOne, playerTwo):
        self.display.blit(self.boardImg, (0,0))
        for piece in self.piecesOnBoard:
            if self.piecesOnBoard[piece].ownedBy == playerOne.number:
                self.display.blit(self.piecesOnBoard[piece].sprite, 
                    [x-self.PIECE_HITBOX for x in self.XY_POINTS[piece]])
            else:
                self.display.blit(self.piecesOnBoard[piece].sprite,
                    [x-self.PIECE_HITBOX for x in self.XY_POINTS[piece]])
        pygame.display.flip()

    # Calculates the amount of new mills as an int. Updates
    # the old mills to the current mills on the board.
    #
    # Returns a count of the mills as an int.
    def calculateNewMills(self, totalMills, player):
        count = 0
        for mill in totalMills:
            if mill not in player.oldMills:
                count += 1
        player.oldMills = totalMills
        return count

    # Checks for mills on the board owned by 'player'. Refer to
    # NUM_POINTS for the logic of checking for a mill.
    # 
    # Returns an integer that represents the count of new mills.
    def checkForMill(self, player):
        rowMill = []
        colMill = []
        totalMills = []
        for rowIndex in range(len(self.NUM_POINTS)):
            for colIndex in range(len(self.NUM_POINTS)):
                rowItem = self.NUM_POINTS[rowIndex][colIndex]
                colItem = self.NUM_POINTS[colIndex][rowIndex]
                if rowItem != -1:
                    piece = self.piecesOnBoard.get(rowItem, None)
                    if piece != None:
                        if piece.ownedBy == player.number:
                            # If a piece exists and is owned by the correct player
                            rowMill.append(piece)
                            # Once two have been grabed
                            if len(rowMill) == 2:
                                # Are they on the same row/col
                                if rowMill[0].row == rowMill[1].row:
                                    # Are they in the center row/col of the board
                                    if rowMill[0].row == 3:
                                        colDiff = -1
                                    else:
                                        colDiff = rowMill[0].col - rowMill[1].col
                                else:
                                    # Reset and start again
                                    rowMill = []
                                    rowMill.append(piece)
                            # Once three pieces have been grabed and at least two are valid
                            if len(rowMill) == 3:
                                # Is the third piece on the same row/col
                                if rowMill[1].row == rowMill[2].row:
                                    newColDiff = rowMill[1].col - rowMill[2].col
                                    if newColDiff != colDiff:
                                        # Are they in the center row/col of the board
                                        if rowMill[0].row == 3:
                                            temp = [rowMill[1], rowMill[2]]
                                            rowMill = []
                                            rowMill.append(temp[0])
                                            rowMill.append(temp[1])
                                            colDiff == rowMill[0].col - rowMill[1].col
                                        else:
                                            # Reset and start again
                                            rowMill = []
                                            rowMill.append(piece)
                                else:
                                    # Reset and start again
                                    rowMill = []
                                    rowMill.append(piece)
                            if len(rowMill) == 3:
                                # Three valid pieces aka: a mill
                                totalMills.append(rowMill)
                                rowMill = []
                # SAME LOGIC AS FOR ROWS
                if colItem != -1:
                    piece = self.piecesOnBoard.get(colItem, None)
                    if piece != None:
                        if piece.ownedBy == player.number:
                            colMill.append(piece)
                            if len(colMill) == 2:
                                if colMill[0].col == colMill[1].col:
                                    if colMill[0].col == 3:
                                        rowDiff = -1
                                    else:
                                        rowDiff = colMill[0].row - colMill[1].row
                                else:
                                    colMill = []
                                    colMill.append(piece)
                            if len(colMill) == 3:
                                if colMill[1].col == colMill[2].col:
                                    newRowDiff = colMill[1].row - colMill[2].row
                                    if newRowDiff != rowDiff:
                                        if colMill[0].col == 3:
                                            temp = [colMill[1], colMill[2]]
                                            colMill = []
                                            colMill.append(temp[0])
                                            colMill.append(temp[1])
                                            rowDiff == colMill[0].row - colMill[1].row
                                        else:
                                            colMill = []
                                            colMill.append(piece)
                                else:
                                    colMill = []
                                    colMill.append(piece)
                            if len(colMill) == 3:
                                totalMills.append(colMill)
                                colMill = []

        print(len(totalMills))
        newMillCount = self.calculateNewMills(totalMills, player)
        print(newMillCount)
        return newMillCount








