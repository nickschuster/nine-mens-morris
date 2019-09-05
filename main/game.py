#game logic
import pygame;
from board import Board
from piece import Piece

class Game:

	def __init__(self, display, clock, whitePiece, blackPiece):
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
			if(turn == "white"):
				pieceImg = self.display.blit(self.whitePiece, (validPos[0] - 25,validPos[1] - 25));
			else:
				pieceImg = self.display.blit(self.blackPiece, (validPos[0] - 25,validPos[1] - 25));

			newPiece = Piece(turn, location, pieceImg);
			self.gameBoard.Pieces.append(newPiece);

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
								print(1);
								currentMouseX, currentMouseY = pygame.mouse.get_pos();
								self.display.blit(self.whitePiece, (currentMouseX, currentMouseY));
								pygame.display.flip();
								if event.type == pygame.MOUSEBUTTONDOWN:
									if event.button == 1:
										print(2)
										for pos in self.gameBoard.XYPoints:
											if ((currentMouseX <= pos[0]+self.hitBoxRadius and currentMouseX >= pos[0]-self.hitBoxRadius) and 
												(currentMouseY <= pos[1]+self.hitBoxRadius and currentMouseY >= pos[1]-self.hitBoxRadius)): 
													piece.locaiton = j;
													placed = True;
													valid = True;

										j = j + 1;


							

			i = i + 1;

		return valid;