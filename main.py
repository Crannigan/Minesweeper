import pygame
from mainGui import *
from easyScreen import *

(width, height) = (750,750)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

pygame.font.init()
pygame.display.set_caption('Zech\'s Minesweeper')

pygame.display.update()
mainScreen = mainScreen(screen)
easyScreen = easyScreen(screen)

#currScreen = mainScreen
currScreen = easyScreen

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.VIDEORESIZE:
			scrsize = event.size
			width = event.w
			height = event.h
			screen = pygame.display.set_mode(scrsize,pygame.RESIZABLE)
			changed = True
		elif event.type == pygame.MOUSEBUTTONUP:
			currScreen.click(width, height)

	currScreen.load(width, height)
	if(currScreen.getChangeState() == "EASY"):
		currScreen = easyScreen
		currScreen.load(width, height)

	pygame.display.update()