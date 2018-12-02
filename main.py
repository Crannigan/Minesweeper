import pygame
from mainGui import *
from screen import *

(width, height) = (750,750)
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

pygame.font.init()
pygame.display.set_caption('Minesweeper')

pygame.display.update()
mainScreen = mainScreen(screen)
easyScreen = easyScreen(screen, width, height)
fairScreen = fairScreen(screen, width, height)
hardScreen = hardScreen(screen, width, height)

currScreen = mainScreen

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

	
	if(currScreen.getChangeState() == "EASY"):
		currScreen = easyScreen
		currScreen.make(width, height)
	elif(currScreen.getChangeState() == "FAIR"):
		currScreen = fairScreen
		currScreen.make(width, height)
	elif(currScreen.getChangeState() == "HARD"):
		currScreen = hardScreen
		currScreen.make(width, height)
	
	currScreen.load(width, height)

	pygame.display.update()