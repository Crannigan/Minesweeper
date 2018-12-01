import pygame
import random

from tile import *

class gameState:
	xRow = 0
	yRow = 0
	lost = False
	builtBombs = False
	mainIMG = "images/smile.png"
	def __init__(self, screen, numXPieces, numYPieces, width, height, bombNum):
		self.screen = screen
		self.gray = (128,128,128)
		self.yellow = (255,255,0)
		self.black = (0,0,0)
		self.numXPieces = numXPieces
		self.numYPieces = numYPieces
		self.bombNum = bombNum
		self.buildTiles(width, height)

	def draw(self, width, height):
		self.buildHeader(width, height)
		self.printTiles(width, height)


	def buildHeader(self, width, height):
		self.rectWidth = width
		self.rectHeight = self.rectWidth // 7
		self.headerRect = pygame.draw.rect(self.screen, self.gray,(0,0,self.rectWidth,self.rectHeight))

		# print Main Image
		self.img = pygame.image.load(self.mainIMG)
		self.img = pygame.transform.scale(self.img, (int(self.rectHeight * 0.8), int(self.rectHeight * 0.8)))
		rect = self.img.get_rect()
		rect = rect.move(((self.rectWidth // 2) - (int(self.rectHeight * 0.8) // 2), (self.rectHeight - int(self.rectHeight * 0.8)) // 2))
		self.screen.blit(self.img, rect)



	def buildTiles(self, width, height):
		self.xRow = list()
		for i in range(1, self.numXPieces + 1):
			yRow = list()
			for y in range(1, self.numYPieces + 1):
				tileWidth = width // self.numXPieces
				tileHeight = (height - (width // 7)) // self.numYPieces
				tileX = (i - 1) * tileWidth
				tileY = ((y - 1) * tileHeight) + (width // 7)
				thisTile = tile(tileX, tileY, tileWidth, tileHeight, self.screen)
				yRow.append(thisTile)

			self.xRow.append(yRow)



	def leftClick(self, width, height):
		mouseX, mouseY = pygame.mouse.get_pos()
		tileXNum = mouseX // (width // self.numXPieces)
		tileYNum = (mouseY - (width // 7)) // ((height - (width // 7)) // self.numYPieces)
		self.detBombCalcNear(width, height)
		if not(self.lost):
			if(self.xRow[tileXNum][tileYNum].getNumNearBombs() == 0):
				self.recClick(tileXNum, tileYNum)
			else:
				isBomb = self.xRow[tileXNum][tileYNum].clickedTile()
		
				if (isBomb):
					self.lostGame()	
			

	def rightClick(self, width, height):
		mouseX, mouseY = pygame.mouse.get_pos()
		tileXNum = mouseX // (width // self.numXPieces)
		tileYNum = (mouseY - (width // 7)) // ((height - (width // 7)) // self.numYPieces)

		self.detBombCalcNear(width, height)

		if not(self.lost):
			self.xRow[tileXNum][tileYNum].placeFlag()


	def detBombCalcNear(self, width, height):
		mouseX, mouseY = pygame.mouse.get_pos()
		tileXNum = mouseX // (width // self.numXPieces)
		tileYNum = (mouseY - (width // 7)) // ((height - (width // 7)) // self.numYPieces)
		
		if not(self.builtBombs):
			i = 0
			while(i < self.bombNum):
				tempRandX = random.randint(0, self.numXPieces - 1)
				tempRandY = random.randint(0,self.numXPieces - 1)
				if(tempRandX != tileXNum and tempRandY != tileYNum):
					checkBomb = self.xRow[tempRandX][tempRandY].addBomb()
					if (checkBomb):
						i = i + 1
			self.builtBombs = True
			self.calculateNearBombs()

		


	def recClick(self, x, y):
		if(x < 0 or (x+1) > self.numXPieces):
			return

		if(y < 0 or (y+1) > self.numYPieces):
			return

		if(self.xRow[x][y].isClicked()):
			return

		self.xRow[x][y].clickedTile()

		if(self.xRow[x][y].getNumNearBombs() == 0):
			self.recClick(x, y - 1)
			self.recClick(x - 1, y)
			self.recClick(x + 1, y)
			self.recClick(x, y + 1)



	def printTiles(self, width, height):
		for i in range(self.numXPieces):
			for y in range(self.numYPieces):
				tileWidth = width // self.numXPieces
				tileHeight = (height - (width // 7)) // self.numYPieces
				tileX = i * tileWidth
				tileY = (y * tileHeight) + (width // 7)
				tempTile = self.xRow[i][y].updateAndPrint(tileX, tileY, tileWidth, tileHeight)
				self.xRow[i][y] = tempTile


	def lostGame(self):
		self.lost = True

		# Draw Smiley Face
		self.mainIMG = 'images/blech.png'
		#show rest of bombs
		for i in range(self.numXPieces):
			for k in range(self.numYPieces):
				self.xRow[i][k].clickedBomb()



	def calculateNearBombs(self):
		for i in range(self.numXPieces):
			for k in range(self.numYPieces):
				total = 0
				#north-west diagonal
				if(self.correct(i - 1, k - 1)):
					if(self.xRow[i - 1][k - 1].isBomb()):
						total += 1

				#north
				if(self.correct(i, k - 1)):
					if(self.xRow[i][k - 1].isBomb()):
						total += 1

				#north-east diagonal
				if(self.correct(i + 1, k - 1)):
					if(self.xRow[i + 1][k - 1].isBomb()):
						total += 1

				#west 
				if(self.correct(i - 1, k)):
					if(self.xRow[i - 1][k].isBomb()):
						total += 1

				#center 
				if(self.correct(i, k)):
					if(self.xRow[i][k].isBomb()):
						total += 1

				#east 
				if(self.correct(i + 1, k)):
					if(self.xRow[i + 1][k].isBomb()):
						total += 1

				#south-west diagonal 
				if(self.correct(i - 1, k + 1)):
					if(self.xRow[i - 1][k + 1].isBomb()):
						total += 1

				#south 
				if(self.correct(i, k + 1)):
					if(self.xRow[i][k + 1].isBomb()):
						total += 1

				#south-east diagonal 
				if(self.correct(i + 1, k + 1)):
					if(self.xRow[i + 1][k + 1].isBomb()):
						total += 1


				self.xRow[i][k].setNearBombs(total)

	def correct(self, x_val, y_val):
		if(x_val < 0):
			return False
		elif(x_val > (self.numXPieces - 1)):
			return False

		if(y_val < 0):
			return False
		elif(y_val > (self.numYPieces - 1)):
			return False

		return True
