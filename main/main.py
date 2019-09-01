#draws all game assets and handels all pygame logic
import pygame
from board import Board

pygame.init();

gameWidth = 750;
gameHeight = 750;

black = (0,0,0);
white = (255,255,255);
red = (255, 0, 0);

display = pygame.display.set_mode((gameHeight, gameWidth));

pygame.display.set_caption('Nine Men\'s Morris');

boardImg = pygame.image.load("../assets/ninemensboard.png");
whitePiece = pygame.image.load("../assets/whitepiece.png");
blackPiece = pygame.image.load("../assets/blackpiece.png");

display.blit(boardImg, (0,0));

gameBoard = Board();

i = 0;
for pos in gameBoard.XYPoints:
	if(i < 9):
		display.blit(whitePiece, (pos[0] - 25,pos[1] - 25));
	elif(i < 18):
		display.blit(blackPiece, (pos[0] - 25,pos[1] - 25));
	else:
		pygame.draw.circle(display, red, pos, 20);

	i = i + 1

pygame.display.flip();

clock = pygame.time.Clock();

crashed = False;

while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True;

		pygame.display.update();

		clock.tick(60);

pygame.quit();

quit();
