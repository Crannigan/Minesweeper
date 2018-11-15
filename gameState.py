import pygame

class gameState:
	def __init__(self, screen, numXPieces, numYPieces):
		self.screen = screen
		self.gray = (128,128,128)
		self.yellow = (255,255,0)
		self.numXPieces = numXPieces
		self.numYPieces = numYPieces

	def draw(self, width, height):
		self.buildHeader(width, height)
		# Build board

	def buildHeader(self, width, height):
		self.rectWidth = width
		self.rectHeight = self.rectWidth//7
		self.headerRect = pygame.draw.rect(self.screen, self.gray,(0,0,self.rectWidth,self.rectHeight))

		# Draw Smiley Face
		widthPos = self.rectWidth // 2
		heightPos = self.rectHeight // 2
		circRad = (int(self.rectHeight * 0.8)) // 2
		self.smileyCircle = pygame.draw.circle(self.screen, self.yellow, (widthPos, heightPos), circRad, 0)

		# Write Counter for Bomb Flags

		# Write Timer