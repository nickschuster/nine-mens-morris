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
    # Returns nothing.
    def placePiece(self, player):
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                valid, index, piece = self.getValid(event.pos)
                if valid and piece == None:
                    self.newPiece(index, player)
                    self.numPieces += 1
                    player.numPieces += 1
                    print("placePiece")
                    break
        print("exit")

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
        for col in self.NUM_POINTS:
            for item in col:
                if item == index:
                    return rowIndex, colIndex
                rowIndex += 1
            rowIndex = 0    
            colIndex += 1

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
        print("Update board")
        self.display.blit(self.boardImg, (0,0))
        for piece in self.piecesOnBoard:
            if piece == playerOne.number:
                self.display.blit(playerOne.sprite, self.XY_POINTS[piece])
            elif piece == playerTwo.number:
                self.display.blit(playerTwo.sprite, self.XY_POINTS[piece])

