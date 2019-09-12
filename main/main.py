#main loop, asset loading, pygame details
import pygame; pygame.init()
from game import Game
from board import Board
from piece import Piece

gameWidth = 750
gameHeight = 750

display = pygame.display.set_mode((gameHeight, gameWidth))

pygame.display.set_caption('Nine Men\'s Morris')

boardImg = pygame.image.load("../assets/ninemensboard.png").convert_alpha()
whitePiece = pygame.image.load("../assets/whitepiece.png").convert_alpha()
blackPiece = pygame.image.load("../assets/blackpiece.png").convert_alpha()

display.blit(boardImg, (0,0))

clock = pygame.time.Clock()

game = Game(display, clock, whitePiece, blackPiece, boardImg)               

#MAIN LOOP
while not game.win:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if len(game.gameBoard.Pieces) == game.maxPieces:
                    game.phase = 2

                if game.phase == 1:
                    if(game.placePiece(game.turn, event.pos, game.phase)):
                        millCount = game.checkForMills(game.turn);
                        if(game.takePiece(game.turn, millCount)):
                            if(game.turn == "white"):
                                game.turn = "black"
                            else:
                                game.turn = "white"

                if game.phase == 2:
                    if game.movePiece(game.turn, event.pos):
                        millCount = game.checkForMills(game.turn);
                        if(game.takePiece(game.turn, millCount)):
                            if(game.turn == "white"):
                                game.turn = "black"
                            else:
                                game.turn = "white"

        game.checkForWin();    
        pygame.display.flip()
        clock.tick()
