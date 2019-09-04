#draws all game assets and handels all pygame logic
import pygame
from board import Board
from piece import Piece

pygame.init();

black = (0,0,0);
white = (255,255,255);
red = (255, 0, 0);

gameWidth = 750;
gameHeight = 750;

hitBoxRadius = 15;

maxPieces = 18;

win = False;

phase = 1;

turn = "white";

display = pygame.display.set_mode((gameHeight, gameWidth));

pygame.display.set_caption('Nine Men\'s Morris');

boardImg = pygame.image.load("../assets/ninemensboard.png");
whitePiece = pygame.image.load("../assets/whitepiece.png");
blackPiece = pygame.image.load("../assets/blackpiece.png");

display.blit(boardImg, (0,0));

clock = pygame.time.Clock();

gameBoard = Board();

def updateBoard(): 

	for piece in gameBoard.Pieces:
		pos = gameBoard.XYPoints[piece.location];
		if(piece.color == "white"):
			display.blit(whitePiece, (pos[0] - 25,pos[1] - 25));
		else:
			display.blit(blackPiece, (pos[0] - 25,pos[1] - 25));

	pygame.display.flip();

def placePiece(turn, placement):
	i = 0
	valid = False
	mouseX, mouseY = placement
	for pos in gameBoard.XYPoints:
		if ((mouseX <= pos[0]+hitBoxRadius and mouseX >= pos[0]-hitBoxRadius) and 
			(mouseY <= pos[1]+hitBoxRadius and mouseY >= pos[1]-hitBoxRadius)):
			newPiece = Piece(turn, i);
			if len(gameBoard.Pieces) > 0:
				for piece in gameBoard.Pieces:
					if piece.location == newPiece.location:
						valid = False;
						break;
					else:
						valid = True;
			else: 
				valid = True;

		i = i + 1;

	if valid:
		gameBoard.Pieces.append(newPiece);

	return valid;

def movePiece(turn, mousePosition):
	i = 0;
	j = 0;
	valid = False;
	mouseX, mouseY = mousePosition;
	for pos in gameBoard.XYPoints:
		if ((mouseX <= pos[0]+hitBoxRadius and mouseX >= pos[0]-hitBoxRadius) and 
			(mouseY <= pos[1]+hitBoxRadius and mouseY >= pos[1]-hitBoxRadius)):
			for piece in gameBoard.Pieces:
				if piece.location == i:
					#Attach piece to mouse cursor
					placed = False
					while not placed:
						


#MAIN LOOP
while not win:
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			pygame.quit();
			quit();
		elif(event.type) == pygame.MOUSEBUTTONDOWN:
			if(event.button == 1):
				if len(gameBoard.Pieces) == maxPieces:
					phase = 2;

				if(phase == 1):
					if(placePiece(turn, event.pos)):
						if(turn == "white"):
							turn = "black";
						else:
							turn = "white";

				if(phase == 2):
					if(movePiece(turn, event.pos)):
						#TODO
						if(turn == "white"):
							turn = "black";
						else:
							turn = "white";
						
		updateBoard();
		clock.tick();
