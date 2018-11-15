import pygame
from gameState import *

class easyScreen:
	changeState = "GAME"
	def __init__(self, screen):
		self.screen = screen
		self.silver = (192,192,192)
		self.gray = (128,128,128)
		self.red = (255,0,0)
		self.numXPieces = 8
		self.numYPieces = 8
		self.gameState = gameState(self.screen, self.numXPieces, self.numYPieces)

	def load(self, width, height):
		self.draw(width, height)


	def draw(self, width, height):
		self.screen.fill(self.silver)
		self.gameState.draw(width, height)

	def getChangeState(self):
		return self.changeState

	def click(self, width, height):
		print ("Click!")