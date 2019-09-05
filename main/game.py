#game logic
import pygame;
from board import Board
from piece import Piece

class Game:

	def __init__(self, display, clock, whitePiece, blackPiece, boardImg):
		self.black = (0,0,0);
		self.white = (255,255,255);
		self.red = (255, 0, 0);

		self.hitBoxRadius = 15;

		self.maxPieces = 18;

		self.win = False;

		self.phase = 1;

		self.turn = "white";

		self.gameBoard = Board();

		self.display = display;

		self.clock = clock;

		self.whitePiece = whitePiece;

		self.blackPiece = blackPiece;

		self.boardImg = boardImg;

	def placePiece(self, turn, placement):
		i = 0
		valid = False
		mouseX, mouseY = placement
		for pos in self.gameBoard.XYPoints:
			if ((mouseX <= pos[0]+self.hitBoxRadius and mouseX >= pos[0]-self.hitBoxRadius) and 
				(mouseY <= pos[1]+self.hitBoxRadius and mouseY >= pos[1]-self.hitBoxRadius)):
				if len(self.gameBoard.Pieces) > 0:
					for piece in self.gameBoard.Pieces:
						if piece.location == i:
							valid = False;
							break;
						else:
							location = i;
							validPos = pos;
							valid = True;
				else: 
					location = i;
					validPos = pos;
					valid = True;

			i = i + 1;

		if valid:
			newPiece = Piece(turn, location);
			self.gameBoard.Pieces.append(newPiece);
			self.drawCurrentBoard();

		return valid;

	def movePiece(self, turn, mousePosition):
		i = 0;
		j = 0;
		valid = False;
		mouseX, mouseY = mousePosition;
		for pos in self.gameBoard.XYPoints:
			if ((mouseX <= pos[0]+self.hitBoxRadius and mouseX >= pos[0]-self.hitBoxRadius) and 
				(mouseY <= pos[1]+self.hitBoxRadius and mouseY >= pos[1]-self.hitBoxRadius)):
				for piece in self.gameBoard.Pieces:
					if piece.location == i:
						#Attach piece to mouse cursor
						#TODO
						placed = False;
						while not placed:
							for event in pygame.event.get():
								self.display.blit(self.boardImg, (0,0));
								self.drawCurrentBoard(piece.location);
								currentMouseX, currentMouseY = pygame.mouse.get_pos();
								self.display.blit(self.whitePiece, (currentMouseX-25, currentMouseY-25));
								self.clock.tick(5000);
								pygame.display.flip();
								if event.type == pygame.MOUSEBUTTONDOWN:
									if event.button == 1:
										for pos in self.gameBoard.XYPoints:
											if ((currentMouseX <= pos[0]+self.hitBoxRadius and currentMouseX >= pos[0]-self.hitBoxRadius) and 
												(currentMouseY <= pos[1]+self.hitBoxRadius and currentMouseY >= pos[1]-self.hitBoxRadius)): 
													piece.locaiton = j;
													placed = True;
													valid = True;

										j = j + 1;


							

			i = i + 1;

		return valid;

	def drawCurrentBoard(self, pieceToExclude=-1):
		i = 0;
		for pos in self.gameBoard.XYPoints:
			for piece in self.gameBoard.Pieces:
				if piece.location == i:
					if pieceToExclude != -1:
						if piece.location != pieceToExclude:
							if piece.color == "white":
								self.display.blit(self.whitePiece, (pos[0]-25, pos[1]-25));
							else:
								self.display.blit(self.blackPiece, (pos[0]-25, pos[1]-25));
					else:
						if piece.color == "white":
							self.display.blit(self.whitePiece, (pos[0]-25, pos[1]-25));
						else:
							self.display.blit(self.blackPiece, (pos[0]-25, pos[1]-25));
			i = i + 1;
