import pygame
from mainGui import *
from easyScreen import *

(width, height) = (750,750)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

pygame.font.init()
pygame.display.set_caption('Minesweeper')

pygame.display.update()
mainScreen = mainScreen(screen)
easyScreen = easyScreen(screen, width, height)

# Currently for building and testing I am just skipping straight to the screen for the easy game!
currScreen = mainScreen
#currScreen = easyScreen

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
		elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
			currScreen.leftClick(width, height)
		elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
			if(currScreen != mainScreen):
				currScreen.rightClick(width, height)

	currScreen.load(width, height)
	if(currScreen.getChangeState() == "EASY"):
		currScreen = easyScreen
		currScreen.load(width, height)

	pygame.display.update()