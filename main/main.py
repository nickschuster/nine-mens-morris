#draws all game assets and handels all pygame logic
import pygame

pygame.init();

gameWidth = 750;
gameHeight = 750;

black = (0,0,0);
white = (255,255,255);
red = (255, 0, 0);

display = pygame.display.set_mode((gameHeight, gameWidth));

pygame.display.set_caption('Nine Men\'s Morris');

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
