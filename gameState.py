import pygame
import random

from tile import *

class gameState:
	xRow = 0
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
		self.flagsAvailable = self.bombNum

	def make(self, width, height):
		self.buildTiles(width, height)

	def draw(self, width, height):
		self.buildHeader(width, height)
		self.printTiles(width, height)
		self.printFlagCount(width, height)


	def printFlagCount(self, width, height):
		self.flagCounterTextTop = pygame.font.SysFont('Comic Sans MS', (width // 7) // 4)
		textsurfaceTop = self.flagCounterTextTop.render('Flag', False, (0, 0, 0))
		
		self.flagCounterTextBot = pygame.font.SysFont('Comic Sans MS', (width // 7) // 4)
		textsurfaceBot = self.flagCounterTextBot.render('Counter', False, (0, 0, 0))

		offset = ((width // 7) - (textsurfaceTop.get_height() + textsurfaceBot.get_height())) // 2
		self.screen.blit(textsurfaceTop,(0,offset))
		self.screen.blit(textsurfaceBot,(0,offset + textsurfaceTop.get_height()))

		rectSide = (width // 7) * 0.8
		rectX = textsurfaceBot.get_width() + 15
		rextY = ((width // 7) - rectSide) // 2

		self.flagCounterBG = pygame.draw.rect(self.screen, self.black, (rectX,rextY,rectSide,rectSide))

		self.countText = pygame.font.SysFont('Comic Sans MS', (width // 7) // 2)
		flagCounterTXT = self.countText.render(str(self.flagsAvailable), False, (255,255,255))
		self.screen.blit(flagCounterTXT, (rectX + ((rectSide - flagCounterTXT.get_width()) // 2),rextY))



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
		offset = (width - ((width // self.numXPieces) * self.numXPieces)) // 2

		self.xRow = list()
		for i in range(1, self.numXPieces + 1):
			yRow = list()
			for y in range(1, self.numYPieces + 1):
				tileWidth = width // self.numXPieces
				tileHeight = (height - (width // 7)) // self.numYPieces
				tileX = ((i - 1) * tileWidth) + offset
				tileY = ((y - 1) * tileHeight) + (width // 7)
				thisTile = tile(tileX, tileY, tileWidth, tileHeight, self.screen)
				yRow.append(thisTile)

			self.xRow.append(yRow)



	def leftClick(self, width, height):
		mouseX, mouseY = pygame.mouse.get_pos()

		#test if reset
		leftx = ((self.rectWidth // 2) - (int(self.rectHeight * 0.8) // 2))
		rightx = leftx + self.img.get_width()
		topy = (self.rectHeight - int(self.rectHeight * 0.8)) // 2
		boty = topy + self.img.get_height()
		if(mouseX > leftx and mouseX < rightx):
			if(mouseY > topy and mouseY < boty):
				self.mainIMG = "images/smile.png"
				self.lost = False
				self.builtBombs = False
				self.buildTiles(width, height)
				self.flagsAvailable = self.bombNum


		tileXNum = mouseX // (width // self.numXPieces)
		tileYNum = (mouseY - (width // 7)) // ((height - (width // 7)) // self.numYPieces)


		if tileXNum >= self.numXPieces:
			return
		elif tileYNum < 0 or tileYNum >= self.numYPieces:
			return

		self.detBombCalcNear(width, height)
		if not(self.lost):
			if(self.xRow[tileXNum][tileYNum].getNumNearBombs() == 0):
				self.recClick(tileXNum, tileYNum)
			else:
				isBomb = self.xRow[tileXNum][tileYNum].bust()
				if (isBomb):
					self.lostGame()

		if self.didWin():
			self.mainIMG = "images/cool.png"

			

	def rightClick(self, width, height):
		mouseX, mouseY = pygame.mouse.get_pos()
		tileXNum = mouseX // (width // self.numXPieces)
		tileYNum = (mouseY - (width // 7)) // ((height - (width // 7)) // self.numYPieces)

		if tileXNum >= self.numXPieces:
			return
		elif tileYNum < 0 or tileYNum >= self.numYPieces:
			return

		self.detBombCalcNear(width, height)

		if not(self.lost):
			placedFlag = self.xRow[tileXNum][tileYNum].placeFlag()
			if placedFlag and self.flagsAvailable != 0:
				self.flagsAvailable -= 1
			elif not placedFlag:
				self.flagsAvailable += 1


		if self.didWin():
			self.mainIMG = "images/cool.png"


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
		tilesWidth = (width // self.numXPieces) * self.numXPieces
		tilesHeight = ((height - (width // 7)) // self.numYPieces) * self.numYPieces
		tilesBGx = (width - (tilesWidth + 6)) // 2
		tilesBGy = (width // 7) - 3
		tilesWidth = tilesWidth + tilesBGx + (6 - tilesBGx)
		tilesHeight = tilesHeight + (6 - tilesBGy) + tilesBGy
		tileBG = pygame.draw.rect(self.screen, self.black,(tilesBGx,tilesBGy,tilesWidth,tilesHeight))

		offset = (width - ((width // self.numXPieces) * self.numXPieces)) // 2

		for i in range(self.numXPieces):
			for y in range(self.numYPieces):
				tileWidth = width // self.numXPieces
				tileHeight = (height - (width // 7)) // self.numYPieces
				tileX = (i * tileWidth) + offset
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


	def didWin(self):
		for i in range(self.numXPieces):
			for k in range(self.numYPieces):
				if not self.xRow[i][k].guessRight():
					return False


		return True