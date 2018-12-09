import pygame
from gameState import *

class easyScreen:
	changeState = "GAME"
	def __init__(self, screen, width, height):
		self.screen = screen
		self.gray = (128,128,128)
		self.red = (255,0,0)
		self.numXPieces = 8
		self.numYPieces = 8
		self.bombNum = 10
		self.gameState = gameState(self.screen, self.numXPieces, self.numYPieces, width, height, self.bombNum)

	def load(self, width, height):
		self.draw(width, height)


	def draw(self, width, height):
		self.screen.fill(self.gray)
		self.gameState.draw(width, height)

	def getChangeState(self):
		return self.changeState

	def leftClick(self, width, height):
		mouseX, mouseY = pygame.mouse.get_pos()
		#test if go home/main
		leftx = (width // 2) - (width // 5) 
		topy = (width // 7) // 6
		rightx = ((width // 8)) + leftx
		botY = ((width // 7) // 4) + topy

		if mouseX < rightx and mouseX > leftx:
			if mouseY < botY and mouseY > topy:
				self.changeState = "MAIN"


		self.gameState.leftClick(width, height)

	def rightClick(self, width, height):
		self.gameState.rightClick(width, height)

	def make(self, width, height):
		self.changeState = "GAME"
		self.gameState.make(width, height)


class fairScreen:
	changeState = "GAME"
	def __init__(self, screen, width, height):
		self.screen = screen
		self.gray = (192,192,192)
		self.gray = (128,128,128)
		self.red = (255,0,0)
		self.numXPieces = 16
		self.numYPieces = 16
		self.bombNum = 40
		self.gameState = gameState(self.screen, self.numXPieces, self.numYPieces, width, height, self.bombNum)

	def load(self, width, height):
		self.draw(width, height)


	def draw(self, width, height):
		self.screen.fill(self.gray)
		self.gameState.draw(width, height)

	def getChangeState(self):
		return self.changeState

	def leftClick(self, width, height):
		mouseX, mouseY = pygame.mouse.get_pos()
		#test if go home/main
		leftx = (width // 2) - (width // 5) 
		topy = (width // 7) // 6
		rightx = ((width // 8)) + leftx
		botY = ((width // 7) // 4) + topy

		if mouseX < rightx and mouseX > leftx:
			if mouseY < botY and mouseY > topy:
				self.changeState = "MAIN"

		self.gameState.leftClick(width, height)

	def rightClick(self, width, height):
		self.gameState.rightClick(width, height)

	def make(self, width, height):
		self.changeState = "GAME"
		self.gameState.make(width, height)


class hardScreen:
	changeState = "GAME"
	def __init__(self, screen, width, height):
		self.screen = screen
		self.gray = (192,192,192)
		self.gray = (128,128,128)
		self.red = (255,0,0)
		self.numXPieces = 24
		self.numYPieces = 24
		self.bombNum = 99
		self.gameState = gameState(self.screen, self.numXPieces, self.numYPieces, width, height, self.bombNum)

	def load(self, width, height):
		self.draw(width, height)


	def draw(self, width, height):
		self.screen.fill(self.gray)
		self.gameState.draw(width, height)

	def getChangeState(self):
		return self.changeState

	def leftClick(self, width, height):
		mouseX, mouseY = pygame.mouse.get_pos()
		#test if go home/main
		leftx = (width // 2) - (width // 5) 
		topy = (width // 7) // 6
		rightx = ((width // 8)) + leftx
		botY = ((width // 7) // 4) + topy

		if mouseX < rightx and mouseX > leftx:
			if mouseY < botY and mouseY > topy:
				self.changeState = "MAIN"
				
		self.gameState.leftClick(width, height)

	def rightClick(self, width, height):
		self.gameState.rightClick(width, height)

	def make(self, width, height):
		self.changeState = "GAME"
		self.gameState.make(width, height)