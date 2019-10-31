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

    # Moves a piece to a valid location on the board. 
    # If the movement is the same as the same position
    # as the original piece it exists.
    #
    # Returns true or false depending on if a valid move occurred.
    # An inplace move is not considered valid.
    def movePiece(self, player, clickPos, display):
        valid, index, piece = self.getValid(clickPos)
        if valid and piece != None:
            if piece.ownedBy == player.number:
                mouseX, mouseY = pygame.mouse.get_pos()
                notPlaced = True
                while notPlaced:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            newValid, newIndex, newPiece = self.getValid((mouseX, mouseY))
                            if newValid:
                                validMove = self.validateMove(newIndex, index, player)
                                if validMove:
                                    self.piecesOnBoard[newIndex] = piece
                                    del self.piecesOnBoard[index]
                                    self.updateBoard()
                                    return True
                                else:
                                    self.updateBoard()
                                    return False
                        if event.type == pygame.MOUSEMOTION:
                            self.updateBoard(index)
                            mouseX, mouseY = event.pos
                            display.blit(piece.sprite, (mouseX-self.PIECE_HITBOX, 
                                                        mouseY-self.PIECE_HITBOX))
                            pygame.display.flip()
                            break

    # Validates a movement of a piece. Assumes it was
    # called from movePiece function.
    #
    # Returns true or false depending on move validity.
    def validateMove(self, newIndex, oldIndex, player):
        if player.phase == player.ROVING_PHASE:
            return True
        elif newIndex == oldIndex:
            return False
        else:
            oldRow, oldCol = self.getRelativePosition(oldIndex)
            newRow, newCol = self.getRelativePosition(newIndex)
            rowDiff = oldRow - newRow
            colDiff = oldCol - newCol
            if rowDiff != 0 and colDiff != 0:
                return False
            elif rowDiff != 0:
                if oldRow == 0 or oldRow == 6:
                    if rowDiff != 3 or rowDiff != -3:
                        return False
            elif colDiff != 0: 
                if oldCol == 0 or oldCol == 6:
                    if colDiff != 3 or colDiff != -3:
                        return False
            return True


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

    # Updates the board on the screen. Can choose to 
    # ignore one piece. Used when that piece is in movement.
    #
    # Returns nothing
    def updateBoard(self, ignore=-1):
        self.display.blit(self.boardImg, (0,0))
        for pieceIndex in self.piecesOnBoard:
            if pieceIndex != ignore:
                self.display.blit(self.piecesOnBoard[pieceIndex].sprite, 
                    [x-self.PIECE_HITBOX for x in self.XY_POINTS[pieceIndex]])
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
                # Ensure a valid index
                if rowItem != -1:
                    piece = self.piecesOnBoard.get(rowItem, None)
                    # A piece exists at a valid index
                    if piece != None:
                        # Piece is owned by current player
                        if piece.ownedBy == player.number:
                            rowMill.append(piece)
                            # Two pieces in a row
                            if len(rowMill) == 2:
                                # Are they on the same row
                                if rowMill[0].row != rowMill[1].row:
                                    # Reset
                                    rowMill = []
                                    rowMill.append(piece)
                                # Are they on row 3 (4), refer to NUM_POINTS
                                elif rowMill[0].row == 3:
                                    # Check distance from each other
                                    if rowMill[0].col - rowMill[1].col != -1:
                                        # Reset
                                        rowMill = []
                                        rowMill.append(piece)
                            # Three in a row
                            if len(rowMill) == 3:
                                # Last two on same row
                                if rowMill[1].row != rowMill[2].row:
                                    # Reset
                                    rowMill = []
                                    rowMill.append(piece)
                                # Are they on row 3 (4), refer to NUM_POINTS
                                elif rowMill[2].row == 3:
                                    # Check distance from each other
                                    if rowMill[1].col - rowMill[2].col != -1:
                                        # Reset
                                        rowMill = []
                                        rowMill.append(piece)
                            # Valid 3 in a row/Mill found
                            if len(rowMill) == 3:
                                totalMills.append(rowMill)
                                rowMill = []
                # Refer to row logic
                if colItem != -1:
                    piece = self.piecesOnBoard.get(colItem, None)
                    if piece != None:
                        if piece.ownedBy == player.number:
                            colMill.append(piece)
                            if len(colMill) == 2:
                                if colMill[0].col != colMill[1].col:
                                    colMill = []
                                    colMill.append(piece)
                                elif colMill[0].col == 3:
                                    if colMill[0].row - colMill[1].row != -1:
                                        colMill = []
                                        colMill.append(piece)
                            if len(colMill) == 3:
                                if colMill[1].col != colMill[2].col:
                                    colMill = []
                                    colMill.append(piece)
                                elif colMill[2].col == 3:
                                    if colMill[1].row - colMill[2].row != -1:
                                        colMill = []
                                        colMill.append(piece)
                            if len(colMill) == 3:
                                totalMills.append(colMill)
                                colMill = []
        # Check how many mills are new
        count = self.calculateNewMills(totalMills, player)
        return count







