#draws all game assets and handels all pygame logic
import pygame

pygame.init();

display = pygame.display.set_mode((600,600));

pygame.display.set_caption('Nine Men\'s Morris');

clock = pygame.time.Clock();

crashed = False;

while not crashed:
	for event in pygame.event.get();
		if event.type == pygame.QUIT:
			crashed = True;

		print(event);

		pygame.display.update();

		clock.tick(60);

pygame.quit();

quit();
