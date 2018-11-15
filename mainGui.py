import pygame

class mainScreen:
    changeState = "START"
    def __init__(self, screen):
        self.screen = screen
        self.silver = (192,192,192)
        self.gray = (128,128,128)
        self.red = (255,0,0)
        self.buttonColorEZ = self.gray
        self.buttonColorFair = self.gray
        self.buttonColorHard = self.gray

        self.startTXT = "START"
        self.ezTXT = "EASY"
        self.fairTXT = "FAIR"
        self.hardTXT = "HARD"

    def load(self, width, height):
        self.rectWidth = (width // 3)
        self.rectHeight = (self.rectWidth // 4)

        self.isHoveringEZButton(width, height)
        self.isHoveringFairButton(width, height)
        self.isHoveringHardButton(width, height)
        self.draw(width, height)
        
    def draw(self, width, height):
        self.screen.fill(self.silver)

        widthPos = (width//15)
        self.myFont = pygame.font.SysFont('Comic Sans MS', widthPos)
        textsurface = self.myFont.render('Select A Difficulty', False, (0, 0, 0))

        widthPos = (width//2)-(textsurface.get_width()//2)
        self.screen.blit(textsurface,(widthPos,0))

        self.drawEZButton(width, height)
        self.drawFairButton(width, height)
        self.drawHardButton(width, height)
        

    def drawEZButton(self, width, height):
        widthPos = (width // 2) - (self.rectWidth // 2)
        heightPos = height // 4
        self.ezButton = pygame.draw.rect(self.screen, self.buttonColorEZ,(widthPos,heightPos,self.rectWidth,self.rectHeight))

        self.ezFont = pygame.font.SysFont('Arial', self.rectWidth//8)
        self.ezTxt = self.ezFont.render('Easy 8x8', True, (0,0,0)) 
       
        widthPos = ((width // 2) - (self.rectWidth // 2)) + ((self.rectWidth - self.ezTxt.get_width()) // 2)
        heightPos = (height // 4) + (self.rectHeight - self.ezTxt.get_height()) // 2
        self.screen.blit(self.ezTxt, (widthPos,heightPos,150,50))


    def isHoveringEZButton(self, width, height):
        mouseX, mouseY = pygame.mouse.get_pos()

        leftX = (width // 2) - (self.rectWidth // 2)
        rightX = leftX + self.rectWidth
        topY = height // 4
        botY = topY + self.rectHeight
        if(mouseX > leftX and mouseX < rightX and mouseY < botY and mouseY > topY):
            self.buttonColorEZ = self.red
            return True
        else:
            self.buttonColorEZ = self.gray
            return False

    def drawFairButton(self, width, height):
        widthPos = (width // 2) - (self.rectWidth // 2)
        heightPos = (height//4) * 2
        self.fairButton = pygame.draw.rect(self.screen, self.buttonColorFair,(widthPos,heightPos,self.rectWidth,self.rectHeight))

        self.fairFont = pygame.font.SysFont('Arial', self.rectWidth//8)
        self.fairTxt = self.fairFont.render('Fair 16x16', True, (0,0,0)) 
       
        widthPos = ((width // 2) - (self.rectWidth // 2)) + ((self.rectWidth - self.fairTxt.get_width()) // 2)
        heightPos = ((height // 4) * 2) + (self.rectHeight - self.fairTxt.get_height())//2
        self.screen.blit(self.fairTxt, (widthPos,heightPos,150,50))


    def isHoveringFairButton(self, width, height):
        mouseX, mouseY = pygame.mouse.get_pos()

        leftX = (width // 2) - (self.rectWidth // 2)
        rightX = leftX + self.rectWidth
        topY = (height // 4) * 2
        botY = topY + self.rectHeight
        if(mouseX > leftX and mouseX < rightX and mouseY < botY and mouseY > topY):
            self.buttonColorFair = self.red
            return True
        else:
            self.buttonColorFair = self.gray
            return False


    def drawHardButton(self, width, height):
        widthPos = (width // 2) - (self.rectWidth // 2)
        heightPos = (height // 4) * 3
        self.hardButton = pygame.draw.rect(self.screen, self.buttonColorHard,(widthPos,heightPos,self.rectWidth,self.rectHeight))

        self.hardFont = pygame.font.SysFont('Arial', self.rectWidth//8)
        self.hardTxt = self.hardFont.render('Hard 24x24', True, (0,0,0)) 
       
        widthPos = ((width // 2) - (self.rectWidth // 2)) + ((self.rectWidth - self.hardTxt.get_width()) // 2)
        heightPos = ((height // 4) * 3) + (self.rectHeight - self.hardTxt.get_height())//2
        self.screen.blit(self.hardTxt, (widthPos,heightPos,self.rectWidth,self.rectHeight))


    def isHoveringHardButton(self, width, height):
        mouseX, mouseY = pygame.mouse.get_pos()

        leftX = (width // 2) - (self.rectWidth // 2)
        rightX = leftX + self.rectWidth
        topY = (height // 4) * 3
        botY = topY + self.rectHeight
        if(mouseX > leftX and mouseX < rightX and mouseY < botY and mouseY > topY):
            self.buttonColorHard = self.red
            return True
        else:
            self.buttonColorHard = self.gray
            return False


    def click(self, width, height):
        if(self.isHoveringEZButton(width, height)):
            print('Easy Button Pressed')
            self.changeState = self.ezTXT
        elif(self.isHoveringFairButton(width, height)):
            print('Fair Button Pressed')
            self.changeState = self.fairTXT
        elif(self.isHoveringHardButton(width, height)):
            print('Hard Button Pressed')
            self.changeState = self.hardTXT

    def getChangeState(self):
        return self.changeState