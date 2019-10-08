import pygame;

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

    # Game sprites
    BOARD_IMG = pygame.image.load("../assets/ninemensboard.png")
    PLAYER_ONE_IMG = pygame.image.load("../assets/whitepiece.png")
    PLAYER_TWO_IMG = pygame.image.load("../assets/blackpiece.png")

    # Sizes
    BOARD_WIDTH = 750
    BOARD_HEIGHT = 750
    PIECE_WIDTH = 50
    PIECE_HEIGHT = 50

    def __init__(self, display):
        self.display = display
        self.piecesOnBoard = {}
        self.placedPieces = 0

    def create(self):
        self.display.blit(self.BOARD_IMG, (0,0))
        pygame.display.flip()

    def placePiece(self, player):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                valid, position = self.getValid(event.pos)

    def getValid(self, clickPos):
        XYIndex = self.validXY(clickPos)
        print(XYIndex)
        return True, XYIndex

    def validXY(self, clickPos):
        index = 0
        for XYPos in self.XY_POINTS:
            if (clickPos[0] + 25 >= XYPos[0] and clickPos[1] + 25 >= XYPos[1] and
                clickPos[0] - 25 <= XYPos[0] and clickPos[1] - 25 <= XYPos[1]):
                return index
            index += 1
            print(clickPos)
            print(clickPos[0] + 25 < XYPos[0] and clickPos[1] + 25 < XYPos[1])
            print(clickPos[0] - 25 > XYPos[0] and clickPos[1] - 25 > XYPos[1])
            print(XYPos)

