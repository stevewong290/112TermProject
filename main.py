from cmu_112_graphics import *
from tkinter import *
from TwoAI import * 
import random, math, copy, string, time

#I got the cmu 112 graphics from the class notes 
#https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html

verbose = True
fill = '#D5EFB5'
winner = None
############################  Class Setup  #####################################  

#I got the structure of the code from the modal app from class
#https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html

class Player(object):
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
        self.numRailroads = 0
        self.inJail = False
        self.jailCounter = 0
        self.colorBuild = set()
        self.critMoney = 0
        self.lastTransaction = '$0'
        self.utilDouble = False

    def numRail(self):
        counter = 0
        for property in self.properties:
            if isinstance(property, Railroad):
                counter += 1
        self.numRailroads = counter
    
    def doubleRent(self):
        #brown properties
        if mediterranean in self.properties and baltic in self.properties:
            self.colorBuild.add('brown')
            mediterranean.double = True
            baltic.double = True
        else:
            mediterranean.double = False
            baltic.double = False
        #grey properties
        if (oriental in self.properties and vermont in self.properties and 
              connecticut in self.properties):
            self.colorBuild.add('grey')
            oriental.double = True
            vermont.double = True
            connecticut.double = True
        else:
            oriental.double = False
            vermont.double = False
            connecticut.double = False
        #pink properties
        if (stCharles in self.properties and state in self.properties and 
            virginia in self.properties):
            self.colorBuild.add('pink')
            stCharles.double = True
            state.double = True
            virginia.double = True
        else:
            stCharles.double = False
            state.double = False
            virginia.double = False
        #orange properties
        if (stJames in self.properties and tennessee in self.properties and 
            newYork in self.properties):
            self.colorBuild.add('orange')
            stJames.double = True
            tennessee.double = True
            newYork.double = True
        else:
            stJames.double = False
            tennessee.double = False
            newYork.double = False
        #red properties
        if (kentucky in self.properties and indiana in self.properties and 
            illinois in self.properties):
            self.colorBuild.add('red')
            kentucky.double = True
            indiana.double = True
            illinois.double = True
        else:
            kentucky.double = False
            indiana.double = False
            illinois.double = False
        #yellow properties
        if (atlantic in self.properties and vetnor in self.properties and 
            marvin in self.properties):
            self.colorBuild.add('yellow')
            atlantic.double = True
            vetnor.double = True
            marvin.double = True
        else:
            atlantic.double = False
            vetnor.double = False
            marvin.double = False
        #green properties
        if (pacific in self.properties and northCarolina in self.properties and 
            pennsylvania in self.properties):
            self.colorBuild.add('green')
            pacific.double = True
            northCarolina.double = True
            pennsylvania.double = True
        else:
            pacific.double = False
            northCarolina.double = False
            pennsylvania.double = False
        #blue properties
        if (parkPlace in self.properties and boardwalk in self.properties):
            self.colorBuild.add('blue')
            parkPlace.double = True
            boardwalk.double = True
        else:
            parkPlace.double = False
            boardwalk.double = False
        #utilities
        if (electric in self.properties and water in self.properties):
            electric.double = True
            water.double = True
            self.utilDouble = True
        else:
            electric.double = False
            water.double = False
            self.utilDouble = False
    def propertySort(self):
        for i in range(len(self.properties)):
            minPosition = i
            for j in range(i+1, len(self.properties)):
                if self.properties[minPosition].rank > self.properties[j].rank:
                    minPosition = j
            #swap
            temp = self.properties[i]
            self.properties[i] = self.properties[minPosition]
            self.properties[minPosition] = temp
            
            
            
class Property(object):
    def __init__(self, name, cost, rent, h1, h2, h3, h4, hotel, houseCost, color, setRank, rank):
        self.name = name
        self.cost = cost
        self.rent = rent
        self.h1 = h1
        self.h2 = h2
        self.h3 = h3
        self.h4 = h4
        self.hotel = hotel
        self.houseCost = houseCost
        self.double = False
        self.numHouse = 0
        self.selected = False
        self.color = color
        self.setRank = setRank
        self.rank = rank
        
    def __str__(self):
        return self.name
        
    def __repr__(self):
        return self.name
        
        
class Railroad(object):
    def __init__(self, name, rank):
        self.name = name
        self.cost = 200
        self.r1 = 25
        self.r2 = 50
        self.r3 = 100
        self.r4 = 200
        self.rank = rank
        
class CommunityChance(object):
    def __init__(self, name):
        self.name = name

class CommunityChanceCardMoney(CommunityChance):
    def __init__(self, name, action, message):
        super().__init__(name)
        self.action = action
        self.message = message
        
class CommunityChanceCardMovement(CommunityChance):
    def __init__(self, name, action, message):
        super().__init__(name)
        self.action = action
        self.message = message
        

        

class CornerSpace(object):
    def __init__(self, name):
        self.name = name

class Tax(object):
    def __init__(self, name, tax):
        self.name = name
        self.tax = tax
        
class Utilities(object):
    def __init__(self, name, cost, rank):
        self.name = name
        self.cost = cost
        self.double = False
        self.rank = rank

############################  Board Setup  #####################################     

######################## Community Chest and Chance Cards ######################

communityChance1 = CommunityChanceCardMoney('1', 50, 'CMU overcharged you, collect $50 refund')
communityChance2 = CommunityChanceCardMoney('2', -15, 'Purchased a meal at ABP, pay $15')
communityChance3 = CommunityChanceCardMoney('3', 100, 'You won Hack112, collect $100')
communityChance4 = CommunityChanceCardMoney('4', -200, 'Cheated on 112 HW, pay $200')
communityChance5 = CommunityChanceCardMoney('5', 150, 'Won the lottery, collect $150')
communityChance6 = CommunityChanceCardMoney('6', -250, 'Tuition is due, pay $250')

communityChance7 = CommunityChanceCardMovement('7', -3, 'Move back 3 spaces')
communityChance8 = CommunityChanceCardMovement('8', 0, 'Advance to the nearest Railroad')
communityChance9 = CommunityChanceCardMovement('9', 0, 'Advance to the nearest Utility')
communityChance10 = CommunityChanceCardMovement('10', 0, 'Advance to the Illinois Ave')
communityChance11 = CommunityChanceCardMovement('11', 0, 'Advance to the Boardwalk')
communityChance12 = CommunityChanceCardMovement('12', 0, 'Advance to the St. Charles')

communityChanceList = []
communityChanceList.append(communityChance1)
communityChanceList.append(communityChance2)
communityChanceList.append(communityChance3)
communityChanceList.append(communityChance4)
communityChanceList.append(communityChance5)
communityChanceList.append(communityChance6)
communityChanceList.append(communityChance7)
communityChanceList.append(communityChance8)
communityChanceList.append(communityChance9)
communityChanceList.append(communityChance10)
communityChanceList.append(communityChance11)
communityChanceList.append(communityChance12)

random.shuffle(communityChanceList)

print(communityChanceList[0])



#################################  Spaces  #####################################
#instantiated properties        
mediterranean = Property('Mediterranean Ave', 60, 2, 10, 30, 90, 160, 250, 50, 'brown',1, 1)
baltic = Property('Baltic Ave', 60, 4, 20, 60, 180, 320, 450, 50, 'brown', 2, 2)
oriental = Property('Oriental Ave', 100, 6, 30, 90, 270, 400, 550, 50, 'grey', 1, 3)
vermont = Property('Vermont Ave', 100, 6, 30, 90, 270, 400, 550, 50, 'grey', 2, 4)
connecticut = Property('Connecticut Ave', 120, 8, 40, 100, 300, 450, 600, 50, 'grey', 3, 5)
stCharles = Property('St. Charles Place', 140, 10, 50, 150, 450, 625, 750, 100, 'pink', 1, 6)
state = Property('State Ave', 140, 10, 50, 150, 450, 625, 750, 100, 'pink', 2, 7)
virginia = Property('Virginia Ave', 160, 12, 60, 180, 500, 700, 900, 100, 'pink', 3, 8)
stJames = Property('St. James Place', 180, 14, 70, 200, 550, 750, 950, 100, 'orange', 1, 9)
tennessee = Property('Tennessee Ave', 180, 14, 70, 200, 550, 750, 950, 100, 'orange', 2, 10)
newYork = Property('New York Ave', 200, 16, 80, 220, 600, 800, 1000, 100, 'orange', 3, 11)
kentucky = Property('Kentucky Ave', 220, 18, 90, 250, 700, 875, 1050, 150, 'red', 1, 12)
indiana = Property('Indiana Ave', 220, 18, 90, 250, 700, 875, 1050, 150, 'red', 2, 13)
illinois = Property('Illinois Ave', 240, 20, 100, 300, 750, 925, 1100, 150, 'red', 3, 14)
atlantic = Property('Atlantic Ave', 260, 22, 110, 330, 800, 975, 1150, 150, 'yellow', 1, 15)
vetnor = Property('Vetnor Ave', 260, 22, 110, 330, 800, 975, 1150, 150, 'yellow', 2, 16)
marvin = Property('Marvin Gardens', 280, 24, 120, 360, 850, 1025, 1200, 150, 'yellow', 3,17)
pacific = Property('Pacific Ave', 300, 26, 130, 390, 900, 1100, 1275, 200, 'green', 1, 18)
northCarolina = Property('N. Carolina Ave', 300, 26, 130, 390, 900, 1100, 1275, 200, 'green', 2, 19)
pennsylvania = Property('Penn Ave', 320, 28, 150, 450, 1000, 1200, 1400, 200, 'green', 3, 20)
parkPlace = Property('Park Place',350, 35, 175, 500, 1100, 1300, 1500, 200, 'blue', 1, 21)
boardwalk = Property('Boardwalk', 400, 50, 200, 600, 1400, 1700, 2000, 200, 'blue', 2, 22)

#instantiated railroads
readingRail = Railroad('Reading R.R.', 23)
pennsylvaniaRail = Railroad('Pennsylvania R.R.', 24)
boRail= Railroad('B & O R.R.', 25)
shortRail = Railroad('Short Line R.R.', 26)

#instantiated utilities
electric = Utilities('Electric Company', 150, 27)
water = Utilities('Water Works', 150, 28)

#instantiated corner spaces
passGo = CornerSpace('Pass Go')
jailCell = CornerSpace('Jail Cell')
freeParking = CornerSpace('Free Parking')
goToJail = CornerSpace('Go To Jail')

#instantiated community chest / chance spaces
communitySide1 = CommunityChance('Community Chest Side 1')
communitySide2 = CommunityChance('Community Chest Side 2')
communitySide4 = CommunityChance('Community Chest Side 4')
chanceSide1 = CommunityChance('Chance Side 1')
chanceSide3 = CommunityChance('Chance Side 3')
chanceSide4 = CommunityChance('Chance Side 4')

#instantiated tax space
incomeTax = Tax('Income Tax', 200)
luxuryTax = Tax('Luxury Tax', 100)

############################  Board ############################################

#putting each space into a list
board = []

#side1
board.append(passGo)
board.append(mediterranean)
board.append(communitySide1)
board.append(baltic)
board.append(incomeTax)
board.append(readingRail)
board.append(oriental)
board.append(chanceSide1)
board.append(vermont)
board.append(connecticut)
board.append(jailCell)

#side2
board.append(stCharles)
board.append(electric)
board.append(state)
board.append(virginia)
board.append(pennsylvaniaRail)
board.append(stJames)
board.append(communitySide2)
board.append(tennessee)
board.append(newYork)
board.append(freeParking)

#side3
board.append(kentucky)
board.append(chanceSide3)
board.append(indiana)
board.append(illinois)
board.append(boRail)
board.append(atlantic)
board.append(vetnor)
board.append(water)
board.append(marvin)
board.append(goToJail)

#side4
board.append(pacific)
board.append(northCarolina)
board.append(communitySide4)
board.append(pennsylvania)
board.append(shortRail)
board.append(chanceSide4)
board.append(parkPlace)
board.append(luxuryTax)
board.append(boardwalk)


#property set
propertySet = set(board)

#this removes the nonproperties from the set 
for element in board:
    if (isinstance(element, Tax) or isinstance(element, CornerSpace) or
        isinstance(element, CommunityChance)):
        propertySet.remove(element)
        
###########################  Houses ############################################
        
#brown houses
mediterraneanHouse = []
for house in range(4):
    mediterraneanHouse.append((791 + 12 * house, 595))

    
balticHouse = []    
for house in range(4):
    balticHouse.append((686 + 12 * house, 595))
 
#grey houses
orientalHouse = []
for house in range(4):
    orientalHouse.append((529.5 + 12 * house, 595))
    
vermontHouse = []
for house in range(4):
    vermontHouse.append((424.5 + 12 * house, 595))
    
connecticutHouse = []
for house in range(4):
    connecticutHouse.append((372 + 12 * house, 595))

#pink houses     
stCharlesHouse = []
for house in range(4):
    stCharlesHouse.append((352, 542 + 12 * house))
    
stateHouse = []
for house in range(4):
    stateHouse.append((352, 437 + 12 * house))
    
virginiaHouse = []
for house in range(4):
    virginiaHouse.append((352, 384.5 + 12 * house))

#orange houses    
stJamesHouse = []
for house in range(4):
    stJamesHouse.append((352, 279.5 + 12 * house))
    
tennesseeHouse = []
for house in range(4):
    tennesseeHouse.append((352, 174.5 + 12 * house))
    
newYorkHouse = []
for house in range(4):
    newYorkHouse.append((352, 122 + 12 * house))
 
 #red houses   
kentuckyHouse = []
for house in range(4):
    kentuckyHouse.append((408 - 12 * house, 102))
    
indianaHouse = []
for house in range(4):
    indianaHouse.append((513 - 12 * house, 102))
    
illinoisHouse = []
for house in range(4):
    illinoisHouse.append((565.5 - 12 * house, 102))

#yellow houses    
atlanticHouse = []
for house in range(4):
    atlanticHouse.append((670.5 - 12 * house, 102))
    
vetnorHouse = []
for house in range(4):
    vetnorHouse.append((723 - 12 * house, 102))
    
marvinHouse = []
for house in range(4):
    marvinHouse.append((828 - 12 * house, 102))
 
#green houses   
pacificHouse = []
for house in range(4):
    pacificHouse.append((845, 157 - 12 * house))
    
northCarolinaHouse = []
for house in range(4):
    northCarolinaHouse.append((845, 209.5 - 12 * house))
    
pennsylvaniaHouse = []
for house in range(4):
    pennsylvaniaHouse.append((845, 314.5 - 12 * house))

#blue houses    
parkPlaceHouse = []
for house in range(4):
    parkPlaceHouse.append((845, 472 - 12 * house))
    
boardwalkHouse = []
for house in range(4):
    boardwalkHouse.append((845, 577 - 12 * house))

        
housePosition = []
housePosition.append(None)
housePosition.append(mediterraneanHouse)
housePosition.append(None)
housePosition.append(balticHouse)
housePosition.append(None)
housePosition.append(None)
housePosition.append(orientalHouse)
housePosition.append(None)
housePosition.append(vermontHouse)
housePosition.append(connecticutHouse)
housePosition.append(None)
housePosition.append(stCharlesHouse)
housePosition.append(None)
housePosition.append(stateHouse)
housePosition.append(virginiaHouse)
housePosition.append(None)
housePosition.append(stJamesHouse)
housePosition.append(None)
housePosition.append(tennesseeHouse)
housePosition.append(newYorkHouse)
housePosition.append(None)
housePosition.append(kentuckyHouse)
housePosition.append(None)
housePosition.append(indianaHouse)
housePosition.append(illinoisHouse)
housePosition.append(None)
housePosition.append(atlanticHouse)
housePosition.append(vetnorHouse)
housePosition.append(None)
housePosition.append(marvinHouse)
housePosition.append(None)
housePosition.append(pacificHouse)
housePosition.append(northCarolinaHouse)
housePosition.append(None)
housePosition.append(pennsylvaniaHouse)
housePosition.append(None)
housePosition.append(None)
housePosition.append(parkPlaceHouse)
housePosition.append(None)
housePosition.append(boardwalkHouse)

houses = dict()
houses['brown'] = (0,0)
houses['grey'] = (0,0,0)
houses['pink'] = (0,0,0)
houses['orange'] = (0,0,0)
houses['red'] = (0,0,0)
houses['yellow'] = (0,0,0)
houses['green'] = (0,0,0)
houses['blue'] = (0,0)

########################  Splash Screen Setup  #################################  

class SplashScreenMode(Mode):
    def appStarted(mode):
        mode.counter = 0
        #this is for the background
        background = 'splash2.png'
        mode.background = mode.loadImage(background)
        mode.background = mode.scaleImage(mode.background, .5)
        mode.timerDelay = 1
        
    def timerFired(mode):
        mode.counter += 1
        
    def redrawAll(mode, canvas):
        font = 'Arial 60 bold'
        font1 = 'Arial 24 bold'
        canvas.create_rectangle(0,0,mode.width, mode.height, fill = '#D5EFB5')
        canvas.create_image(600, 250, image = ImageTk.PhotoImage(mode.background))
        canvas.create_rectangle(mode.width / 2 - 166, 382, mode.width / 2 + 166, 418, 
                                fill = 'white', outline = 'red', width = 2)
        canvas.create_rectangle(mode.width / 2 - 236, 482, mode.width / 2 + 236, 518, 
                                fill = 'white', outline = 'red', width = 2)
        canvas.create_rectangle(mode.width / 2 - 186, 582, mode.width / 2 + 186, 618, 
                                fill = 'white', outline = 'red', width = 2)
        if (mode.counter // 8) % 2 == 0:
            canvas.create_text(mode.width/2, 400, text="Press  'a'  for the AI Mode!", 
                               fill = 'red', font=font1)
            canvas.create_text(mode.width/2, 500, text="Press 'space' for the Two Player Mode!", 
                               fill = 'red', font=font1)
            canvas.create_text(mode.width/2, 600, text="Press 'h' for the Instructions!", 
                               fill = 'red', font=font1)

    def keyPressed(mode, event):
        if (event.key == 'h'):
            mode.app.setActiveMode(mode.app.helpMode)
        elif (event.key == 'a'):
            mode.app.setActiveMode(mode.app.AIMode)
        elif event.key == 'Space':
            mode.app.setActiveMode(mode.app.gameMode)
        elif event.key == 'd':
            mode.app.setActiveMode(mode.app.AIAIMode)
            
##########################  Game Mode Setup  ###################################  

class GameMode(Mode):
    def appStarted(mode):
        mode.player1 = Player('Player 1')
        mode.player2 = Player('Player 2')
        
        '''
        #showing that buying houses works
        mode.player1.colorBuild.add('grey')
        mode.player1.properties.append(oriental)
        mode.player1.properties.append(vermont)
        mode.player1.properties.append(connecticut)
        
        mode.player2.colorBuild.add('green')
        mode.player2.properties.append(pacific)
        mode.player2.properties.append(northCarolina)
        mode.player2.properties.append(pennsylvania)
        
        mode.player2.colorBuild.add('yellow')
        mode.player2.properties.append(atlantic)
        mode.player2.properties.append(vetnor)
        mode.player2.properties.append(marvin)
        
        mode.player2.colorBuild.add('orange')
        mode.player2.properties.append(stJames)
        mode.player2.properties.append(tennessee)
        mode.player2.properties.append(newYork)
        
        propertySet.remove(oriental)
        propertySet.remove(vermont)
        propertySet.remove(connecticut)
        propertySet.remove(pacific)
        propertySet.remove(northCarolina)
        propertySet.remove(atlantic)
        propertySet.remove(vetnor)
        propertySet.remove(marvin)
        propertySet.remove(stJames)
        propertySet.remove(tennessee)
        propertySet.remove(newYork)
        propertySet.remove(pennsylvania)
        '''
        
        
        mode.dice = (1,1)
        
        #roll tracking in order to help calculate the rent for utilities
        mode.prevRoll = 0
        
        #roll counter used to make sure the gameplay goes as it is supposed to
        mode.rollCounter = 0
        
        #turn counter
        #if divisible by 2 then it is player 1's turn
        mode.turnCounter = 0
        
        #this is the monopoly logo we are uploading
        logo = ('monopolyLogo.jpg')
        mode.logo = mode.loadImage(logo)
        mode.logo = mode.scaleImage(mode.logo, 0.06)
        
        #this is the board image that we are uploading
        board = ('board.jpg')
        mode.board = mode.loadImage(board)
        
        #this is the buy button that we are uploading
        buyButton = ('buyProperty.png')
        mode.buy = mode.loadImage(buyButton)
        
        #this is the end turn button
        turnButton = ('endTurn.png')
        mode.turn = mode.loadImage(turnButton)
        
        #this is the roll dice button
        rollDice = ('rollDice.png')
        mode.roll = mode.loadImage(rollDice)
        
        #this is the buy house button
        buyHouse = ('buyHouse.png')
        mode.buyHouseButton = mode.loadImage(buyHouse)
        
        #these are the die
        mode.diceOne = mode.loadImage('dice1.png')
        mode.diceOne = mode.scaleImage(mode.diceOne,.3)
        mode.diceTwo = mode.loadImage('dice2.png')
        mode.diceTwo = mode.scaleImage(mode.diceTwo,.3)
        mode.diceThree = mode.loadImage('dice3.png')
        mode.diceThree = mode.scaleImage(mode.diceThree,.3)
        mode.diceFour = mode.loadImage('dice4.png')
        mode.diceFour = mode.scaleImage(mode.diceFour,.3)
        mode.diceFive = mode.loadImage('dice5.png')
        mode.diceFive = mode.scaleImage(mode.diceFive,.3)
        mode.diceSix = mode.loadImage('dice6.png')
        mode.diceSix = mode.scaleImage(mode.diceSix,.3)
        
        
        
        #this is announcementsa
        mode.announcements = []
        
        '''
        #these are the pictures of the dices
        dice1 = 
        mode.dice1 = 
        '''
        
        #THESE ARE THE POSSIBLE LOCATIONS OF PLAYER 1 (outer)
        mode.player1Locations = []
            
        #pass go, this is where we start appending
        mode.player1Locations.append((901.5,651.5))
        
        #go to bottom locations
        for i in range(9):
            mode.player1Locations.append((808.5 - 52.5 * i, 651.5))
            
        #jail
        mode.player1Locations.append((298.5,651.5))
        
        #go to left locations
        for i in range(9):
            mode.player1Locations.append((298.5,561.25 - 52.5 * i))
            
        #free parking
        mode.player1Locations.append((298.5,48.5))
        
        #top locations
        for i in range(9):
            mode.player1Locations.append((388.5 + 52.5 * i, 48.5))
        
        #go to jail location
        mode.player1Locations.append((901.5,48.5))
        
        #right locations
        for i in range(9):
            mode.player1Locations.append((901.5,141.25 + 52.5 * i))
        
        #THESE ARE THE POSSIBLE LOCATIONS OF player2
        mode.player2Locations = []
        
        #pass go, this is where we start appending
        mode.player2Locations.append((876.5,626.5))
        
        #go to bottom locations
        for i in range(9):
            mode.player2Locations.append((808.5 - 52.5 * i, 626.5))
            
        #jail
        mode.player2Locations.append((323.5,626.5))
        
        #go to left locations
        for i in range(9):
            mode.player2Locations.append((323.5,561.25 - 52.5 * i))
            
        #free parking
        mode.player2Locations.append((323.5,73.5))
        
        #top locations
        for i in range(9):
            mode.player2Locations.append((388.5 + 52.5 * i, 73.5))
        
        #go to jail location
        mode.player2Locations.append((876.5, 73.5))
        
        #right locations
        for i in range(9):
            mode.player2Locations.append((876.5,141.25 + 52.5 * i))
        
    def diceRoll(mode):
        x = random.randint(1,6)
        y = random.randint(1,6)
        return (x,y)
        
    def communityChance(mode):
        x = random.randint()

#################################  Buying  #####################################  
        
    def buyProperty(mode):
        #player 1 turn
        if mode.turnCounter % 2 == 0:
            space = board[mode.player1.position % 40]
            if space in propertySet: 
                if mode.player1.money >= space.cost:
                    mode.player1.money -= space.cost
                    mode.player1.properties.append(space)
                    propertySet.remove(space)
                    if len(mode.announcements) == 5:
                        mode.announcements = mode.announcements[1:]
                        mode.announcements.append(f'Player 1 bought {space.name}')
                    elif len(mode.announcements) < 5:
                        mode.announcements.append(f'Player 1 bought {space.name}')
        #player 2 turn
        else:
            space = board[mode.player2.position % 40]
            if space in propertySet: 
                if mode.player2.money >= space.cost:
                    mode.player2.money -= space.cost
                    mode.player2.properties.append(space)
                    propertySet.remove(space)
                    if len(mode.announcements) == 5:
                        mode.announcements = mode.announcements[1:]
                        mode.announcements.append(f'Player 2 bought {space.name}')
                    elif len(mode.announcements) < 5:
                        mode.announcements.append(f'Player 2 bought {space.name}')
        mode.player1.doubleRent()
        mode.player1.propertySort()
        mode.player2.doubleRent()
        mode.player2.propertySort()
        
    def buyHouseConstraint(mode, property):
        #player 1 turn
        if mode.turnCounter % 2 == 0:
            #print(property.color)
            #print(mode.player1.colorBuild)
            if (property.color in mode.player1.colorBuild):
                if property.color == 'brown' or property.color == 'blue':
                    a, b = houses[property.color]
                    if property.numHouse == min(a,b):
                        return True
                    else:
                        return False
                else:
                    a, b, c = houses[property.color]
                    if property.numHouse == min(a,b,c):
                        return True
                    else:
                        return False
            return False
        else:
            if (property.color in mode.player2.colorBuild):
                if property.color == 'brown' or property.color == 'blue':
                    a, b = houses[property.color]
                    if property.numHouse == min(a,b):
                        return True
                    else:
                        return False
                else:
                    a, b, c = houses[property.color]
                    if property.numHouse == min(a,b,c):
                        return True
                    else:
                        return False
            return False
            
    def buyHouse(mode, property):
        if mode.buyHouseConstraint(property):
            if property.numHouse <= 4:
                property.numHouse += 1
                if property.color == 'brown' or property.color == 'blue':
                    a,b = houses[property.color]
                    if property.setRank == 1:
                        houses[property.color] = (a+1,b)
                    else:
                        houses[property.color] = (a, b+1)
                    if property in mode.player1.properties:
                        mode.player1.money -= property.houseCost
                    else:
                        mode.player2.money -= property.houseCost
                else:
                    a,b,c = houses[property.color]
                    if property.setRank == 1:
                        houses[property.color] = (a+1,b,c)
                    elif property.setRank == 2:
                        houses[property.color] = (a,b+1,c)
                    else:
                        houses[property.color] = (a,b,c+1)
                    if property in mode.player1.properties:
                        mode.player1.money -= property.houseCost
                    else:
                        mode.player2.money -= property.houseCost
                if len(mode.announcements) < 5:
                    if mode.turnCounter % 2 == 0:
                        mode.announcements.append('Player 1 bought a house')
                    else:
                        mode.announcements.append('Player 2 bought a house')
                elif len(mode.announcements) == 5:
                    mode.announcements = mode.announcements[1:]
                    if mode.turnCounter % 2 == 0:
                        mode.announcements.append('Player 1 bought a house')
                    else:
                        mode.announcements.append('Player 2 bought a house')
                    
            #print(houses['grey'])

            
                    
#########################  Rent Price Calculator  ##############################  

    #this function takes in a property and returns how much to pay
    def rentPriceProperty(mode, property):
        if property.numHouse == 0:
            print(property.double)
            if property.double:
                return property.rent * 2
            else:
                return property.rent
        elif property.numHouse == 1:
            return property.h1
        elif property.numHouse == 2:
            return property.h2
        elif property.numHouse == 3:
            return property.h3
        elif property.numHouse == 4:
            return property.h4
        elif property.numHouse == 5:
            return property.hotel

    #this function takes in a utility and returns how much to pay
    def rentPriceUtility(mode, utility):
        if utility.double:
            return mode.prevRoll * 10
        else:
            return mode.prevRoll * 4
    
    #this function takes in a railroad and returns how much to pay
    def rentPriceRailroad(mode, railroad):
        if mode.turnCounter % 2 == 1:
            mode.player1.numRail()
            if mode.player1.numRailroads == 1:
                return railroad.r1
            elif mode.player1.numRailroads == 2:
                return railroad.r2
            elif mode.player1.numRailroads == 3:
                return railroad.r3
            elif mode.player1.numRailroads == 4:
                return railroad.r4
        else:
            mode.player2.numRail()
            if mode.player2.numRailroads == 1:
                return railroad.r1
            elif mode.player2.numRailroads == 2:
                return railroad.r2
            elif mode.player2.numRailroads == 3:
                return railroad.r3
            elif mode.player2.numRailroads == 4:
                return railroad.r4
                
###############################  Movement  #####################################  

    #this implements moving the player and tracking whether or not it 
    #passed or landed on go
    def didRollAndPassGo(mode, dice, doubleBool):
        if mode.turnCounter % 2 == 0:
            if mode.moveForwardJail(doubleBool):
                prev = mode.player1.position // 40
                mode.player1.position += (dice)
                mode.landOnJail()
                newPos = mode.player1.position // 40
                if mode.player1.position % 40 == 0:
                    mode.player1.money += 400
                elif prev != newPos:
                    mode.player1.money += 200
        else:
            if mode.moveForwardJail(doubleBool):
                prev = mode.player2.position // 40
                mode.player2.position += (dice)
                mode.landOnJail()
                newPos = mode.player2.position // 40
                if mode.player2.position % 40 == 0:
                    mode.player2.money += 400
                elif prev != newPos:
                    mode.player2.money += 200
                
    #This is a function that returns a bool on whether or not the player can move
    def moveForwardJail(mode, doubleBool):
        if mode.turnCounter % 2 == 0:
            if mode.player1.jailCounter == 3:
                mode.player1.inJail = False
                mode.player1.money -= 50
                return True
            elif not doubleBool and mode.player1.inJail:
                mode.player1.jailCounter += 1
                return False
            elif doubleBool and mode.player1.inJail:
                mode.player1.inJail = False
                mode.player1.jailCounter = 0
                return True
        else:
            if mode.player2.jailCounter == 3:
                mode.player2.money -= 50
                return True
            elif not doubleBool and mode.player2.inJail:
                mode.player2.jailCounter += 1
                return False
            elif doubleBool and mode.player2.inJail:
                mode.player2.inJail = False
                mode.player2.jailCounter = 0
                return True
        return True
        
    def landOnJail(mode):
        if mode.turnCounter % 2 == 0:
            if mode.player1.position % 40 == 30:
                mode.player1.position -= 20
                mode.player1.inJail = True
        else:
            if mode.player2.position % 40 == 30:
                mode.player2.position -= 20
                mode.player2.inJail = True
            
                
    def landOpponentOrTax(mode):
        if mode.turnCounter % 2 == 0:
            #redefine location as space
            space = board[mode.player1.position % 40]
            if space in mode.player2.properties:
                if isinstance(space, Property):
                    rent = mode.rentPriceProperty(space)
                    mode.player1.money -= rent
                    mode.player2.money += rent
                elif isinstance(space, Utilities):
                    rent = mode.rentPriceUtility(space)
                    mode.player1.money -= rent
                    mode.player2.money += rent
                elif isinstance(space, Railroad):
                    rent = mode.rentPriceRailroad(space)
                    mode.player1.money -= rent
                    mode.player2.money += rent
            elif isinstance(space, Tax):
                mode.player1.money -= space.tax
            if len(mode.announcements) == 5:
                mode.announcements = mode.announcements[1:]
                if isinstance(space, CommunityChance):
                    if (space.name == 'Community Chest Side 1' or space.name == 'Community Chest Side 2' or 
                        space.name == 'Community Chest Side 4'):
                        mode.announcements.append(f'Player 1 landed on Community Chest')
                    else:
                        mode.announcements.append('Player 1 landed on Chance')
                else:
                    mode.announcements.append(f'Player 1 landed on {space.name}')
            elif len(mode.announcements) < 5:
                mode.announcements.append(f'Player 1 landed on {space.name}')
        else:
            #redefine location as space
            space = board[mode.player2.position % 40]
            #if where you landed is owned by the opponent, pay rent
            if space in mode.player1.properties:
                if isinstance(space, Property):
                    rent = mode.rentPriceProperty(space)
                    mode.player2.money -= rent
                    mode.player1.money += rent
                elif isinstance(space, Utilities):
                    rent = mode.rentPriceUtility(space)
                    mode.player2.money -= rent
                    mode.player1.money += rent
                elif isinstance(space, Railroad):
                    rent = mode.rentPriceRailroad(space)
                    mode.player2.money -= rent
                    mode.player1.money += rent
            elif isinstance(space, Tax):
                mode.player2.money -= space.tax
            if len(mode.announcements) == 5:
                mode.announcements = mode.announcements[1:]
                if isinstance(space, CommunityChance):
                    if (space.name == 'Community Chest Side 1' or space.name == 'Community Chest Side 2' or 
                        space.name == 'Community Chest Side 4'):
                        mode.announcements.append(f'Player 2 landed on Community Chest')
                    else:
                        mode.announcements.append('Player 2 landed on Chance')
                else:
                    mode.announcements.append(f'Player 2 landed on {space.name}')
            elif len(mode.announcements) < 5:
                mode.announcements.append(f'Player 2 landed on {space.name}')
   
    def rollDice(mode):
        if mode.rollCounter == 0:
            mode.rollCounter += 1
            dice1, dice2 = mode.diceRoll()
            if len(mode.announcements) == 5:
                mode.announcements = mode.announcements[1:]
                if mode.turnCounter % 2 == 0:
                    mode.announcements.append('Player 1 rolled the dice')
                else:
                    mode.announcements.append('Player 2 rolled the dice')
            elif len(mode.announcements) < 5:
                if mode.turnCounter % 2 == 0:
                    mode.announcements.append('Player 1 rolled the dice')
                else:
                    mode.announcements.append('Player 2 rolled the dice')
            double = False
            if dice1 == dice2:
                double == True
            #stores the previous dice in the app
            mode.prevRoll = dice1 + dice2
            mode.dice = (dice1, dice2)
            diceTotal = dice1 + dice2
            mode.actionsAfterRoll(diceTotal, double)
            
    def actionsAfterRoll(mode, diceTotal, double):
        mode.didRollAndPassGo(diceTotal, double)
        mode.landOpponentOrTax()
        mode.player1.doubleRent()
        mode.player1.propertySort()
        mode.player2.doubleRent()
        mode.player2.propertySort()
        mode.checkEndGame()
     
    '''
    def endTurn(mode):
        if mode.rollCounter == 1:
            mode.turnCounter += 1
            mode.rollCounter = 0
        mode.player1.doubleRent()
        mode.player2.doubleRent()
    '''
        
    def checkEndGame(mode):
        global winner
        if mode.player1.money < 0:
            winner = mode.player2
            mode.app.setActiveMode(mode.app.gameOverMode)
        elif mode.player2.money < 0:
            winner = mode.player1
            mode.app.setActiveMode(mode.app.gameOverMode)
                    
    def endTurn(mode):
        if mode.rollCounter == 1:
            mode.turnCounter += 1
            mode.rollCounter = 0
            if len(mode.announcements) == 5:
                mode.announcements = mode.announcements[1:]
                if mode.turnCounter % 2 == 1:
                    mode.announcements.append('Player 1 ended their turn')
                else:
                    mode.announcements.append('Player 2 ended their turn')
            elif len(mode.announcements) < 5:
                if mode.turnCounter % 2 == 1:
                    mode.announcements.append('Player 1 ended their turn')
                else:
                    mode.announcements.append('Player 2 ended their turn')
            mode.player1.doubleRent()
            mode.player1.propertySort()
            mode.player2.doubleRent()
            mode.player2.propertySort()
            mode.checkEndGame()
        
############################  Select Spaces  ###################################  

    def propertySelection(mode, x, y):
        for space in board:
            if isinstance(space,Property):
                space.selected = False
                
        #selection from side 1
        if (x >= 810 - 26.25 and x <= 810 + 26.25 and 
            y >= 628 - 42.5 and y <= 628 + 42.5):
            mediterranean.selected = True
        elif (x >= 705 - 26.25 and x <= 705 + 26.25 and 
            y >= 628 - 42.5 and y <= 628 + 42.5):
            baltic.selected = True
        elif (x >= 547.5 - 26.25 and x <= 547.5 + 26.25 and 
            y >= 628 - 42.5 and y <= 628 + 42.5):
            oriental.selected = True
        elif (x >= 442.5 - 26.25 and x <= 442.5 + 26.25 and 
            y >= 628 - 42.5 and y <= 628 + 42.5):
            vermont.selected = True
        elif (x >= 390 - 26.25 and x <= 390 + 26.25 and 
            y >= 628 - 42.5 and y <= 628 + 42.5):
            connecticut.selected = True
        
        #selection from side 2
        elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
            y >= 560 - 26.25 and y <= 560 + 26.25):
            stCharles.selected = True
        elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
            y >= 455 - 26.25 and y <= 455 + 26.25):
            state.selected = True
        elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
            y >= 402.5 - 26.25 and y <= 402.5 + 26.25):
            virginia.selected = True
        elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
            y >= 297.5 - 26.25 and y <= 297.5 + 26.25):
            stJames.selected = True
        elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
            y >= 192.5 - 26.25 and y <= 192.5 + 26.25):
            tennessee.selected = True
        elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
            y >= 140 - 26.25 and y <= 140 + 26.25):
            newYork.selected = True
       
        #selection from side 3
        elif (x >= 390 - 26.25 and x <= 390 + 26.25 and 
            y >= 70 - 42.5 and y <= 70 + 42.5):
            kentucky.selected = True
        elif (x >= 495 - 26.25 and x <= 495 + 26.25 and 
            y >= 70 - 42.5 and y <= 70 + 42.5):
            indiana.selected = True
        elif (x >= 547.5 - 26.25 and x <= 547.5 + 26.25 and 
            y >= 70 - 42.5 and y <= 70 + 42.5):
            illinois.selected = True
        elif (x >= 652.5 - 26.25 and x <= 652.5 + 26.25 and 
            y >= 70 - 42.5 and y <= 70 + 42.5):
            atlantic.selected = True
        elif (x >= 705 - 26.25 and x <= 705 + 26.25 and 
            y >= 70 - 42.5 and y <= 70 + 42.5):
            vetnor.selected = True
        elif (x >= 810 - 26.25 and x <= 810 + 26.25 and 
            y >= 70 - 42.5 and y <= 70 + 42.5):
            marvin.selected = True
        
        #selection from side 4
        elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
            y >= 140 - 26.25 and y <= 140 + 26.25):
            pacific.selected = True
        elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
            y >= 192.5 - 26.25 and y <= 192.5 + 26.25):
            northCarolina.selected = True
        elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
            y >= 297.5 - 26.25 and y <= 297.5 + 26.25):
            pennsylvania.selected = True
        elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
            y >= 455 - 26.25 and y <= 455 + 26.25):
            parkPlace.selected = True
        elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
            y >= 560 - 26.25 and y <= 560 + 26.25):
            boardwalk.selected = True
        

###############################  User Input  ################################### 

    def mousePressed(mode, event):
        #pressed buy property button
        if (event.x >= 140 - 85 and event.x <= 140 + 85 and 
            event.y >= 490 and event.y <= 530):
            mode.buyProperty()
            print('you pressed the buy property button')
            
        #pressed roll dice button
        if (event.x >= 205 - 63 and event.x <= 205 + 63 and 
            event.y >= 420 and event.y <= 460):
            print('you pressed the roll dice button')
            mode.rollDice()
            
        #pressed end turn button
        if (event.x >= 140-64 and event.x <= 140 + 64 and 
            event.y >= 630 and event.y <= 670):
            mode.endTurn()
            print('you pressed the end turn button')
            
        #pressed buy house button
        if (event.x >= 140-72 and event.x <= 140+72 and 
            event.y >= 560 and event.y <= 600):
            selected = None
            for space in board:
                if isinstance(space, Property):
                    if space.selected:
                        selected = space
            if selected != None:
                mode.buyHouse(selected)
            print('you pressed the buyHouse button')
            
        #property selection
        mode.propertySelection(event.x, event.y)
        for space in board:
            if isinstance(space, Property):
                if space.selected == True:
                    print(f'{space.name} is selected') 
            

    def keyPressed(mode, event):
        if event.key == 'h':
            mode.app.setActiveMode(mode.app.helpMode)
        
    def timerFired(mode):
        pass
        
############################  Draw Functions  ################################## 
        
    def drawPlayer1Path(mode,canvas,x,y):
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill = 'blue')
        
    def drawPlayer2Path(mode,canvas,x,y):
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill = 'green')
        
    def drawPlayer1(mode, canvas, player1):
        position = player1.position % 40
        (x, y) = mode.player1Locations[position]
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill = 'blue')
        
    def drawPlayer2(mode, canvas, player2):
        position = player2.position % 40
        (x, y) = mode.player2Locations[position]
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill = 'green')
        
    def drawPlayer1Values(mode, canvas, player1):
        canvas.create_rectangle(930,10,1190, 345)
        canvas.create_rectangle(940, 20, 1180, 60, fill = fill)
        canvas.create_text(1060,40,text = (f'Player 1'), font = 'Arial, 18')
        canvas.create_text(1060, 80, text = (f'Money: ${player1.money}'))
        canvas.create_text(950,100,text = 'Properties:', anchor = 'w')
        canvas.create_text(1076,100, text = 'Houses:', anchor = 'w')
        counter = 0
        r = 4
        for element in player1.properties:
            canvas.create_text(950, 130 + (18 * counter), text = element.name, anchor = 'w')
            if isinstance(element, Property):
                for circleCounter in range(5):
                    if circleCounter == element.numHouse - 1 and circleCounter == 4:
                        canvas.create_oval(1080-r + (20 * circleCounter),130 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 130 + r + (18 * counter),
                                        fill = 'red')
                    elif circleCounter <= element.numHouse - 1:
                        canvas.create_oval(1080-r + (20 * circleCounter),130 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 130 + r + (18 * counter),
                                        fill = 'green')
                    else:
                        canvas.create_oval(1080-r + (20 * circleCounter),130 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 130 + r + (18 * counter))
            counter += 1
        
    def drawPlayer2Values(mode, canvas, player2):
        canvas.create_rectangle(930, 355, 1190, 690)
        canvas.create_rectangle(940, 365, 1180, 405, fill = fill)
        canvas.create_text(1060,385,text = (f'Player 2'), font = 'Arial, 18')
        canvas.create_text(1060, 425, text = (f'Money: ${player2.money}'))
        canvas.create_text(950,445,text = 'Properties:', anchor = 'w')
        canvas.create_text(1076,445, text = 'Houses:', anchor = 'w')
        counter = 0
        r = 4
        for element in player2.properties:
            canvas.create_text(950, 475 + (18 * counter), text = element.name, anchor = 'w')
            if isinstance(element, Property):
                for circleCounter in range(5):
                    if circleCounter == element.numHouse - 1 and circleCounter == 4:
                        canvas.create_oval(1080-r + (20 * circleCounter),475 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 475 + r + (18 * counter),
                                        fill = 'red')
                    elif circleCounter <= element.numHouse - 1:
                        canvas.create_oval(1080-r + (20 * circleCounter),475 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 475 + r + (18 * counter),
                                        fill = 'green')
                    else:
                        canvas.create_oval(1080-r + (20 * circleCounter),475 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 475 + r + (18 * counter))
            counter += 1
        '''
        canvas.create_text(1075,200,text = (
                           f'computer money:{mode.computer.money}'))
        canvas.create_text(1075,220,text = 'properties')
        counter = 0
        for element in computer.properties:
            canvas.create_text(940, 240 + (20 * counter), text = element.name, anchor = 'w')
            counter += 1
        a'''   
    def drawCommunityChance(mode, canvas):
        pass
        
    

                
        
    
     
    def drawDice(mode, canvas):
        (dice1, dice2) = mode.dice
        canvas.create_rectangle(20, 410, 125, 470, fill = fill)
        #canvas.create_text(45, 400, text = 'Dice:', font = 'Arial, 22')
        if dice1 == 1:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceOne))
        elif dice1 == 2:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceTwo))
        elif dice1 == 3:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceThree))
        elif dice1 == 4:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceFour))
        elif dice1 == 5:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceFive))
        elif dice1 == 6:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceSix))
        if dice2 == 1:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceOne))
        elif dice2 == 2:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceTwo))
        elif dice2 == 3:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceThree))
        elif dice2 == 4:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceFour))
        elif dice2 == 5:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceFive))
        elif dice2 == 6:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceSix))
        
        
        
        
    def drawTurn(mode, canvas):
        canvas.create_rectangle(50, 140, 230, 180, fill = fill)
        canvas.create_text(90, 160, text = 'Turn:', font = 'Arial 22')
        if mode.turnCounter % 2 == 0:
            canvas.create_text(180, 160, text = 'Player 1', font = 'Arial 20')
        else:
            canvas.create_text(180, 160, text = 'Player 2', font = 'Arial 20')
        
        
    def drawHouse(mode, canvas):
        spaceIndex = 0
        for property in housePosition:
            if property != None:
                counter = 0
                if board[spaceIndex].numHouse == 5:
                    space = board[spaceIndex]
                    x, y = property[1]
                    if space.color == 'brown' or space.color == 'grey':
                        canvas.create_rectangle(x - 4.5, y - 4.5, x + 16.5, 
                                                y + 4.5, fill = 'red')
                    elif space.color == 'pink' or space.color == 'orange':
                        canvas.create_rectangle(x - 4.5, y - 4.5, x + 4.5, 
                                                y + 16.5, fill = 'red')
                    elif space.color == 'red' or space.color == 'yellow':
                        canvas.create_rectangle(x - 16.5, y - 4.5, x + 4.5, 
                                                y + 4.5, fill = 'red')
                    elif space.color == 'green' or space.color == 'blue':
                        canvas.create_rectangle(x - 4.5, y - 16.5, x + 4.5, 
                                                y + 4.5, fill = 'red')
                else:
                    for houseCoor in property:
                        if counter < board[spaceIndex].numHouse and counter < 4:
                            x, y = houseCoor
                            canvas.create_rectangle(x-4.5,y-4.5,x+4.5,y+4.5,fill = 'green')
                        counter += 1
                
                    
            spaceIndex += 1
            
    def drawPropArea(mode, canvas):
        for pair in coorSide1:
            x,y = pair
            canvas.create_rectangle(x - 26.25, y - (42.5), 
                                    x + 26.25, y + (42.5), fill = 'red')
                                    
        for pair in coorSide2:
            x,y = pair
            canvas.create_rectangle(x-42.5, y-26.25, x+42.5, y+26.25, fill = 'red')
        
        for pair in coorSide3:
            x,y = pair
            canvas.create_rectangle(x - 26.25, y - (42.5), 
                                    x + 26.25, y + (42.5), fill = 'red')
        
        for pair in coorSide4:
            x,y = pair
            canvas.create_rectangle(x-42.5, y-26.25, x+42.5, y+26.25, fill = 'red')
            
    def drawAnnouncements(mode, canvas):
        counter = 0
        canvas.create_rectangle(10, 210, 270, 380, fill = fill)
        canvas.create_text(140, 230, text = 'Announcements:', font = 'Arial, 20')
        for message in mode.announcements:
            canvas.create_text(140, 260 + 25 * counter, text = message, font = 'Arial 16')
            counter += 1
        
    

    def redrawAll(mode, canvas):
        #draw turn
        mode.drawTurn(canvas)
        
        #draw logo
        canvas.create_image(140, 65, image = ImageTk.PhotoImage(mode.logo))
        
        #draw board
        canvas.create_image(mode.width / 2,mode.height / 2,
                            image=ImageTk.PhotoImage(mode.board))
                            
        #draw buy property button 
        canvas.create_image(140, 510, image =
                            ImageTk.PhotoImage(mode.buy))
                            
        #draw end turn button
        canvas.create_image(140, 650, image = 
                            ImageTk.PhotoImage(mode.turn))
                            
        #draw roll dice button
        canvas.create_image(205, 440, image = 
                            ImageTk.PhotoImage(mode.roll))
                            
        #draw buy house button
        canvas.create_image(140, 580, image = 
                            ImageTk.PhotoImage(mode.buyHouseButton))
        
        #draw players
        mode.drawPlayer1(canvas, mode.player1)
        mode.drawPlayer2(canvas, mode.player2)
        
        #draw players values
        mode.drawPlayer1Values(canvas, mode.player1)
        mode.drawPlayer2Values(canvas, mode.player2)
        
        #finding coordinates for houses
        
        mode.drawHouse(canvas)
        #mode.drawPropArea(canvas)
        
        #canvas.create_text(mode.width / 2, mode.height / 2, text = 'THIS IS THE AI MODE', 
        #                   font = 'Arial 50 bold')
        mode.drawAnnouncements(canvas)
        
        mode.drawDice(canvas)
        
        #print(mode.secondDepthSumExpectedValue())
        #print(mode.sumExpectedValue(baltic))
        
        
        '''
        #help find player location on the board
        for location in mode.player1Locations:
            (xcor, ycor) = location
            mode.drawPlayer1Path(canvas,xcor,ycor)
            
        for location in mode.computerLocations:
            h(xcor, ycor) = location
            mode.drawcomputerPath(canvas,xcor,ycor)
        '''
################################################################################
################################################################################
############################## AI Mode Setup ###################################
################################################################################
################################################################################


class AIMode(Mode):
    def appStarted(mode):
        mode.player1 = Player('Player 1')
        mode.computer = Player('Computer AI')
        mode.turnCompletedPlayer1 = True
        mode.turnCompletedComputer = True
        mode.oldPositionPlayer1 = 0
        mode.tempPositionPlayer1 = 0
        mode.oldPositionComputer = 0
        mode.tempPositionComputer = 0
        mode.counterDrawPlayer1 = 0
        mode.counterDrawComputer = 0
        mode.nextSelected = False
        mode.selectionCounter = 0
        mode.communityChanceMessage = ''
        mode.animationSkip = False
        mode.secondDepthMax = 0
        
        
        '''
        for space in mode.player1.properties:
            print(f'{space.name}: {space.double}')
        '''
        
        '''
        mode.computer.colorBuild.add('green')
        mode.computer.properties.append(pacific)
        mode.computer.properties.append(northCarolina)
        mode.computer.properties.append(pennsylvania)
        
        mode.computer.colorBuild.add('yellow')
        mode.computer.properties.append(atlantic)
        mode.computer.properties.append(vetnor)
        mode.computer.properties.append(marvin)
        
        mode.computer.colorBuild.add('orange')
        mode.computer.properties.append(stJames)
        mode.computer.properties.append(tennessee)
        mode.computer.properties.append(newYork)
        '''
        
        
        '''
        propertySet.remove(pacific)
        propertySet.remove(northCarolina)
        propertySet.remove(pennsylvania)
        
        propertySet.remove(atlantic)
        propertySet.remove(vetnor)
        propertySet.remove(marvin)
        '''
        
        
        
        
        
        
        mode.dice = (1,1)
        
        #roll tracking in order to help calculate the rent for utilities
        mode.prevRoll = 0
        
        #roll counter used to make sure the gameplay goes as it is supposed to
        mode.rollCounter = 0
        
        #turn counter
        #if divisible by 2 then it is player 1's turn
        mode.turnCounter = 0
        
        #this is the monopoly logo we are uploading
        logo = ('monopolyLogo.jpg')
        mode.logo = mode.loadImage(logo)
        mode.logo = mode.scaleImage(mode.logo, 0.06)
        
        #this is the board image that we are uploading
        board = ('board.jpg')
        mode.board = mode.loadImage(board)
        
        #this is the buy button that we are uploading
        buyButton = ('buyProperty.png')
        mode.buy = mode.loadImage(buyButton)
        
        #this is the end turn button
        turnButton = ('endTurn.png')
        mode.turn = mode.loadImage(turnButton)
        
        #this is the roll dice button
        rollDice = ('rollDice.png')
        mode.roll = mode.loadImage(rollDice)
        
        #this is the buy house button
        buyHouse = ('buyHouse.png')
        mode.buyHouseButton = mode.loadImage(buyHouse)
        
        #these are the die
        mode.diceOne = mode.loadImage('dice1.png')
        mode.diceOne = mode.scaleImage(mode.diceOne,.3)
        mode.diceTwo = mode.loadImage('dice2.png')
        mode.diceTwo = mode.scaleImage(mode.diceTwo,.3)
        mode.diceThree = mode.loadImage('dice3.png')
        mode.diceThree = mode.scaleImage(mode.diceThree,.3)
        mode.diceFour = mode.loadImage('dice4.png')
        mode.diceFour = mode.scaleImage(mode.diceFour,.3)
        mode.diceFive = mode.loadImage('dice5.png')
        mode.diceFive = mode.scaleImage(mode.diceFive,.3)
        mode.diceSix = mode.loadImage('dice6.png')
        mode.diceSix = mode.scaleImage(mode.diceSix,.3)
        
        
        
        #this is announcementsa
        mode.announcements = []
        
        '''
        #these are the pictures of the dices
        dice1 = 
        mode.dice1 = 
        '''
        
        #THESE ARE THE POSSIBLE LOCATIONS OF PLAYER 1 (outer)
        mode.player1Locations = []
            
        #pass go, this is where we start appending
        mode.player1Locations.append((901.5,651.5))
        
        #go to bottom locations
        for i in range(9):
            mode.player1Locations.append((808.5 - 52.5 * i, 651.5))
            
        #jail
        mode.player1Locations.append((298.5,651.5))
        
        #go to left locations
        for i in range(9):
            mode.player1Locations.append((298.5,561.25 - 52.5 * i))
            
        #free parking
        mode.player1Locations.append((298.5,48.5))
        
        #top locations
        for i in range(9):
            mode.player1Locations.append((388.5 + 52.5 * i, 48.5))
        
        #go to jail location
        mode.player1Locations.append((901.5,48.5))
        
        #right locations
        for i in range(9):
            mode.player1Locations.append((901.5,141.25 + 52.5 * i))
        
        #THESE ARE THE POSSIBLE LOCATIONS OF COMPUTER
        mode.computerLocations = []
        
        #pass go, this is where we start appending
        mode.computerLocations.append((876.5,626.5))
        
        #go to bottom locations
        for i in range(9):
            mode.computerLocations.append((808.5 - 52.5 * i, 626.5))
            
        #jail
        mode.computerLocations.append((323.5,626.5))
        
        #go to left locations
        for i in range(9):
            mode.computerLocations.append((323.5,561.25 - 52.5 * i))
            
        #free parking
        mode.computerLocations.append((323.5,73.5))
        
        #top locations
        for i in range(9):
            mode.computerLocations.append((388.5 + 52.5 * i, 73.5))
        
        #go to jail location
        mode.computerLocations.append((876.5, 73.5))
        
        #right locations
        for i in range(9):
            mode.computerLocations.append((876.5,141.25 + 52.5 * i))
            
        mode.communityChance = []
        
        
    def diceRoll(mode):
        x = random.randint(1,6)
        y = random.randint(1,6)
        return (x,y)
        
        

#################################  AI Buying  ##################################
        
    def buyProperty(mode):
        #player 1 turn
        if mode.turnCounter % 2 == 0:
            space = board[mode.player1.position % 40]
            if space in propertySet: 
                if mode.player1.money >= space.cost:
                    mode.player1.money -= space.cost
                    mode.player1.lastTransaction = f'-${space.cost}'
                    mode.player1.properties.append(space)
                    propertySet.remove(space)
                    if len(mode.announcements) == 5:
                        mode.announcements = mode.announcements[1:]
                        mode.announcements.append(f'Player 1 bought {space.name}')
                    elif len(mode.announcements) < 5:
                        mode.announcements.append(f'Player 1 bought {space.name}')
        #computer turn
        else:
            space = board[mode.computer.position % 40]
            if space in propertySet: 
                if mode.computer.money >= space.cost:
                    mode.computer.money -= space.cost
                    mode.computer.lastTransaction = f'-${space.cost}'
                    mode.computer.properties.append(space)
                    propertySet.remove(space)
                    if len(mode.announcements) == 5:
                        mode.announcements = mode.announcements[1:]
                        mode.announcements.append(f'Computer bought {space.name}')
                    elif len(mode.announcements) < 5:
                        mode.announcements.append(f'Computer bought {space.name}')
        mode.player1.doubleRent()
        mode.player1.propertySort()
        mode.computer.doubleRent()
        mode.computer.propertySort()
        
    def buyHouseConstraint(mode, property):
        #player 1 turn
        if mode.turnCounter % 2 == 0:
            #print(property.color)
            #print(mode.player1.colorBuild)
            if (property.color in mode.player1.colorBuild and mode.player1.money >= property.houseCost):
                if property.color == 'brown' or property.color == 'blue':
                    a, b = houses[property.color]
                    if property.numHouse == min(a,b):
                        return True
                    else:
                        return False
                else:
                    a, b, c = houses[property.color]
                    if property.numHouse == min(a,b,c):
                        return True
                    else:
                        return False
            return False
        else:
            if (property.color in mode.computer.colorBuild and mode.computer.money >= property.houseCost):
                if property.color == 'brown' or property.color == 'blue':
                    a, b = houses[property.color]
                    if property.numHouse == min(a,b):
                        return True
                    else:
                        return False
                else:
                    a, b, c = houses[property.color]
                    if property.numHouse == min(a,b,c):
                        return True
                    else:
                        return False
            return False
            
    def buyHouse(mode, property):
        if mode.buyHouseConstraint(property):
            if property.numHouse <= 4:
                property.numHouse += 1
                if property.color == 'brown' or property.color == 'blue':
                    a,b = houses[property.color]
                    if property.setRank == 1:
                        houses[property.color] = (a+1,b)
                    else:
                        houses[property.color] = (a, b+1)
                    if property in mode.player1.properties:
                        mode.player1.money -= property.houseCost
                        mode.player1.lastTransaction = f'-${property.houseCost}'
                    else:
                        mode.computer.money -= property.houseCost
                        mode.computer.lastTransaction = f'-${property.houseCost}'
                else:
                    a,b,c = houses[property.color]
                    if property.setRank == 1:
                        houses[property.color] = (a+1,b,c)
                    elif property.setRank == 2:
                        houses[property.color] = (a,b+1,c)
                    else:
                        houses[property.color] = (a,b,c+1)
                    if property in mode.player1.properties:
                        mode.player1.money -= property.houseCost
                        mode.player1.lastTransaction = f'-${property.houseCost}'
                    else:
                        mode.computer.money -= property.houseCost
                        mode.computer.lastTransaction = f'-${property.houseCost}'
                if len(mode.announcements) < 5:
                    if mode.turnCounter % 2 == 0:
                        mode.announcements.append('Player 1 bought a house')
                    else:
                        mode.announcements.append('Computer bought a house')
                elif len(mode.announcements) == 5:
                    mode.announcements = mode.announcements[1:]
                    if mode.turnCounter % 2 == 0:
                        mode.announcements.append('Player 1 bought a house')
                    else:
                        mode.announcements.append('Computer bought a house')
                        
            #print(houses['grey'])

            
                    
#########################  Rent Price Calculator  ##############################  

    #this function takes in a property and returns how much to pay
    def rentPriceProperty(mode, property, player):
        mode.player1.doubleRent()
        mode.computer.doubleRent()
        '''
        for i in range(len(mode.player1.properties)):
            print(f'{mode.player1.properties[i].name}: {mode.player1.properties[i].double}')
            if givenProp == mode.player1.properties[i]:
                property = mode.player1.properties[i]
                print(f'{property.name}: {property.double}')
        '''
        if property.numHouse == 0:
            if property.color in player.colorBuild:
                return (property.rent * 2)
            else:
                return property.rent
        elif property.numHouse == 1:
            return property.h1
        elif property.numHouse == 2:
            return property.h2
        elif property.numHouse == 3:
            return property.h3
        elif property.numHouse == 4:
            return property.h4
        elif property.numHouse == 5:
            return property.hotel

    #this function takes in a utility and returns how much to pay
    def rentPriceUtility(mode, utility, player):
        mode.player1.doubleRent()
        mode.computer.doubleRent()
        if player.utilDouble: 
            return mode.prevRoll * 10
        else:
            return mode.prevRoll * 4
    
    #this function takes in a railroad and returns how much to pay
    def rentPriceRailroad(mode, railroad):
        if mode.turnCounter % 2 == 1:
            mode.player1.numRail()
            if mode.player1.numRailroads == 1:
                return railroad.r1
            elif mode.player1.numRailroads == 2:
                return railroad.r2
            elif mode.player1.numRailroads == 3:
                return railroad.r3
            elif mode.player1.numRailroads == 4:
                return railroad.r4
        else:
            mode.computer.numRail()
            if mode.computer.numRailroads == 1:
                return railroad.r1
            elif mode.computer.numRailroads == 2:
                return railroad.r2
            elif mode.computer.numRailroads == 3:
                return railroad.r3
            elif mode.computer.numRailroads == 4:
                return railroad.r4
                
###############################  AI Movement  ##################################

    #this implements moving the player and tracking whether or not it 
    #passed or landed on go
    def didRollAndPassGo(mode, dice, doubleBool):
        if mode.turnCounter % 2 == 0:
            mode.turnCompletedPlayer1 = False
            if mode.moveForwardJail(doubleBool):
                prev = mode.player1.position // 40
                mode.oldPositionPlayer1 = mode.player1.position % 40
                mode.tempPositionPlayer1 = mode.oldPositionPlayer1
                mode.player1.position += (dice)
                mode.landOnJail()
                if mode.animationSkip:
                    mode.tempPositionPlayer1 += dice
                newPos = mode.player1.position // 40
                if mode.player1.position % 40 == 0:
                    mode.player1.money += 400
                    mode.player1.lastTransaction = f'+$400'
                elif prev != newPos:
                    mode.player1.money += 200
                    mode.player1.lastTransaction = f'+$200'
        else:
            mode.turnCompletedComputer = False
            if mode.moveForwardJail(doubleBool):
                prev = mode.computer.position // 40
                mode.oldPositionComputer = mode.computer.position % 40
                mode.tempPositionComputer = mode.oldPositionComputer
                mode.computer.position += (dice)
                mode.landOnJail()
                if mode.animationSkip:
                    mode.tempPositionComputer += dice
                newPos = mode.computer.position // 40
                if mode.computer.position % 40 == 0:
                    mode.computer.money += 400
                    mode.computer.lastTransaction = f'+$400'
                elif prev != newPos:
                    mode.computer.money += 200
                    mode.computer.lastTransaction = f'+$200'
                
    #This is a function that returns a bool on whether or not the player can move
    def moveForwardJail(mode, doubleBool):
        if mode.turnCounter % 2 == 0:
            if mode.player1.jailCounter == 3:
                mode.player1.inJail = False
                mode.player1.money -= 50
                mode.player1.lastTransaction = f'-$50'
                return True
            elif not doubleBool and mode.player1.inJail:
                mode.player1.jailCounter += 1
                return False
            elif doubleBool and mode.player1.inJail:
                mode.player1.inJail = False
                mode.player1.jailCounter = 0
                return True
        else:
            if mode.computer.jailCounter == 3:
                mode.computer.money -= 50
                mode.computer.lastTransaction = f'-$50'
                return True
            elif not doubleBool and mode.computer.inJail:
                mode.computer.jailCounter += 1
                return False
            elif doubleBool and mode.computer.inJail:
                mode.computer.inJail = False
                mode.computer.jailCounter = 0
                return True
        return True
        
    def landOnJail(mode):
        
        if mode.turnCounter % 2 == 0:
            if mode.player1.position % 40 == 30:
                mode.player1.position -= 20
                mode.player1.inJail = True
                mode.animationSkip = True
        else:
            if mode.computer.position % 40 == 30:
                mode.computer.position -= 20
                mode.computer.inJail = True
                mode.animationSkip = True
                
    def reshuffleCommunityChance(mode):
        #add back all the cards
        communityChanceList.append(communityChance1)
        communityChanceList.append(communityChance2)
        communityChanceList.append(communityChance3)
        communityChanceList.append(communityChance4)
        communityChanceList.append(communityChance5)
        communityChanceList.append(communityChance6)
        communityChanceList.append(communityChance7)
        communityChanceList.append(communityChance8)
        communityChanceList.append(communityChance9)
        communityChanceList.append(communityChance10)
        communityChanceList.append(communityChance11)
        communityChanceList.append(communityChance12)
        #shuffle the cards
        random.shuffle(communityChanceList)
        
    def nearestRailroad(mode, player):
        curPos = player.position % 40
        if curPos > 5 and curPos < 15:
            player.position = 15
        elif curPos > 15 and curPos < 25:
            player.position = 25
        elif curPos > 25 and curPos < 35:
            player.position = 35
        elif curPos < 5 or curPos > 35:
            player.position = 5
            
    def nearestUtility(mode, player):
        curPos = player.position % 40
        if curPos > 12 and curPos < 28:
            player.position = 28
        else:
            player.position = 12
        
    def moveAction(mode, communityChanceCard, player):
        #move back 3 spaces
        if communityChanceCard.name == '7':
            player.position -= 3
            mode.communityChanceMessage = 'Move back 3 spaces'
        #Advance to the nearest Railroad
        elif communityChanceCard.name == '8':
            mode.communityChanceMessage = 'Advance to the nearest Railroad'
            mode.nearestRailroad(player)
        #Advance to the nearest Utility
        elif communityChanceCard.name == '9':
            mode.communityChanceMessage = 'Advance to the nearest Utility'
            mode.nearestUtility(player)
        #Advance to the Illinois Ave
        elif communityChanceCard.name == '10':
            if player.position % 40 > 24:
                player.money += 200
            player.position = 24
            mode.communityChanceMessage = 'Advance to the Illinois Ave'
        #Advance to the Boardwalk
        elif communityChanceCard.name == '11':
            player.position = 39
            mode.communityChanceMessage = 'Advance to the Boardwalk'
        #Advance to the St. Charles
        elif communityChanceCard.name == '12':
            if player.position % 40 > 11:
                player.money += 200
            player.position = 11
            mode.communityChanceMessage = 'Advance to the St. Charles Place'
                
    def landOnCommunityChance(mode):
        if len(communityChanceList) == 0:
            mode.reshuffleCommunictyChance()
        currCommunityChance = communityChanceList.pop(0)
        #player 1
        if mode.turnCounter % 2 == 0:
            if isinstance(currCommunityChance, CommunityChanceCardMoney):
                mode.player1.money += currCommunityChance.action
                if currCommunityChance.action > 0:
                    mode.player1.lastTransaction = f'+${currCommunityChance.action}'
                else:
                    absValAction = currCommunityChance.action * -1
                    mode.player1.lastTransaction = f'-${absValAction}'
                mode.communityChanceMessage = currCommunityChance.message
                print(currCommunityChance.message)
                print('money action player 1')
            elif isinstance(currCommunityChance, CommunityChanceCardMovement):
                mode.moveAction(currCommunityChance, mode.player1)
                print('move action player 1')
        #computer
        else:
            if isinstance(currCommunityChance, CommunityChanceCardMoney):
                mode.computer.money += currCommunityChance.action
                if currCommunityChance.action > 0:
                    mode.computer.lastTransaction = f'+${currCommunityChance.action}'
                else:
                    absValAction = currCommunityChance.action * -1
                    mode.computer.lastTransaction = f'-${absValAction}'
                mode.communityChanceMessage = currCommunityChance.message
                print(currCommunityChance.message)
                print('money action computer')
            elif isinstance(currCommunityChance, CommunityChanceCardMovement):
                mode.moveAction(currCommunityChance, mode.computer)
                print('move action computer')
        mode.actionsAfterRoll()
            
                
    def landOpponentOrTax(mode):
        if mode.turnCounter % 2 == 0:
            #redefine location as space
            space = board[mode.player1.position % 40]
            if space in mode.computer.properties:
                if isinstance(space, Property):
                    rent = mode.rentPriceProperty(space, mode.computer)
                    print(space.double)
                    mode.player1.money -= rent
                    mode.player1.lastTransaction = f'-${rent}'
                    mode.computer.money += rent
                    mode.computer.lastTransaction = f'+${rent}'
                elif isinstance(space, Utilities):
                    rent = mode.rentPriceUtility(space, mode.computer)
                    mode.player1.money -= rent
                    mode.player1.lastTransaction = f'-${rent}'
                    mode.computer.money += rent
                    mode.computer.lastTransaction = f'+${rent}'
                elif isinstance(space, Railroad):
                    rent = mode.rentPriceRailroad(space)
                    mode.player1.money -= rent
                    mode.player1.lastTransaction = f'-${rent}'
                    mode.computer.money += rent
                    mode.computer.lastTransaction = f'+${rent}'
            elif isinstance(space, Tax):
                mode.player1.money -= space.tax
                mode.player1.lastTransaction = f'-${space.tax}'
            if len(mode.announcements) == 5:
                mode.announcements = mode.announcements[1:]
            if isinstance(space, CommunityChance):
                if (space.name == 'Community Chest Side 1' or space.name == 'Community Chest Side 2' or 
                    space.name == 'Community Chest Side 4'):
                    mode.announcements.append(f'Player 1 landed on Community Chest')
                else:
                    mode.announcements.append('Player 1 landed on Chance')
                mode.landOnCommunityChance()
            else:
                mode.announcements.append(f'Player 1 landed on {space.name}')
            

        else:
            #redefine location as space
            space = board[mode.computer.position % 40]
            #if where you landed is owned by the opponent, pay rent
            if space in mode.player1.properties:
                if isinstance(space, Property):
                    rent = mode.rentPriceProperty(space, mode.player1)
                    print(space.double)
                    for element in mode.player1.properties:
                        print(f'{element.name}: {element.double}')
                    mode.computer.money -= rent
                    mode.computer.lastTransaction = f'-${rent}'
                    mode.player1.money += rent
                    mode.player1.lastTransaction = f'+${rent}'
                elif isinstance(space, Utilities):
                    rent = mode.rentPriceUtility(space, mode.player1)
                    mode.computer.money -= rent
                    mode.computer.lastTransaction = f'-${rent}'
                    mode.player1.money += rent
                    mode.player1.lastTransaction = f'+${rent}'
                elif isinstance(space, Railroad):
                    rent = mode.rentPriceRailroad(space)
                    mode.computer.money -= rent
                    mode.computer.lastTransaction = f'-${rent}'
                    mode.player1.money += rent
                    mode.player1.lastTransaction = f'+${rent}'
            elif isinstance(space, Tax):
                mode.computer.money -= space.tax
                mode.computer.lastTransaction = f'-${space.tax}'
            if len(mode.announcements) == 5:
                mode.announcements = mode.announcements[1:]
            if isinstance(space, CommunityChance):
                if (space.name == 'Community Chest Side 1' or space.name == 'Community Chest Side 2' or 
                    space.name == 'Community Chest Side 4'):
                    mode.announcements.append(f'Computer landed on Community Chest')
                else:
                    mode.announcements.append('Computer landed on Chance')
                mode.landOnCommunityChance()
            else:
                mode.announcements.append(f'Computer landed on {space.name}')

   
    def rollDice(mode):
        if mode.rollCounter == 0:
            mode.player1.lastTransaction = '$0'
            mode.computer.lastTransaction = '$0'
            mode.counterDrawPlayer1 = 1
            mode.counterDrawComputer = 1
            mode.rollCounter += 1
            dice1, dice2 = mode.diceRoll()
            if len(mode.announcements) == 5:
                mode.announcements = mode.announcements[1:]
                if mode.turnCounter % 2 == 0:
                    mode.announcements.append('Player 1 rolled the dice')
                else:
                    mode.announcements.append('Computer rolled the dice')
            elif len(mode.announcements) < 5:
                if mode.turnCounter % 2 == 0:
                    mode.announcements.append('Player 1 rolled the dice')
                else:
                    mode.announcements.append('Computer rolled the dice')
            double = False
            if dice1 == dice2:
                double = True
            #print(dice1, dice2)
            #print(f'roll doubes? {double}')
            #stores the previous dice in the app
            mode.prevRoll = dice1 + dice2
            mode.dice = (dice1, dice2)
            diceTotal = dice1 + dice2
            mode.didRollAndPassGo(diceTotal, double)
            mode.actionsAfterRoll()
            '''
            mode.didRollAndPassGo(diceTotal, double)
            mode.landOpponentOrTax()
            mode.player1.doubleRent()
            mode.player1.propertySort()
            mode.computer.doubleRent()
            mode.computer.propertySort()
            mode.checkEndGame()
            '''
            
    def actionsAfterRoll(mode):
        #check pass go
        mode.landOpponentOrTax()
        mode.player1.doubleRent()
        mode.player1.propertySort()
        mode.computer.doubleRent()
        mode.computer.propertySort()
        mode.checkEndGame()
        
        '''
        print(mode.withinRange(0, 38)) #True
        print(mode.withinRange(0, 28)) #True
        print(mode.withinRange(12, 0)) #True
        print(mode.withinRange(6, 37)) #True
        print(mode.withinRange(6, 34)) #True
        print(mode.withinRange(6, 33)) #False
        print(mode.withinRange(2,0))   #True
        print(mode.withinRange(4, 32)) #True
        print(mode.withinRange(4, 31)) #False
        '''
    def checkEndGame(mode):
        global winner
        if mode.player1.money < 0:
            winner = mode.computer
            mode.app.setActiveMode(mode.app.gameOverMode)
        elif mode.computer.money < 0:
            winner = mode.player1
            mode.app.setActiveMode(mode.app.gameOverMode)
                    
    def endTurn(mode):
        print(f'Computer: {mode.computer.critMoney}')
        if mode.rollCounter == 1:
            mode.turnCounter += 1
            mode.rollCounter = 0
            if len(mode.announcements) == 5:
                mode.announcements = mode.announcements[1:]
                if mode.turnCounter % 2 == 1:
                    mode.announcements.append('Player 1 ended their turn')
                else:
                    mode.announcements.append('Computer ended their turn')
            elif len(mode.announcements) < 5:
                if mode.turnCounter % 2 == 1:
                    mode.announcements.append('Player 1 ended their turn')
                else:
                    mode.announcements.append('Computer ended their turn')
            mode.player1.doubleRent()
            mode.player1.propertySort()
            mode.computer.doubleRent()
            mode.computer.propertySort()
            mode.checkEndGame()
            if mode.turnCounter % 2 == 1:
                mode.monopolyAI()
        
############################  AI Select Spaces  ###################################  

    def propertySelection(mode, x, y):
        #print(mode.nextSelected)
        if mode.nextSelected:
            for space in board:
                if isinstance(space,Property):
                    space.selected = False
                    
            #selection from side 1
            if (x >= 810 - 26.25 and x <= 810 + 26.25 and 
                y >= 628 - 42.5 and y <= 628 + 42.5):
                mediterranean.selected = True
            elif (x >= 705 - 26.25 and x <= 705 + 26.25 and 
                y >= 628 - 42.5 and y <= 628 + 42.5):
                baltic.selected = True
            elif (x >= 547.5 - 26.25 and x <= 547.5 + 26.25 and 
                y >= 628 - 42.5 and y <= 628 + 42.5):
                oriental.selected = True
            elif (x >= 442.5 - 26.25 and x <= 442.5 + 26.25 and 
                y >= 628 - 42.5 and y <= 628 + 42.5):
                vermont.selected = True
            elif (x >= 390 - 26.25 and x <= 390 + 26.25 and 
                y >= 628 - 42.5 and y <= 628 + 42.5):
                connecticut.selected = True
            
            #selection from side 2
            elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
                y >= 560 - 26.25 and y <= 560 + 26.25):
                stCharles.selected = True
            elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
                y >= 455 - 26.25 and y <= 455 + 26.25):
                state.selected = True
            elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
                y >= 402.5 - 26.25 and y <= 402.5 + 26.25):
                virginia.selected = True
            elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
                y >= 297.5 - 26.25 and y <= 297.5 + 26.25):
                stJames.selected = True
            elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
                y >= 192.5 - 26.25 and y <= 192.5 + 26.25):
                tennessee.selected = True
            elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
                y >= 140 - 26.25 and y <= 140 + 26.25):
                newYork.selected = True
        
            #selection from side 3
            elif (x >= 390 - 26.25 and x <= 390 + 26.25 and 
                y >= 70 - 42.5 and y <= 70 + 42.5):
                kentucky.selected = True
            elif (x >= 495 - 26.25 and x <= 495 + 26.25 and 
                y >= 70 - 42.5 and y <= 70 + 42.5):
                indiana.selected = True
            elif (x >= 547.5 - 26.25 and x <= 547.5 + 26.25 and 
                y >= 70 - 42.5 and y <= 70 + 42.5):
                illinois.selected = True
            elif (x >= 652.5 - 26.25 and x <= 652.5 + 26.25 and 
                y >= 70 - 42.5 and y <= 70 + 42.5):
                atlantic.selected = True
            elif (x >= 705 - 26.25 and x <= 705 + 26.25 and 
                y >= 70 - 42.5 and y <= 70 + 42.5):
                vetnor.selected = True
            elif (x >= 810 - 26.25 and x <= 810 + 26.25 and 
                y >= 70 - 42.5 and y <= 70 + 42.5):
                marvin.selected = True
            
            #selection from side 4
            elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
                y >= 140 - 26.25 and y <= 140 + 26.25):
                pacific.selected = True
            elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
                y >= 192.5 - 26.25 and y <= 192.5 + 26.25):
                northCarolina.selected = True
            elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
                y >= 297.5 - 26.25 and y <= 297.5 + 26.25):
                pennsylvania.selected = True
            elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
                y >= 455 - 26.25 and y <= 455 + 26.25):
                parkPlace.selected = True
            elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
                y >= 560 - 26.25 and y <= 560 + 26.25):
                boardwalk.selected = True
               
            selected = None
            for space in board:
                if isinstance(space, Property):
                    if space.selected:
                        selected = space
            if selected != None:
                mode.buyHouse(selected)
           
        #print(mode.selectionCounter)
        if mode.selectionCounter >= 1:
            mode.selectionCounter = 0
            mode.nextSelected = False
            
#######################  Monopoly Aritifical Intelligence  #####################

    def expectedValue(mode, space):
        expectedValueResult = 0
        #if where you landed is owned by the opponent, pay rent, so we can add 
        #that to the expected value
        if space in mode.player1.properties:
            if isinstance(space, Property):
                rent = mode.rentPriceProperty(space, mode.player1)
                expectedValueResult -= rent
            elif isinstance(space, Utilities):
                rent = mode.rentPriceUtility(space, mode.player1)
                expectedValueResult -= rent
            elif isinstance(space, Railroad):
                rent = mode.rentPriceRailroad(space)
                expectedValueResult -= rent
        elif isinstance(space, Tax):
            expectedValueResult -= space.tax
        return expectedValueResult
        
    def comboCalculator(mode, n, k):
        return math.factorial(n) / ((math.factorial(k))*(math.factorial(n-k)))
        
    #this function checks whether the positions a and b are within range of 
    #one move, returns an ordered pair of boolean and distance
    #we can let a represent the position of the target space and b represent the 
    #position of the opponent
    def withinRange(mode, a, b):
        if a >= 12 and a < 40:
            if b >= a - 12 and b <= a - 2:
                return (True, a - b)
            else:
                return (False, (a - b) % 40)
        elif a < 12 and a >= 2:
            if b >= 0 and b <= a - 2:
                return (True, a - b)
            elif b <= 39 and b >= (a - 12) % 40:
                return (True, a + 40 - b) 
            else:
                return (False, a - b % 40)
        elif a == 1 or a == 0:
            if b <= (a - 2) % 40 and b >= (a - 12)  % 40:
                return (True, a + 40 - b)
            else:
                return (False, a - b % 40)
    

    def probabilityCalculator(mode, n):
        # n represents how many spaces
        if n == 2 or n == 12:
            return 1 / 6 * 1 / 6
        elif n == 3 or n == 11:
            return 2 * (1 / 6 * 1 / 6)
        elif n == 4 or n == 10:
            return 3 * (1 / 6 * 1 / 6)
        elif n == 5 or n == 9:
            return 4 * (1 / 6 * 1 / 6)
        elif n == 6 or n == 8:
            return 5 * (1 / 6 * 1 / 6)
        elif n == 7:
            return 6 * (1 / 6 * 1 / 6)
    
    def rentHomeCalculator(mode, space, num):
        if num == 1:
            return space.h1
        elif num == 2:
            return space.h2
        elif num == 3:
            return space.h3
        elif num == 4:
            return space.h4
        elif num == 5:
            return space.hotel
            
    def rentAcquiredProperty(mode, space):
        color = space.color
        counter = 0
        player1Potential = mode.player1.money
        for prop in mode.player1.properties:
            if isinstance(prop, Property) and prop.color == color:
                counter += 1
        if color == 'blue' or color == 'brown':
            if player1Potential >= space.cost:
                player1Potential -= space.cost
                if counter == 1:
                    houses = player1Potential // space.houseCost
                    if houses >= 10:
                        return space.hotel
                    elif houses % 2 == 1:
                        boughtHouse = houses // 2 + 1
                        return mode.rentHomeCalculator(space, boughtHouse)
                    else:
                        boughtHouse == houses // 2
                        if boughtHouse == 0:
                            return space.rent * 2
                        else:
                            return mode.rentHomeCalculator(space, boughtHouse)
                else:
                    return space.rent
            return 0
        else:
            if player1Potential >= space.cost:
                player1Potential -= space.cost
                if counter == 2:
                    houses = player1Potential // space.houseCost
                    if houses >= 10:
                        return space.hotel
                    elif houses % 3 == 1 or houses % 3 == 2:
                        boughtHouse = houses // 2 + 1
                        return mode.rentHomeCalculator(space, boughtHouse)
                    else:
                        boughtHouse = houses // 2
                        if boughtHouse == 0:
                            return space.rent * 2
                        else:
                            return mode.rentHomeCalculator(space, boughtHouse)
                else:
                    return space.rent
            return 0
    
    def rentAcquiredUtilities(mode, space, range):
        counter = 0
        for prop in mode.player1.properties:
            if isinstance(prop, Utilities):
                counter += 1
        player1Potential = mode.player1.money
        if player1Potential >= space.cost:
            player1Potential -= space.cost
            if counter == 1:
                return 10 * range
            else:
                return 4 * range
        return 0
        
    def rentAcquiredRailroad(mode, space):
        counter = 0
        for prop in mode.player1.properties:
            if isinstance(prop, Railroad):
                counter += 1
        player1Potential = mode.player1.money
        if player1Potential >= space.cost:
            player1Potential -= space.cost
            if counter == 1:
                return 50
            elif counter == 2:
                return 100
            elif counter == 3:
                return 200
            else:
                return 25
        return 0
            
    def rentIfAcquired(mode, space, range):
        if isinstance(space,Property):
            return mode.rentAcquiredProperty(space)
        elif isinstance(space, Utilities):
            return mode.rentAcquiredUtilities(space, range)
        elif isinstance(space, Railroad):
            return mode.rentAcquiredRailroad(space)
            
    def potentialLossFromOpponent(mode, position):
        sumExpectedValuePotential = 0
        for n in range(2,13):
            posValue = (position + n) % 40
            space = board[posValue]
            opponentPosValue = mode.player1.position % 40
            boolRange, distance = mode.withinRange(posValue, opponentPosValue)
            if (isinstance(space, Property) or isinstance(space, Utilities) or 
                isinstance(space, Railroad)) and (space in propertySet):
                #if the space we are looking at is both unowned and a space where rent needs to be paid,
                #we assume that the opponent will buy it and therefore will require us to have some money
                #we now have to check whether or not it will complete a set, and if it does complete a set
                #we assume the worst case and the opponent will buy the maxnumber of houses
                if boolRange:
                    #print(space.name)
                    sumExpectedValuePotential += (mode.probabilityCalculator(distance) * 
                                                  mode.rentIfAcquired(space, distance))
        return sumExpectedValuePotential
    
    def secondDepthMaxPay(mode, position):
        maxVal = 0
        for n in range(2,13):
            space = board[ (position + n) % 40 ]
            expectedPay = mode.expectedValue(space)
            for m in range(2,13):
                secondSpace = board[(position + n + m) % 40]
                secondExpectedPay = mode.expectedValue(secondSpace)
                if secondExpectedPay + expectedPay < maxVal:
                    maxVal = secondExpectedPay + expectedPay
        return maxVal
                
            
    def sumExpectedValue(mode, position):
        sumExpectedValueResult = 0
        for n in range(2,13):
            space = board[(position + n) % 40]
            #if mode.expectedValue(space) <= -50:
            #   sumExpectedValueResult += mode.expectedValue(space)
            print(f'{space.name}: {mode.expectedValue(space)}')
            sumExpectedValueResult += (mode.probabilityCalculator(n) * 
                                       mode.expectedValue(space))
            
        sumExpectedValueResult -= mode.potentialLossFromOpponent(position)
        return sumExpectedValueResult
        
    def secondDepthSumExpectedValue(mode):
        sumSecondExpectedValue = 0
        for n in range(2,13):
            space = board[(mode.computer.position + n) % 40]
            position = mode.computer.position + n
            sumSecondExpectedValue += (mode.probabilityCalculator(n) * 
                        (mode.expectedValue(space) + mode.sumExpectedValue(position)))
            #print(space.name)
            #print(f'expected val: {mode.expectedValue(space)}')
            #print(f'sumExpectedVal: {mode.sumExpectedValue(position)}')
            #print(f'Second Depth:{sumSecondExpectedValue}')
        sumSecondExpectedValue += mode.secondDepthMaxPay(mode.computer.position)
        return sumSecondExpectedValue
        
    def AIBuyHouse(mode, color):
        houseBuild = []
        for space in board:
            if isinstance(space, Property):
                if space.color == color:
                    houseBuild.append(space)
        #print(f'houseBuild: {houseBuild}')
        for i in range(5):
            for space in houseBuild:
                if (mode.computer.money - mode.computer.critMoney > houseBuild[0].houseCost):
                    mode.buyHouse(space)
                    #print(space.color)
    
    def monopolyAI(mode):
        #list of things my AI needs to do 
        #1. find the expected value change on the next 2 moves 
        #2. find the critical money value held based ont he expected value change
        #3. use the extra money either to buy properties the next 2 rounds or 
        #   buy houses when possible
        mode.rollDice()
        mode.computer.critMoney = mode.secondDepthSumExpectedValue()
        mode.computer.critMoney = int(mode.computer.critMoney) - 1
        mode.computer.critMoney *= -1
        if mode.computer.money > mode.computer.critMoney:
            #buy property if you can and have extra money
            space = board[mode.computer.position % 40]
            if ((isinstance(space, Property) or isinstance(space, Utilities) or 
                 isinstance(space, Railroad)) and 
                 mode.computer.money - mode.computer.critMoney > space.cost):
                mode.buyProperty()
            
            #buy houses if you can and have extra money
            #print(mode.computer.colorBuild)
            for element in mode.computer.colorBuild:
                #print(element)
                mode.AIBuyHouse(element)
        mode.endTurn()
        print(f'AI Turn Counter: {mode.turnCounter}')
            
        

###############################  User Input  ################################### 

    def mousePressed(mode, event):
        mode.selectionCounter += 1
        #pressed buy property button
        if (event.x >= 140 - 85 and event.x <= 140 + 85 and 
            event.y >= 490 and event.y <= 530 
            and mode.turnCompletedPlayer1 and mode.turnCompletedComputer):
            mode.buyProperty()
            print('you pressed the buy property button')
            
        #pressed roll dice button
        if (event.x >= 205 - 63 and event.x <= 205 + 63 and 
            event.y >= 420 and event.y <= 460
            and mode.turnCompletedPlayer1 and mode.turnCompletedComputer):
            print('you pressed the roll dice button')
            mode.communityChanceMessage = ''
            mode.rollDice()
            
        #pressed end turn button
        if (event.x >= 140-64 and event.x <= 140 + 64 and 
            event.y >= 630 and event.y <= 670
            and mode.turnCompletedPlayer1 and mode.turnCompletedComputer):
            mode.endTurn()
            mode.animationSkip = False
            print('you pressed the end turn button')
            
        #pressed buy house button
        if (event.x >= 140-72 and event.x <= 140+72 and 
            event.y >= 560 and event.y <= 600
            and mode.turnCompletedPlayer1 and mode.turnCompletedComputer):
            
            mode.selectionCounter = 0
            mode.nextSelected = True
            print('you pressed the buyHouse button')
            
        #property selection
        mode.propertySelection(event.x, event.y)
        for space in board:
            if isinstance(space, Property):
                if space.selected == True:
                    print(f'{space.name} is selected') 
            

    def keyPressed(mode, event):
        if event.key == 'h':
            mode.app.setActiveMode(mode.app.helpMode)
        if event.key == 'o':
            
            #showing that buying houses works
            #easy to show pass go 
            #easy to show critical value calculator
            mode.player1.colorBuild.add('grey')
            mode.player1.properties.append(oriental)
            mode.player1.properties.append(vermont)
            mode.player1.properties.append(connecticut)
            
            mode.player1.colorBuild.add('orange')
            mode.player1.properties.append(stJames)
            mode.player1.properties.append(tennessee)
            mode.player1.properties.append(newYork)
            mode.player1.doubleRent()
            
            
            propertySet.remove(oriental)
            propertySet.remove(vermont)
            propertySet.remove(connecticut)
            
            propertySet.remove(stJames)
            propertySet.remove(tennessee)
            propertySet.remove(newYork)
            
        if event.key == 'j':
            mode.skipAnimation = True
            mode.player1.inJail = True
            mode.player1.position = 10
            mode.tempPositionPlayer1 = 10
            mode.computer.inJail = True
            mode.computer.position = 10
            mode.tempPositionComputer = 10
        
    def timerFired(mode):
        mode.counterDrawPlayer1 += 1
        mode.counterDrawComputer += 1
        '''
        if mode.turnCounter % 2 == 1:
            mode.counterDrawPlayer1 += 1
        else:
            mode.counterDrawComputer += 1
        '''
############################  AI Draw Functions  ###############################
        
    def drawPlayer1Path(mode,canvas,x,y):
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill = 'blue')
        
    def drawComputerPath(mode,canvas,x,y):
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill = 'green')
        
    def drawPlayer1(mode, canvas, player1):
        position = player1.position % 40
        if mode.tempPositionPlayer1 % 40 == position:
            mode.turnCompletedPlayer1 = True
        if mode.counterDrawPlayer1 % 4 == 0 and not mode.turnCompletedPlayer1:
            mode.tempPositionPlayer1 += 1
        (x, y) = mode.player1Locations[mode.tempPositionPlayer1 % 40]
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill = 'blue')
        #print(f'temp: {mode.tempPositionPlayer1}')
        #print(f'position: {position}')
        #print(f'counterDrawPlayer: {mode.counterDrawPlayer}')
        
    def drawComputer(mode, canvas, computer):
        position = computer.position % 40
        if mode.tempPositionComputer % 40 == position:
            mode.turnCompletedComputer = True
        if mode.counterDrawComputer % 4 == 0 and not mode.turnCompletedComputer:
            mode.tempPositionComputer += 1
        (x, y) = mode.computerLocations[mode.tempPositionComputer % 40]
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill = 'green')
        
    def drawPlayer1Values(mode, canvas, player1):
        canvas.create_rectangle(930,10,1190, 345)
        canvas.create_rectangle(940, 20, 1180, 60, fill = fill)
        canvas.create_text(1060,40,text = (f'Player 1'), font = 'Arial, 18')
        canvas.create_text(940, 80, text = (f'Money: ${player1.money}'), anchor = 'w')
        canvas.create_text(1066, 80, text = (f'Last Trans: {player1.lastTransaction}'), 
                           anchor = 'w')
        canvas.create_text(950,100,text = 'Properties:', anchor = 'w')
        canvas.create_text(1076,100, text = 'Houses:', anchor = 'w')
        counter = 0
        r = 4
        for element in player1.properties:
            canvas.create_text(950, 130 + (18 * counter), text = element.name, anchor = 'w')
            if isinstance(element, Property):
                for circleCounter in range(5):
                    if circleCounter == element.numHouse - 1 and circleCounter == 4:
                        canvas.create_oval(1080-r + (20 * circleCounter),130 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 130 + r + (18 * counter),
                                        fill = 'red')
                    elif circleCounter <= element.numHouse - 1:
                        canvas.create_oval(1080-r + (20 * circleCounter),130 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 130 + r + (18 * counter),
                                        fill = 'green')
                    else:
                        canvas.create_oval(1080-r + (20 * circleCounter),130 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 130 + r + (18 * counter))
            counter += 1
        
    def drawComputerValues(mode, canvas, computer):
        canvas.create_rectangle(930, 355, 1190, 690)
        canvas.create_rectangle(940, 365, 1180, 405, fill = fill)
        canvas.create_text(1060,385,text = (f'Computer'), font = 'Arial, 18')
        canvas.create_text(940, 425, text = (f'Money: ${computer.money}'), anchor = 'w')
        canvas.create_text(1066, 425, text = (f'Last Trans: {computer.lastTransaction}'), 
                           anchor = 'w')
        canvas.create_text(1003 , 445, text = (f'Critical Level: ${mode.computer.critMoney}'), 
                           anchor = 'w')
        canvas.create_text(950,465,text = 'Properties:', anchor = 'w')
        canvas.create_text(1076,465, text = 'Houses:', anchor = 'w')
        counter = 0
        r = 4
        for element in computer.properties:
            canvas.create_text(950, 495 + (18 * counter), text = element.name, anchor = 'w')
            if isinstance(element, Property):
                for circleCounter in range(5):
                    if circleCounter == element.numHouse - 1 and circleCounter == 4:
                        canvas.create_oval(1080-r + (20 * circleCounter),495 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 495 + r + (18 * counter),
                                        fill = 'red')
                    elif circleCounter <= element.numHouse - 1:
                        canvas.create_oval(1080-r + (20 * circleCounter),495 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 495 + r + (18 * counter),
                                        fill = 'green')
                    else:
                        canvas.create_oval(1080-r + (20 * circleCounter),495 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 495 + r + (18 * counter))
            counter += 1
        '''
        canvas.create_text(1075,200,text = (
                           f'computer money:{mode.computer.money}'))
        canvas.create_text(1075,220,text = 'properties')
        counter = 0
        for element in computer.properties:
            canvas.create_text(940, 240 + (20 * counter), text = element.name, anchor = 'w')
            counter += 1
        
        '''   
     
    def drawDice(mode, canvas):
        (dice1, dice2) = mode.dice
        canvas.create_rectangle(20, 410, 125, 470, fill = fill)
        #canvas.create_text(45, 400, text = 'Dice:', font = 'Arial, 22')
        if dice1 == 1:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceOne))
        elif dice1 == 2:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceTwo))
        elif dice1 == 3:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceThree))
        elif dice1 == 4:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceFour))
        elif dice1 == 5:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceFive))
        elif dice1 == 6:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceSix))
        if dice2 == 1:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceOne))
        elif dice2 == 2:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceTwo))
        elif dice2 == 3:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceThree))
        elif dice2 == 4:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceFour))
        elif dice2 == 5:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceFive))
        elif dice2 == 6:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceSix))
        
        
        
        
    def drawTurn(mode, canvas):
        canvas.create_rectangle(50, 140, 230, 180, fill = fill)
        canvas.create_text(90, 160, text = 'Turn:', font = 'Arial 22')
        if mode.turnCounter % 2 == 0:
            canvas.create_text(180, 160, text = 'Player 1', font = 'Arial 20')
        else:
            canvas.create_text(180, 160, text = 'Computer', font = 'Arial 20')
        
        
    def drawHouse(mode, canvas):
        spaceIndex = 0
        for property in housePosition:
            if property != None:
                counter = 0
                if board[spaceIndex].numHouse == 5:
                    space = board[spaceIndex]
                    x, y = property[1]
                    if space.color == 'brown' or space.color == 'grey':
                        canvas.create_rectangle(x - 4.5, y - 4.5, x + 16.5, 
                                                y + 4.5, fill = 'red')
                    elif space.color == 'pink' or space.color == 'orange':
                        canvas.create_rectangle(x - 4.5, y - 4.5, x + 4.5, 
                                                y + 16.5, fill = 'red')
                    elif space.color == 'red' or space.color == 'yellow':
                        canvas.create_rectangle(x - 16.5, y - 4.5, x + 4.5, 
                                                y + 4.5, fill = 'red')
                    elif space.color == 'green' or space.color == 'blue':
                        canvas.create_rectangle(x - 4.5, y - 16.5, x + 4.5, 
                                                y + 4.5, fill = 'red')
                else:
                    for houseCoor in property:
                        if counter < board[spaceIndex].numHouse and counter < 4:
                            x, y = houseCoor
                            canvas.create_rectangle(x-4.5,y-4.5,x+4.5,y+4.5,fill = 'green')
                        counter += 1
            spaceIndex += 1

    def drawPropArea(mode, canvas):
        for pair in coorSide1:
            x,y = pair
            canvas.create_rectangle(x - 26.25, y - (42.5), 
                                    x + 26.25, y + (42.5), fill = 'red')
                                    
        for pair in coorSide2:
            x,y = pair
            canvas.create_rectangle(x-42.5, y-26.25, x+42.5, y+26.25, fill = 'red')
        
        for pair in coorSide3:
            x,y = pair
            canvas.create_rectangle(x - 26.25, y - (42.5), 
                                    x + 26.25, y + (42.5), fill = 'red')
        
        for pair in coorSide4:
            x,y = pair
            canvas.create_rectangle(x-42.5, y-26.25, x+42.5, y+26.25, fill = 'red')
            
    def drawAnnouncements(mode, canvas):
        counter = 0
        canvas.create_rectangle(10, 210, 270, 380, fill = fill)
        canvas.create_text(140, 230, text = 'Announcements:', font = 'Arial, 20')
        for message in mode.announcements:
            canvas.create_text(140, 260 + 25 * counter, text = message, font = 'Arial 16')
            counter += 1
            
    def drawCommunityChanceMessage(mode, canvas):
        canvas.create_rectangle(215, 675, 920, 708, fill = fill)
        canvas.create_text(225, 691.5, text = 'Community Chest or Chance Message:' ,anchor = 'w')
        canvas.create_text(480, 691.5, text = f'{mode.communityChanceMessage}', anchor = 'w')
        
    

    def redrawAll(mode, canvas):
        #draw turn
        mode.drawTurn(canvas)
        
        #draw logo
        canvas.create_image(140, 65, image = ImageTk.PhotoImage(mode.logo))
        
        #draw board
        canvas.create_image(600, 350,
                            image=ImageTk.PhotoImage(mode.board))
                            
        #draw buy property button 
        canvas.create_image(140, 510, image =
                            ImageTk.PhotoImage(mode.buy))
                            
        #draw end turn button
        canvas.create_image(140, 650, image = 
                            ImageTk.PhotoImage(mode.turn))
                            
        #draw roll dice button
        canvas.create_image(205, 440, image = 
                            ImageTk.PhotoImage(mode.roll))
                            
        #draw buy house button
        canvas.create_image(140, 580, image = 
                            ImageTk.PhotoImage(mode.buyHouseButton))
        
        #draw players
        mode.drawPlayer1(canvas, mode.player1)
        mode.drawComputer(canvas, mode.computer)
        
        #draw players values
        mode.drawPlayer1Values(canvas, mode.player1)
        mode.drawComputerValues(canvas, mode.computer)
        
        #finding coordinates for houses
        
        mode.drawHouse(canvas)
        #mode.drawPropArea(canvas)
        
        canvas.create_text(mode.width / 2, mode.height / 2, text = 'THIS IS THE AI MODE', font = 'Arial 50 bold')
        mode.drawAnnouncements(canvas)
        
        mode.drawDice(canvas)
        
        mode.drawCommunityChanceMessage(canvas)
        
        #print(mode.secondDepthSumExpectedValue())
        #print(mode.sumExpectedValue(baltic))
        
        
        '''
        #help find player location on the board
        for location in mode.player1Locations:
            (xcor, ycor) = location
            mode.drawPlayer1Path(canvas,xcor,ycor)
            
        for location in mode.computerLocations:
            h(xcor, ycor) = location
            mode.drawcomputerPath(canvas,xcor,ycor)
        '''
        
################################################################################
################################################################################
############################# AI vs AI mode  ###################################
################################################################################
################################################################################

class AIAIMode(Mode):
    def appStarted(mode):
        mode.computer1 = Player('Computer1 AI')
        mode.computer2 = Player('Computer2 AI')
        mode.turnCompletedComputer1 = True
        mode.turnCompletedComputer2 = True
        mode.oldPositionComputer1 = 0
        mode.tempPositionComputer1 = 0
        mode.oldPositionComputer2 = 0
        mode.tempPositionComputer2 = 0
        mode.counterDrawComputer1 = 0
        mode.counterDrawComputer2 = 0
        mode.nextSelected = False
        mode.selectionCounter = 0
        mode.communityChanceMessage = ''
        mode.animationSkip = False
        
        
        
        #showing that buying houses works
        mode.computer1.colorBuild.add('grey')
        mode.computer1.properties.append(oriental)
        mode.computer1.properties.append(vermont)
        mode.computer1.properties.append(connecticut)
        mode.computer1.doubleRent()
        
        '''
        for space in mode.computer1.properties:
            print(f'{space.name}: {space.double}')
        '''
        '''
        mode.computer.colorBuild.add('green')
        mode.computer.properties.append(pacific)
        mode.computer.properties.append(northCarolina)
        mode.computer.properties.append(pennsylvania)
        
        mode.computer.colorBuild.add('yellow')
        mode.computer.properties.append(atlantic)
        mode.computer.properties.append(vetnor)
        mode.computer.properties.append(marvin)
        
        mode.computer.colorBuild.add('orange')
        mode.computer.properties.append(stJames)
        mode.computer.properties.append(tennessee)
        mode.computer.properties.append(newYork)
        '''
        propertySet.remove(oriental)
        propertySet.remove(vermont)
        propertySet.remove(connecticut)
        
        '''
        propertySet.remove(pacific)
        propertySet.remove(northCarolina)
        propertySet.remove(atlantic)
        propertySet.remove(vetnor)
        propertySet.remove(marvin)
        propertySet.remove(stJames)
        propertySet.remove(tennessee)
        propertySet.remove(newYork)
        propertySet.remove(pennsylvania)
        '''
        
        
        mode.dice = (1,1)
        
        #roll tracking in order to help calculate the rent for utilities
        mode.prevRoll = 0
        
        #roll counter used to make sure the gameplay goes as it is supposed to
        mode.rollCounter = 0
        
        #turn counter
        #if divisible by 2 then it is player 1's turn
        mode.turnCounter = 0
        
        #this is the monopoly logo we are uploading
        logo = ('monopolyLogo.jpg')
        mode.logo = mode.loadImage(logo)
        mode.logo = mode.scaleImage(mode.logo, 0.06)
        
        #this is the board image that we are uploading
        board = ('board.jpg')
        mode.board = mode.loadImage(board)
        
        #this is the buy button that we are uploading
        buyButton = ('buyProperty.png')
        mode.buy = mode.loadImage(buyButton)
        
        #this is the end turn button
        turnButton = ('endTurn.png')
        mode.turn = mode.loadImage(turnButton)
        
        #this is the roll dice button
        rollDice = ('rollDice.png')
        mode.roll = mode.loadImage(rollDice)
        
        #this is the buy house button
        buyHouse = ('buyHouse.png')
        mode.buyHouseButton = mode.loadImage(buyHouse)
        
        #these are the die
        mode.diceOne = mode.loadImage('dice1.png')
        mode.diceOne = mode.scaleImage(mode.diceOne,.3)
        mode.diceTwo = mode.loadImage('dice2.png')
        mode.diceTwo = mode.scaleImage(mode.diceTwo,.3)
        mode.diceThree = mode.loadImage('dice3.png')
        mode.diceThree = mode.scaleImage(mode.diceThree,.3)
        mode.diceFour = mode.loadImage('dice4.png')
        mode.diceFour = mode.scaleImage(mode.diceFour,.3)
        mode.diceFive = mode.loadImage('dice5.png')
        mode.diceFive = mode.scaleImage(mode.diceFive,.3)
        mode.diceSix = mode.loadImage('dice6.png')
        mode.diceSix = mode.scaleImage(mode.diceSix,.3)
        
        
        
        #this is announcementsa
        mode.announcements = []
        
        '''
        #these are the pictures of the dices
        dice1 = 
        mode.dice1 = 
        '''
        
        #THESE ARE THE POSSIBLE LOCATIONS OF PLAYER 1 (outer)
        mode.computer1Locations = []
            
        #pass go, this is where we start appending
        mode.computer1Locations.append((901.5,651.5))
        
        #go to bottom locations
        for i in range(9):
            mode.computer1Locations.append((808.5 - 52.5 * i, 651.5))
            
        #jail
        mode.computer1Locations.append((298.5,651.5))
        
        #go to left locations
        for i in range(9):
            mode.computer1Locations.append((298.5,561.25 - 52.5 * i))
            
        #free parking
        mode.computer1Locations.append((298.5,48.5))
        
        #top locations
        for i in range(9):
            mode.computer1Locations.append((388.5 + 52.5 * i, 48.5))
        
        #go to jail location
        mode.computer1Locations.append((901.5,48.5))
        
        #right locations
        for i in range(9):
            mode.computer1Locations.append((901.5,141.25 + 52.5 * i))
        
        #THESE ARE THE POSSIBLE LOCATIONS OF COMPUTER
        mode.computer2Locations = []
        
        #pass go, this is where we start appending
        mode.computer2Locations.append((876.5,626.5))
        
        #go to bottom locations
        for i in range(9):
            mode.computer2Locations.append((808.5 - 52.5 * i, 626.5))
            
        #jail
        mode.computer2Locations.append((323.5,626.5))
        
        #go to left locations
        for i in range(9):
            mode.computer2Locations.append((323.5,561.25 - 52.5 * i))
            
        #free parking
        mode.computer2Locations.append((323.5,73.5))
        
        #top locations
        for i in range(9):
            mode.computer2Locations.append((388.5 + 52.5 * i, 73.5))
        
        #go to jail location
        mode.computer2Locations.append((876.5, 73.5))
        
        #right locations
        for i in range(9):
            mode.computer2Locations.append((876.5,141.25 + 52.5 * i))
            
        mode.communityChance = []
        
        
    def diceRoll(mode):
        x = random.randint(1,6)
        y = random.randint(1,6)
        return (x,y)
        
        

#################################  AI Buying  ##################################
        
    def buyProperty(mode):
        #computer1 turn
        if mode.turnCounter % 2 == 0:
            space = board[mode.computer1.position % 40]
            if space in propertySet: 
                if mode.computer1.money >= space.cost:
                    mode.computer1.money -= space.cost
                    mode.computer1.lastTransaction = f'-${space.cost}'
                    mode.computer1.properties.append(space)
                    propertySet.remove(space)
                    if len(mode.announcements) == 5:
                        mode.announcements = mode.announcements[1:]
                        mode.announcements.append(f'Computer 1 bought {space.name}')
                    elif len(mode.announcements) < 5:
                        mode.announcements.append(f'Computer 1 bought {space.name}')
        #computer2 turn
        else:
            space = board[mode.computer2.position % 40]
            if space in propertySet: 
                if mode.computer2.money >= space.cost:
                    mode.computer2.money -= space.cost
                    mode.computer2.lastTransaction = f'-${space.cost}'
                    mode.computer2.properties.append(space)
                    propertySet.remove(space)
                    if len(mode.announcements) == 5:
                        mode.announcements = mode.announcements[1:]
                        mode.announcements.append(f'Computer2 bought {space.name}')
                    elif len(mode.announcements) < 5:
                        mode.announcements.append(f'Computer2 bought {space.name}')
        mode.computer1.doubleRent()
        mode.computer1.propertySort()
        mode.computer2.doubleRent()
        mode.computer2.propertySort()
        
    def buyHouseConstraint(mode, property):
        #computer1 turn
        if mode.turnCounter % 2 == 0:
            #print(property.color)
            #print(mode.computer1.colorBuild)
            if (property.color in mode.computer1.colorBuild and mode.computer1.money >= property.houseCost):
                if property.color == 'brown' or property.color == 'blue':
                    a, b = houses[property.color]
                    if property.numHouse == min(a,b):
                        return True
                    else:
                        return False
                else:
                    a, b, c = houses[property.color]
                    if property.numHouse == min(a,b,c):
                        return True
                    else:
                        return False
            return False
        #computer2 turn
        else:
            if (property.color in mode.computer2.colorBuild and mode.computer2.money >= property.houseCost):
                if property.color == 'brown' or property.color == 'blue':
                    a, b = houses[property.color]
                    if property.numHouse == min(a,b):
                        return True
                    else:
                        return False
                else:
                    a, b, c = houses[property.color]
                    if property.numHouse == min(a,b,c):
                        return True
                    else:
                        return False
            return False
            
    def buyHouse(mode, property):
        if mode.buyHouseConstraint(property):
            if property.numHouse <= 4:
                property.numHouse += 1
                if property.color == 'brown' or property.color == 'blue':
                    a,b = houses[property.color]
                    if property.setRank == 1:
                        houses[property.color] = (a+1,b)
                    else:
                        houses[property.color] = (a, b+1)
                    if property in mode.computer1.properties:
                        mode.computer1.money -= property.houseCost
                        mode.computer1.lastTransaction = f'-${property.houseCost}'
                    else:
                        mode.computer2.money -= property.houseCost
                        mode.computer2.lastTransaction = f'-${property.houseCost}'
                else:
                    a,b,c = houses[property.color]
                    if property.setRank == 1:
                        houses[property.color] = (a+1,b,c)
                    elif property.setRank == 2:
                        houses[property.color] = (a,b+1,c)
                    else:
                        houses[property.color] = (a,b,c+1)
                    if property in mode.computer1.properties:
                        mode.computer1.money -= property.houseCost
                        mode.computer1.lastTransaction = f'-${property.houseCost}'
                    else:
                        mode.computer2.money -= property.houseCost
                        mode.computer2.lastTransaction = f'-${property.houseCost}'
                if len(mode.announcements) < 5:
                    if mode.turnCounter % 2 == 0:
                        mode.announcements.append('Computer1 bought a house')
                    else:
                        mode.announcements.append('Computer2 bought a house')
                elif len(mode.announcements) == 5:
                    mode.announcements = mode.announcements[1:]
                    if mode.turnCounter % 2 == 0:
                        mode.announcements.append('Computer1 bought a house')
                    else:
                        mode.announcements.append('Computer2 bought a house')
                        
            #print(houses['grey'])

            
                    
#########################  Rent Price Calculator  ##############################  

    #this function takes in a property and returns how much to pay
    def rentPriceProperty(mode, property, player):
        mode.computer1.doubleRent()
        mode.computer2.doubleRent()
        '''
        for i in range(len(mode.computer1.properties)):
            print(f'{mode.computer1.properties[i].name}: {mode.computer1.properties[i].double}')
            if givenProp == mode.computer1.properties[i]:
                property = mode.computer1.properties[i]
                print(f'{property.name}: {property.double}')
        '''
        if property.numHouse == 0:
            if property.color in player.colorBuild:
                return (property.rent * 2)
            else:
                return property.rent
        elif property.numHouse == 1:
            return property.h1
        elif property.numHouse == 2:
            return property.h2
        elif property.numHouse == 3:
            return property.h3
        elif property.numHouse == 4:
            return property.h4
        elif property.numHouse == 5:
            return property.hotel

    #this function takes in a utility and returns how much to pay
    def rentPriceUtility(mode, utility, player):
        mode.computer1.doubleRent()
        mode.computer.doubleRent()
        if player.utilDouble: 
            return mode.prevRoll * 10
        else:
            return mode.prevRoll * 4
    
    #this function takes in a railroad and returns how much to pay
    def rentPriceRailroad(mode, railroad):
        if mode.turnCounter % 2 == 1:
            mode.computer1.numRail()
            if mode.computer1.numRailroads == 1:
                return railroad.r1
            elif mode.computer1.numRailroads == 2:
                return railroad.r2
            elif mode.computer1.numRailroads == 3:
                return railroad.r3
            elif mode.computer1.numRailroads == 4:
                return railroad.r4
        else:
            mode.computer2.numRail()
            if mode.computer2.numRailroads == 1:
                return railroad.r1
            elif mode.computer2.numRailroads == 2:
                return railroad.r2
            elif mode.computer2.numRailroads == 3:
                return railroad.r3
            elif mode.computer2.numRailroads == 4:
                return railroad.r4
                
###############################  AI Movement  ##################################

    #this implements moving the player and tracking whether or not it 
    #passed or landed on go
    def didRollAndPassGo(mode, dice, doubleBool):
        if mode.turnCounter % 2 == 0:
            mode.turnCompletedComputer1 = False
            if mode.moveForwardJail(doubleBool):
                prev = mode.computer1.position // 40
                mode.oldPositionComputer1 = mode.computer1.position % 40
                mode.tempPositionComputer1 = mode.oldPositionComputer1
                mode.computer1.position += (dice)
                mode.landOnJail()
                if mode.animationSkip:
                    mode.tempPositionComputer1 += dice
                newPos = mode.computer1.position // 40
                if mode.computer1.position % 40 == 0:
                    mode.computer1.money += 400
                    mode.computer1.lastTransaction = f'+$400'
                elif prev != newPos:
                    mode.computer1.money += 200
                    mode.computer1.lastTransaction = f'+$200'
        else:
            mode.turnCompletedComputer2 = False
            if mode.moveForwardJail(doubleBool):
                prev = mode.computer2.position // 40
                mode.oldPositionComputer2 = mode.computer2.position % 40
                mode.tempPositionComputer2 = mode.oldPositionComputer2
                mode.computer2.position += (dice)
                mode.landOnJail()
                if mode.animationSkip:
                    mode.tempPositionComputer2 += dice
                newPos = mode.computer2.position // 40
                if mode.computer2.position % 40 == 0:
                    mode.computer2.money += 400
                    mode.computer2.lastTransaction = f'+$400'
                elif prev != newPos:
                    mode.computer2.money += 200
                    mode.computer2.lastTransaction = f'+$200'
                
    #This is a function that returns a bool on whether or not the player can move
    def moveForwardJail(mode, doubleBool):
        if mode.turnCounter % 2 == 0:
            if mode.computer1.jailCounter == 3:
                mode.computer1.inJail = False
                mode.computer1.money -= 50
                mode.computer1.lastTransaction = f'-$50'
                return True
            elif not doubleBool and mode.computer1.inJail:
                mode.computer1.jailCounter += 1
                return False
            elif doubleBool and mode.computer1.inJail:
                mode.computer1.inJail = False
                mode.computer1.jailCounter = 0
                return True
        else:
            if mode.computer2.jailCounter == 3:
                mode.computer2.money -= 50
                mode.computer2.lastTransaction = f'-$50'
                return True
            elif not doubleBool and mode.computer2.inJail:
                mode.computer2.jailCounter += 1
                return False
            elif doubleBool and mode.computer2.inJail:
                mode.computer2.inJail = False
                mode.computer2.jailCounter = 0
                return True
        return True
        
    def landOnJail(mode):
        
        if mode.turnCounter % 2 == 0:
            if mode.computer1.position % 40 == 30:
                mode.computer1.position -= 20
                mode.computer1.inJail = True
                mode.animationSkip = True
        else:
            if mode.computer2.position % 40 == 30:
                mode.computer2.position -= 20
                mode.computer2.inJail = True
                mode.animationSkip = True
                
    def reshuffleCommunityChance(mode):
        #add back all the cards
        communityChanceList.append(communityChance1)
        communityChanceList.append(communityChance2)
        communityChanceList.append(communityChance3)
        communityChanceList.append(communityChance4)
        communityChanceList.append(communityChance5)
        communityChanceList.append(communityChance6)
        communityChanceList.append(communityChance7)
        communityChanceList.append(communityChance8)
        communityChanceList.append(communityChance9)
        communityChanceList.append(communityChance10)
        communityChanceList.append(communityChance11)
        communityChanceList.append(communityChance12)
        #shuffle the cards
        random.shuffle(communityChanceList)
        
    def nearestRailroad(mode, player):
        curPos = player.position % 40
        if curPos > 5 and curPos < 15:
            player.position = 15
        elif curPos > 15 and curPos < 25:
            player.position = 25
        elif curPos > 25 and curPos < 35:
            player.position = 35
        elif curPos < 5 or curPos > 35:
            player.position = 5
            
    def nearestUtility(mode, player):
        curPos = player.position % 40
        if curPos > 12 and curPos < 28:
            player.position = 28
        else:
            player.position = 12
        
    def moveAction(mode, communityChanceCard, player):
        #move back 3 spaces
        if communityChanceCard.name == '7':
            player.position -= 3
            mode.communityChanceMessage = 'Move back 3 spaces'
        #Advance to the nearest Railroad
        elif communityChanceCard.name == '8':
            mode.communityChanceMessage = 'Advance to the nearest Railroad'
            mode.nearestRailroad(player)
        #Advance to the nearest Utility
        elif communityChanceCard.name == '9':
            mode.communityChanceMessage = 'Advance to the nearest Utility'
            mode.nearestUtility(player)
        #Advance to the Illinois Ave
        elif communityChanceCard.name == '10':
            if player.position % 40 > 24:
                player.money += 200
            player.position = 24
            mode.communityChanceMessage = 'Advance to the Illinois Ave'
        #Advance to the Boardwalk
        elif communityChanceCard.name == '11':
            player.position = 39
            mode.communityChanceMessage = 'Advance to the Boardwalk'
        #Advance to the St. Charles
        elif communityChanceCard.name == '12':
            if player.position % 40 > 11:
                player.money += 200
            player.position = 11
            mode.communityChanceMessage = 'Advance to the St. Charles Place'
                
    def landOnCommunityChance(mode):
        if len(communityChanceList) == 0:
            mode.reshuffleCommunictyChance()
        currCommunityChance = communityChanceList.pop(0)
        #player 1
        if mode.turnCounter % 2 == 0:
            if isinstance(currCommunityChance, CommunityChanceCardMoney):
                mode.computer1.money += currCommunityChance.action
                if currCommunityChance.action > 0:
                    mode.computer1.lastTransaction = f'+${currCommunityChance.action}'
                else:
                    absValAction = currCommunityChance.action * -1
                    mode.computer1.lastTransaction = f'-${absValAction}'
                mode.communityChanceMessage = currCommunityChance.message
                print(currCommunityChance.message)
                print('money action computer1')
            elif isinstance(currCommunityChance, CommunityChanceCardMovement):
                mode.moveAction(currCommunityChance, mode.computer1)
                print('move action computer1')
        #computer
        else:
            if isinstance(currCommunityChance, CommunityChanceCardMoney):
                mode.computer2.money += currCommunityChance.action
                if currCommunityChance.action > 0:
                    mode.computer2.lastTransaction = f'+${currCommunityChance.action}'
                else:
                    absValAction = currCommunityChance.action * -1
                    mode.computer2.lastTransaction = f'-${absValAction}'
                mode.communityChanceMessage = currCommunityChance.message
                print(currCommunityChance.message)
                print('money action computer2')
            elif isinstance(currCommunityChance, CommunityChanceCardMovement):
                mode.moveAction(currCommunityChance, mode.computer)
                print('move action computer2')
            
                
    def landOpponentOrTax(mode):
        if mode.turnCounter % 2 == 0:
            #redefine location as space
            space = board[mode.computer1.position % 40]
            if space in mode.computer2.properties:
                if isinstance(space, Property):
                    rent = mode.rentPriceProperty(space, mode.computer2)
                    print(space.double)
                    mode.computer1.money -= rent
                    mode.computer1.lastTransaction = f'-${rent}'
                    mode.computer2.money += rent
                    mode.computer2.lastTransaction = f'+${rent}'
                elif isinstance(space, Utilities):
                    rent = mode.rentPriceUtility(space, mode.computer2)
                    mode.computer1.money -= rent
                    mode.computer1.lastTransaction = f'-${rent}'
                    mode.computer2.money += rent
                    mode.computer2.lastTransaction = f'+${rent}'
                elif isinstance(space, Railroad):
                    rent = mode.rentPriceRailroad(space)
                    mode.computer1.money -= rent
                    mode.computer1.lastTransaction = f'-${rent}'
                    mode.computer2.money += rent
                    mode.computer2.lastTransaction = f'+${rent}'
            elif isinstance(space, Tax):
                mode.computer1.money -= space.tax
                mode.computer1.lastTransaction = f'-${space.tax}'
            if len(mode.announcements) == 5:
                mode.announcements = mode.announcements[1:]
            if isinstance(space, CommunityChance):
                if (space.name == 'Community Chest Side 1' or space.name == 'Community Chest Side 2' or 
                    space.name == 'Community Chest Side 4'):
                    mode.announcements.append(f'Computer1 landed on Community Chest')
                else:
                    mode.announcements.append('Computer1 landed on Chance')
                mode.landOnCommunityChance()
            else:
                mode.announcements.append(f'Computer1 landed on {space.name}')
            

        else:
            #redefine location as space
            space = board[mode.computer2.position % 40]
            #if where you landed is owned by the opponent, pay rent
            if space in mode.computer1.properties:
                if isinstance(space, Property):
                    rent = mode.rentPriceProperty(space, mode.computer1)
                    print(space.double)
                    for element in mode.computer1.properties:
                        print(f'{element.name}: {element.double}')
                    mode.computer2.money -= rent
                    mode.computer2.lastTransaction = f'-${rent}'
                    mode.computer1.money += rent
                    mode.computer1.lastTransaction = f'+${rent}'
                elif isinstance(space, Utilities):
                    rent = mode.rentPriceUtility(space, mode.computer1)
                    mode.computer2.money -= rent
                    mode.computer2.lastTransaction = f'-${rent}'
                    mode.computer1.money += rent
                    mode.computer1.lastTransaction = f'+${rent}'
                elif isinstance(space, Railroad):
                    rent = mode.rentPriceRailroad(space)
                    mode.computer2.money -= rent
                    mode.computer2.lastTransaction = f'-${rent}'
                    mode.computer1.money += rent
                    mode.computer1.lastTransaction = f'+${rent}'
            elif isinstance(space, Tax):
                mode.computer2.money -= space.tax
                mode.computer2.lastTransaction = f'-${space.tax}'
            if len(mode.announcements) == 5:
                mode.announcements = mode.announcements[1:]
            if isinstance(space, CommunityChance):
                if (space.name == 'Community Chest Side 1' or space.name == 'Community Chest Side 2' or 
                    space.name == 'Community Chest Side 4'):
                    mode.announcements.append(f'Computer2 landed on Community Chest')
                else:
                    mode.announcements.append('Computer2 landed on Chance')
                mode.landOnCommunityChance()
            else:
                mode.announcements.append(f'Computer2 landed on {space.name}')

   
    def rollDice(mode):
        if mode.rollCounter == 0:
            mode.computer1.lastTransaction = '$0'
            mode.computer2.lastTransaction = '$0'
            mode.counterDrawComputer1 = 1
            mode.counterDrawComputer2 = 1
            mode.rollCounter += 1
            dice1, dice2 = mode.diceRoll()
            if len(mode.announcements) == 5:
                mode.announcements = mode.announcements[1:]
                if mode.turnCounter % 2 == 0:
                    mode.announcements.append('Computer1 rolled the dice')
                else:
                    mode.announcements.append('Computer2 rolled the dice')
            elif len(mode.announcements) < 5:
                if mode.turnCounter % 2 == 0:
                    mode.announcements.append('Computer1 rolled the dice')
                else:
                    mode.announcements.append('Computer2 rolled the dice')
            double = False
            if dice1 == dice2:
                double = True
            #print(dice1, dice2)
            #print(f'roll doubes? {double}')
            #stores the previous dice in the app
            mode.prevRoll = dice1 + dice2
            mode.dice = (dice1, dice2)
            diceTotal = dice1 + dice2
            mode.actionsAfterRoll(diceTotal, double)
            '''
            mode.didRollAndPassGo(diceTotal, double)
            mode.landOpponentOrTax()
            mode.computer1.doubleRent()
            mode.computer1.propertySort()
            mode.computer.doubleRent()
            mode.computer.propertySort()
            mode.checkEndGame()
            '''
            
    def actionsAfterRoll(mode, diceTotal, double):
        mode.didRollAndPassGo(diceTotal, double)
        mode.landOpponentOrTax()
        mode.computer1.doubleRent()
        mode.computer1.propertySort()
        mode.computer2.doubleRent()
        mode.computer2.propertySort()
        mode.checkEndGame()
        
        '''
        print(mode.withinRange(0, 38)) #True
        print(mode.withinRange(0, 28)) #True
        print(mode.withinRange(12, 0)) #True
        print(mode.withinRange(6, 37)) #True
        print(mode.withinRange(6, 34)) #True
        print(mode.withinRange(6, 33)) #False
        print(mode.withinRange(2,0))   #True
        print(mode.withinRange(4, 32)) #True
        print(mode.withinRange(4, 31)) #False
        '''
    def checkEndGame(mode):
        global winner
        if mode.computer1.money < 0:
            winner = mode.computer2
            mode.app.setActiveMode(mode.app.gameOverMode)
        elif mode.computer2.money < 0:
            winner = mode.computer1
            mode.app.setActiveMode(mode.app.gameOverMode)
                    
    def endTurn(mode):
        
        if mode.rollCounter == 1:
            mode.turnCounter += 1
            mode.rollCounter = 0
            if len(mode.announcements) == 5:
                mode.announcements = mode.announcements[1:]
                if mode.turnCounter % 2 == 1:
                    mode.announcements.append('Computer1 ended their turn')
                else:
                    mode.announcements.append('Computer2 ended their turn')
            elif len(mode.announcements) < 5:
                if mode.turnCounter % 2 == 1:
                    mode.announcements.append('Computer1 ended their turn')
                else:
                    mode.announcements.append('Computer2 ended their turn')
            mode.computer1.doubleRent()
            mode.computer1.propertySort()
            mode.computer2.doubleRent()
            mode.computer2.propertySort()
            mode.checkEndGame()
            if mode.turnCounter % 2 == 1:
                mode.monopolyAI()
        
############################  AI Select Spaces  ###################################  

    def propertySelection(mode, x, y):
        #print(mode.nextSelected)
        if mode.nextSelected:
            for space in board:
                if isinstance(space,Property):
                    space.selected = False
                    
            #selection from side 1
            if (x >= 810 - 26.25 and x <= 810 + 26.25 and 
                y >= 628 - 42.5 and y <= 628 + 42.5):
                mediterranean.selected = True
            elif (x >= 705 - 26.25 and x <= 705 + 26.25 and 
                y >= 628 - 42.5 and y <= 628 + 42.5):
                baltic.selected = True
            elif (x >= 547.5 - 26.25 and x <= 547.5 + 26.25 and 
                y >= 628 - 42.5 and y <= 628 + 42.5):
                oriental.selected = True
            elif (x >= 442.5 - 26.25 and x <= 442.5 + 26.25 and 
                y >= 628 - 42.5 and y <= 628 + 42.5):
                vermont.selected = True
            elif (x >= 390 - 26.25 and x <= 390 + 26.25 and 
                y >= 628 - 42.5 and y <= 628 + 42.5):
                connecticut.selected = True
            
            #selection from side 2
            elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
                y >= 560 - 26.25 and y <= 560 + 26.25):
                stCharles.selected = True
            elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
                y >= 455 - 26.25 and y <= 455 + 26.25):
                state.selected = True
            elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
                y >= 402.5 - 26.25 and y <= 402.5 + 26.25):
                virginia.selected = True
            elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
                y >= 297.5 - 26.25 and y <= 297.5 + 26.25):
                stJames.selected = True
            elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
                y >= 192.5 - 26.25 and y <= 192.5 + 26.25):
                tennessee.selected = True
            elif (x >= 320 - 42.5 and x <= 320 + 42.5 and 
                y >= 140 - 26.25 and y <= 140 + 26.25):
                newYork.selected = True
        
            #selection from side 3
            elif (x >= 390 - 26.25 and x <= 390 + 26.25 and 
                y >= 70 - 42.5 and y <= 70 + 42.5):
                kentucky.selected = True
            elif (x >= 495 - 26.25 and x <= 495 + 26.25 and 
                y >= 70 - 42.5 and y <= 70 + 42.5):
                indiana.selected = True
            elif (x >= 547.5 - 26.25 and x <= 547.5 + 26.25 and 
                y >= 70 - 42.5 and y <= 70 + 42.5):
                illinois.selected = True
            elif (x >= 652.5 - 26.25 and x <= 652.5 + 26.25 and 
                y >= 70 - 42.5 and y <= 70 + 42.5):
                atlantic.selected = True
            elif (x >= 705 - 26.25 and x <= 705 + 26.25 and 
                y >= 70 - 42.5 and y <= 70 + 42.5):
                vetnor.selected = True
            elif (x >= 810 - 26.25 and x <= 810 + 26.25 and 
                y >= 70 - 42.5 and y <= 70 + 42.5):
                marvin.selected = True
            
            #selection from side 4
            elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
                y >= 140 - 26.25 and y <= 140 + 26.25):
                pacific.selected = True
            elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
                y >= 192.5 - 26.25 and y <= 192.5 + 26.25):
                northCarolina.selected = True
            elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
                y >= 297.5 - 26.25 and y <= 297.5 + 26.25):
                pennsylvania.selected = True
            elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
                y >= 455 - 26.25 and y <= 455 + 26.25):
                parkPlace.selected = True
            elif (x >= 878 - 42.5 and x <= 878 + 42.5 and 
                y >= 560 - 26.25 and y <= 560 + 26.25):
                boardwalk.selected = True
               
            selected = None
            for space in board:
                if isinstance(space, Property):
                    if space.selected:
                        selected = space
            if selected != None:
                mode.buyHouse(selected)
           
        #print(mode.selectionCounter)
        if mode.selectionCounter >= 1:
            mode.selectionCounter = 0
            mode.nextSelected = False
            
#######################  Monopoly Aritifical Intelligence  #####################

    def expectedValue(mode, space):
        expectedValueResult = 0
        #if where you landed is owned by the opponent, pay rent, so we can add 
        #that to the expected value
        if space in mode.computer1.properties:
            if isinstance(space, Property):
                rent = mode.rentPriceProperty(space, mode.computer1)
                expectedValueResult -= rent
            elif isinstance(space, Utilities):
                rent = mode.rentPriceUtility(space, mode.computer1)
                expectedValueResult -= rent
            elif isinstance(space, Railroad):
                rent = mode.rentPriceRailroad(space)
                expectedValueResult -= rent
        elif isinstance(space, Tax):
            expectedValueResult -= space.tax
        return expectedValueResult
        
    def comboCalculator(mode, n, k):
        return math.factorial(n) / ((math.factorial(k))*(math.factorial(n-k)))
        
    #this function checks whether the positions a and b are within range of 
    #one move, returns an ordered pair of boolean and distance
    #we can let a represent the position of the target space and b represent the 
    #position of the opponent
    def withinRange(mode, a, b):
        if a >= 12 and a < 40:
            if b >= a - 12 and b <= a - 2:
                return (True, a - b)
            else:
                return (False, (a - b) % 40)
        elif a < 12 and a >= 2:
            if b >= 0 and b <= a - 2:
                return (True, a - b)
            elif b <= 39 and b >= (a - 12) % 40:
                return (True, a + 40 - b) 
            else:
                return (False, a - b % 40)
        elif a == 1 or a == 0:
            if b <= (a - 2) % 40 and b >= (a - 12)  % 40:
                return (True, a + 40 - b)
            else:
                return (False, a - b % 40)
    

    def probabilityCalculator(mode, n):
        # n represents how many spaces
        if n == 2 or n == 12:
            return 1 / 6 * 1 / 6
        elif n == 3 or n == 11:
            return 2 * (1 / 6 * 1 / 6)
        elif n == 4 or n == 10:
            return 3 * (1 / 6 * 1 / 6)
        elif n == 5 or n == 9:
            return 4 * (1 / 6 * 1 / 6)
        elif n == 6 or n == 8:
            return 5 * (1 / 6 * 1 / 6)
        elif n == 7:
            return 6 * (1 / 6 * 1 / 6)
    
    def rentHomeCalculator(mode, space, num):
        if num == 1:
            return space.h1
        elif num == 2:
            return space.h2
        elif num == 3:
            return space.h3
        elif num == 4:
            return space.h4
        elif num == 5:
            return space.hotel
            
    def rentAcquiredProperty(mode, space):
        color = space.color
        counter = 0
        computer1Potential = mode.computer1.money
        for prop in mode.computer1.properties:
            if isinstance(prop, Property) and prop.color == color:
                counter += 1
        if color == 'blue' or color == 'brown':
            if computer1Potential >= space.cost:
                computer1Potential -= space.cost
                if counter == 1:
                    houses = computer1Potential // space.houseCost
                    if houses >= 10:
                        return space.hotel
                    elif houses % 2 == 1:
                        boughtHouse = houses // 2 + 1
                        return mode.rentHomeCalculator(space, boughtHouse)
                    else:
                        boughtHouse == houses // 2
                        if boughtHouse == 0:
                            return space.rent * 2
                        else:
                            return mode.rentHomeCalculator(space, boughtHouse)
                else:
                    return space.rent
            return 0
        else:
            if computer1Potential >= space.cost:
                computer1Potential -= space.cost
                if counter == 2:
                    houses = computer1Potential // space.houseCost
                    if houses >= 10:
                        return space.hotel
                    elif houses % 3 == 1 or houses % 3 == 2:
                        boughtHouse = houses // 2 + 1
                        return mode.rentHomeCalculator(space, boughtHouse)
                    else:
                        boughtHouse = houses // 2
                        if boughtHouse == 0:
                            return space.rent * 2
                        else:
                            return mode.rentHomeCalculator(space, boughtHouse)
                else:
                    return space.rent
            return 0
    
    def rentAcquiredUtilities(mode, space, range):
        counter = 0
        for prop in mode.computer1.properties:
            if isinstance(prop, Utilities):
                counter += 1
        computer1Potential = mode.computer1.money
        if computer1Potential >= space.cost:
            computer1Potential -= space.cost
            if counter == 1:
                return 10 * range
            else:
                return 4 * range
        return 0
        
    def rentAcquiredRailroad(mode, space):
        counter = 0
        for prop in mode.computer1.properties:
            if isinstance(prop, Railroad):
                counter += 1
        computer1Potential = mode.computer1.money
        if computer1Potential >= space.cost:
            computer1Potential -= space.cost
            if counter == 1:
                return 50
            elif counter == 2:
                return 100
            elif counter == 3:
                return 200
            else:
                return 25
        return 0
            
    def rentIfAcquired(mode, space, range):
        if isinstance(space,Property):
            return mode.rentAcquiredProperty(space)
        elif isinstance(space, Utilities):
            return mode.rentAcquiredUtilities(space, range)
        elif isinstance(space, Railroad):
            return mode.rentAcquiredRailroad(space)
            
    def potentialLossFromOpponent(mode, position):
        sumExpectedValuePotential = 0
        for n in range(2,13):
            posValue = (position + n) % 40
            space = board[posValue]
            opponentPosValue = mode.computer1.position % 40
            boolRange, distance = mode.withinRange(posValue, opponentPosValue)
            if (isinstance(space, Property) or isinstance(space, Utilities) or 
                isinstance(space, Railroad)) and (space in propertySet):
                #if the space we are looking at is both unowned and a space where rent needs to be paid,
                #we assume that the opponent will buy it and therefore will require us to have some money
                #we now have to check whether or not it will complete a set, and if it does complete a set
                #we assume the worst case and the opponent will buy the maxnumber of houses
                if boolRange:
                    #print(space.name)
                    sumExpectedValuePotential += (mode.probabilityCalculator(distance) * 
                                                  mode.rentIfAcquired(space, distance))
        return sumExpectedValuePotential
                
            
    def sumExpectedValue(mode, position):
        sumExpectedValueResult = 0
        for n in range(2,13):
            space = board[(position + n) % 40]
            if mode.expectedValue(space) >= 50:
                sumExpectedValueResult += mode.expectedValue(space)
            sumExpectedValueResult += (mode.probabilityCalculator(n) * 
                                       mode.expectedValue(space))
        sumExpectedValueResult -= mode.potentialLossFromOpponent(position)
        return sumExpectedValueResult
        
    def secondDepthSumExpectedValue(mode):
        sumSecondExpectedValue = 0
        for n in range(2,13):
            space = board[(mode.computer2.position + n) % 40]
            position = mode.computer2.position + n
            sumSecondExpectedValue += (mode.probabilityCalculator(n) * 
                        (mode.expectedValue(space) + mode.sumExpectedValue(position)))
            #print(space.name)
            #print(f'expected val: {mode.expectedValue(space)}')
            #print(f'sumExpectedVal: {mode.sumExpectedValue(position)}')
            #print(f'Second Depth:{sumSecondExpectedValue}')
        sumSecondExpectedValue += mode.secondDepthMaxPay(mode.computer2.position)
        return sumSecondExpectedValue
        
    def secondDepthMaxPay(mode, position):
        maxVal = 0
        for n in range(2,13):
            space = board[ (position + n) % 40 ]
            expectedPay = mode.expectedValue(space)
            for m in range(2,13):
                secondSpace = board[(position + n + m) % 40]
                secondExpectedPay = mode.expectedValue(secondSpace)
                if secondExpectedPay + expectedPay < maxVal:
                    maxVal = secondExpectedPay + expectedPay
        return maxVal
        
    def AIBuyHouse(mode, color):
        houseBuild = []
        for space in board:
            if isinstance(space, Property):
                if space.color == color:
                    houseBuild.append(space)
        #print(f'houseBuild: {houseBuild}')
        for i in range(5):
            for space in houseBuild:
                if (mode.computer2.money - mode.computer2.critMoney > houseBuild[0].houseCost):
                    mode.buyHouse(space)
                    #print(space.color)
    
    def monopolyAI(mode):
        #list of things my AI needs to do 
        #1. find the expected value change on the next 2 moves 
        #2. find the critical money value held based ont he expected value change
        #3. use the extra money either to buy properties the next 2 rounds or 
        #   buy houses when possible
        mode.rollDice()
        mode.computer2.critMoney = mode.secondDepthSumExpectedValue()
        mode.computer2.critMoney = int(mode.computer.critMoney) - 1
        mode.computer2.critMoney *= -1
        if mode.computer2.money > mode.computer2.critMoney:
            #buy property if you can and have extra money
            space = board[mode.computer2.position % 40]
            if ((isinstance(space, Property) or isinstance(space, Utilities) or 
                 isinstance(space, Railroad)) and 
                 mode.computer2.money - mode.computer2.critMoney > space.cost):
                mode.buyProperty()
            
            #buy houses if you can and have extra money
            #print(mode.computer.colorBuild)
            for element in mode.computer2.colorBuild:
                #print(element)
                mode.AIBuyHouse(element)
        mode.endTurn()
        print(f'AI Turn Counter: {mode.turnCounter}')
            
        

###############################  User Input  ################################### 

    def mousePressed(mode, event):
        mode.selectionCounter += 1
        #pressed buy property button
        if (event.x >= 140 - 85 and event.x <= 140 + 85 and 
            event.y >= 490 and event.y <= 530 
            and mode.turnCompletedComputer1 and mode.turnCompletedComputer2):
            mode.buyProperty()
            print('you pressed the buy property button')
            
        #pressed roll dice button
        if (event.x >= 205 - 63 and event.x <= 205 + 63 and 
            event.y >= 420 and event.y <= 460
            and mode.turnCompletedComputer1 and mode.turnCompletedComputer2):
            print('you pressed the roll dice button')
            mode.communityChanceMessage = ''
            mode.rollDice()
            
        #pressed end turn button
        if (event.x >= 140-64 and event.x <= 140 + 64 and 
            event.y >= 630 and event.y <= 670
            and mode.turnCompletedComputer1 and mode.turnCompletedComputer2):
            mode.endTurn()
            mode.animationSkip = False
            print('you pressed the end turn button')
            
        #pressed buy house button
        if (event.x >= 140-72 and event.x <= 140+72 and 
            event.y >= 560 and event.y <= 600
            and mode.turnCompletedComputer1 and mode.turnCompletedComputer2):
            
            mode.selectionCounter = 0
            mode.nextSelected = True
            print('you pressed the buyHouse button')
            
        #property selection
        mode.propertySelection(event.x, event.y)
        for space in board:
            if isinstance(space, Property):
                if space.selected == True:
                    print(f'{space.name} is selected') 
            

    def keyPressed(mode, event):
        if event.key == 'h':
            mode.app.setActiveMode(mode.app.helpMode)
        
    def timerFired(mode):
        mode.counterDrawComputer1 += 1
        mode.counterDrawComputer2 += 1
        '''
        if mode.turnCounter % 2 == 1:
            mode.counterDrawcomputer1 += 1
        else:
            mode.counterDrawComputer += 1
        '''
############################  AI Draw Functions  ###############################
        
    def drawComputer1Path(mode,canvas,x,y):
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill = 'blue')
        
    def drawComputer2Path(mode,canvas,x,y):
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill = 'green')
        
    def drawComputer1(mode, canvas, computer1):
        position = computer1.position % 40
        if mode.tempPositionComputer1 % 40 == position:
            mode.turnCompletedComputer1 = True
        if mode.counterDrawComputer1 % 4 == 0 and not mode.turnCompletedComputer1:
            mode.tempPositionComputer1 += 1
        (x, y) = mode.computer1Locations[mode.tempPositionComputer1 % 40]
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill = 'blue')
        #print(f'temp: {mode.tempPositioncomputer1}')
        #print(f'position: {position}')
        #print(f'counterDrawPlayer: {mode.counterDrawPlayer}')
        
    def drawComputer2(mode, canvas, computer2):
        position = computer2.position % 40
        if mode.tempPositionComputer2 % 40 == position:
            mode.turnCompletedComputer2 = True
        if mode.counterDrawComputer2 % 4 == 0 and not mode.turnCompletedComputer2:
            mode.tempPositionComputer2 += 1
        (x, y) = mode.computer2Locations[mode.tempPositionComputer2 % 40]
        canvas.create_rectangle(x-5,y-5,x+5,y+5, fill = 'green')
        
    def drawComputer1Values(mode, canvas, computer1):
        canvas.create_rectangle(930,10,1190, 345)
        canvas.create_rectangle(940, 20, 1180, 60, fill = fill)
        canvas.create_text(1060,40,text = (f'Player 1'), font = 'Arial, 18')
        canvas.create_text(940, 80, text = (f'Money: ${computer1.money}'), anchor = 'w')
        canvas.create_text(1066, 80, text = (f'Last Trans: {computer1.lastTransaction}'), 
                           anchor = 'w')
        canvas.create_text(950,100,text = 'Properties:', anchor = 'w')
        canvas.create_text(1076,100, text = 'Houses:', anchor = 'w')
        counter = 0
        r = 4
        for element in computer1.properties:
            canvas.create_text(950, 130 + (18 * counter), text = element.name, anchor = 'w')
            if isinstance(element, Property):
                for circleCounter in range(5):
                    if circleCounter == element.numHouse - 1 and circleCounter == 4:
                        canvas.create_oval(1080-r + (20 * circleCounter),130 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 130 + r + (18 * counter),
                                        fill = 'red')
                    elif circleCounter <= element.numHouse - 1:
                        canvas.create_oval(1080-r + (20 * circleCounter),130 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 130 + r + (18 * counter),
                                        fill = 'green')
                    else:
                        canvas.create_oval(1080-r + (20 * circleCounter),130 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 130 + r + (18 * counter))
            counter += 1
        
    def drawComputer2Values(mode, canvas, computer2):
        canvas.create_rectangle(930, 355, 1190, 690)
        canvas.create_rectangle(940, 365, 1180, 405, fill = fill)
        canvas.create_text(1060,385,text = (f'Computer2'), font = 'Arial, 18')
        canvas.create_text(940, 425, text = (f'Money: ${computer2.money}'), anchor = 'w')
        canvas.create_text(1066, 425, text = (f'Last Trans: {computer2.lastTransaction}'), 
                           anchor = 'w')
        canvas.create_text(950,445,text = 'Properties:', anchor = 'w')
        canvas.create_text(1076,445, text = 'Houses:', anchor = 'w')
        counter = 0
        r = 4
        for element in computer2.properties:
            canvas.create_text(950, 475 + (18 * counter), text = element.name, anchor = 'w')
            if isinstance(element, Property):
                for circleCounter in range(5):
                    if circleCounter == element.numHouse - 1 and circleCounter == 4:
                        canvas.create_oval(1080-r + (20 * circleCounter),475 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 475 + r + (18 * counter),
                                        fill = 'red')
                    elif circleCounter <= element.numHouse - 1:
                        canvas.create_oval(1080-r + (20 * circleCounter),475 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 475 + r + (18 * counter),
                                        fill = 'green')
                    else:
                        canvas.create_oval(1080-r + (20 * circleCounter),475 - r + (18 * counter), 
                                        1080 + r + (20 * circleCounter), 475 + r + (18 * counter))
            counter += 1
        '''
        canvas.create_text(1075,200,text = (
                           f'computer money:{mode.computer.money}'))
        canvas.create_text(1075,220,text = 'properties')
        counter = 0
        for element in computer.properties:
            canvas.create_text(940, 240 + (20 * counter), text = element.name, anchor = 'w')
            counter += 1
        
        '''   
     
    def drawDice(mode, canvas):
        (dice1, dice2) = mode.dice
        canvas.create_rectangle(20, 410, 125, 470, fill = fill)
        #canvas.create_text(45, 400, text = 'Dice:', font = 'Arial, 22')
        if dice1 == 1:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceOne))
        elif dice1 == 2:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceTwo))
        elif dice1 == 3:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceThree))
        elif dice1 == 4:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceFour))
        elif dice1 == 5:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceFive))
        elif dice1 == 6:
            canvas.create_image(50,440, image = ImageTk.PhotoImage(mode.diceSix))
        if dice2 == 1:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceOne))
        elif dice2 == 2:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceTwo))
        elif dice2 == 3:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceThree))
        elif dice2 == 4:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceFour))
        elif dice2 == 5:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceFive))
        elif dice2 == 6:
            canvas.create_image(95,440, image = ImageTk.PhotoImage(mode.diceSix))
        
        
        
        
    def drawTurn(mode, canvas):
        canvas.create_rectangle(50, 140, 230, 180, fill = fill)
        canvas.create_text(90, 160, text = 'Turn:', font = 'Arial 22')
        if mode.turnCounter % 2 == 0:
            canvas.create_text(180, 160, text = 'Computer1', font = 'Arial 20')
        else:
            canvas.create_text(180, 160, text = 'Computer2', font = 'Arial 20')
        
        
    def drawHouse(mode, canvas):
        spaceIndex = 0
        for property in housePosition:
            if property != None:
                counter = 0
                if board[spaceIndex].numHouse == 5:
                    space = board[spaceIndex]
                    x, y = property[1]
                    if space.color == 'brown' or space.color == 'grey':
                        canvas.create_rectangle(x - 4.5, y - 4.5, x + 16.5, 
                                                y + 4.5, fill = 'red')
                    elif space.color == 'pink' or space.color == 'orange':
                        canvas.create_rectangle(x - 4.5, y - 4.5, x + 4.5, 
                                                y + 16.5, fill = 'red')
                    elif space.color == 'red' or space.color == 'yellow':
                        canvas.create_rectangle(x - 16.5, y - 4.5, x + 4.5, 
                                                y + 4.5, fill = 'red')
                    elif space.color == 'green' or space.color == 'blue':
                        canvas.create_rectangle(x - 4.5, y - 16.5, x + 4.5, 
                                                y + 4.5, fill = 'red')
                else:
                    for houseCoor in property:
                        if counter < board[spaceIndex].numHouse and counter < 4:
                            x, y = houseCoor
                            canvas.create_rectangle(x-4.5,y-4.5,x+4.5,y+4.5,fill = 'green')
                        counter += 1
            spaceIndex += 1

    def drawPropArea(mode, canvas):
        for pair in coorSide1:
            x,y = pair
            canvas.create_rectangle(x - 26.25, y - (42.5), 
                                    x + 26.25, y + (42.5), fill = 'red')
                                    
        for pair in coorSide2:
            x,y = pair
            canvas.create_rectangle(x-42.5, y-26.25, x+42.5, y+26.25, fill = 'red')
        
        for pair in coorSide3:
            x,y = pair
            canvas.create_rectangle(x - 26.25, y - (42.5), 
                                    x + 26.25, y + (42.5), fill = 'red')
        
        for pair in coorSide4:
            x,y = pair
            canvas.create_rectangle(x-42.5, y-26.25, x+42.5, y+26.25, fill = 'red')
            
    def drawAnnouncements(mode, canvas):
        counter = 0
        canvas.create_rectangle(10, 210, 270, 380, fill = fill)
        canvas.create_text(140, 230, text = 'Announcements:', font = 'Arial, 20')
        for message in mode.announcements:
            canvas.create_text(140, 260 + 25 * counter, text = message, font = 'Arial 16')
            counter += 1
            
    def drawCommunityChanceMessage(mode, canvas):
        canvas.create_rectangle(215, 675, 920, 708, fill = fill)
        canvas.create_text(225, 691.5, text = 'Community Chest or Chance Message:' ,anchor = 'w')
        canvas.create_text(480, 691.5, text = f'{mode.communityChanceMessage}', anchor = 'w')
        
    

    def redrawAll(mode, canvas):
        #draw turn
        mode.drawTurn(canvas)
        
        #draw logo
        canvas.create_image(140, 65, image = ImageTk.PhotoImage(mode.logo))
        
        #draw board
        canvas.create_image(600, 350,
                            image=ImageTk.PhotoImage(mode.board))
                            
        #draw buy property button 
        canvas.create_image(140, 510, image =
                            ImageTk.PhotoImage(mode.buy))
                            
        #draw end turn button
        canvas.create_image(140, 650, image = 
                            ImageTk.PhotoImage(mode.turn))
                            
        #draw roll dice button
        canvas.create_image(205, 440, image = 
                            ImageTk.PhotoImage(mode.roll))
                            
        #draw buy house button
        canvas.create_image(140, 580, image = 
                            ImageTk.PhotoImage(mode.buyHouseButton))
        
        #draw players
        mode.drawComputer1(canvas, mode.computer1)
        mode.drawComputer2(canvas, mode.computer2)
        
        #draw players values
        mode.drawComputer1Values(canvas, mode.computer1)
        mode.drawComputer2Values(canvas, mode.computer2)
        
        #finding coordinates for houses
        
        mode.drawHouse(canvas)
        #mode.drawPropArea(canvas)
        
        canvas.create_text(mode.width / 2, mode.height / 2, text = 'THIS IS THE AI MODE', font = 'Arial 50 bold')
        mode.drawAnnouncements(canvas)
        
        mode.drawDice(canvas)
        
        mode.drawCommunityChanceMessage(canvas)
        
        #print(mode.secondDepthSumExpectedValue())
        #print(mode.sumExpectedValue(baltic))
        
        
        '''
        #help find player location on the board
        for location in mode.computer1Locations:
            (xcor, ycor) = location
            mode.drawcomputer1Path(canvas,xcor,ycor)
            
        for location in mode.computerLocations:
            h(xcor, ycor) = location
            mode.drawcomputerPath(canvas,xcor,ycor)
        '''

##############################  Help Mode Setup  ############################### 

class HelpMode(Mode):
    def appStarted(mode):
        mode.counter = 0
        #this is for the background
        background = 'splash2.png'
        mode.background = mode.loadImage(background)
        mode.background = mode.scaleImage(mode.background, .5)
        mode.timerDelay = 1
        mode.rules1 = mode.loadImage('rules1.png')
        mode.rules1 = mode.scaleImage(mode.rules1, .5)
        mode.rules2 = mode.loadImage('rules2.png')
        mode.rules2 = mode.scaleImage(mode.rules2, .5)
     
        
    def timerFired(mode):
        mode.counter += 1
        
    def redrawAll(mode, canvas):
        font = 'Arial 60 bold'
        font1 = 'Arial 24 bold'
        #background color
        canvas.create_rectangle(0,0,mode.width, mode.height, fill = '#D5EFB5')

        #left side rule book
        canvas.create_rectangle(50,50,mode.width / 2 - 49, mode.height - 49, fill = 'white')
        canvas.create_image(301, 358, image=ImageTk.PhotoImage(mode.rules1))
        
        
        
        #right side rule book
        canvas.create_rectangle(mode.width / 2 + 50,50,mode.width - 49, mode.height - 49, fill = 'white')
        canvas.create_image(901, 358, image=ImageTk.PhotoImage(mode.rules2))
        
        #canvas.create_text(mode.width/2, 250, text='(Rules will be put here)', font=font)
       
        canvas.create_rectangle(mode.width / 4 - 166, 657, mode.width / 4 + 166, 693, 
                                fill = 'white', outline = 'red', width = 2)
        if (mode.counter // 12) % 2 == 0:
            canvas.create_text(mode.width / 4, 675, text='Press "a" for the AI Mode!', 
                               fill = 'red', font=font1)
                               
        canvas.create_rectangle(3  * mode.width / 4 - 206, 657, 3 * mode.width / 4 + 206, 693, 
                                fill = 'white', outline = 'red', width = 2)
        if (mode.counter // 12) % 2 == 0:
            canvas.create_text(3 * mode.width / 4, 675, text='Press "space" for the Two Player!', 
                               fill = 'red', font=font1)
 

    def keyPressed(mode, event):
        if event.key == 'a':
            mode.app.setActiveMode(mode.app.AIMode)
        elif event.key == 'Space':
            mode.app.setActiveMode(mode.app.gameMode)
        
############################  Game Over Mode  ##################################

class GameOverMode(Mode):
    def appStarted(mode):
        mode.gameOver = True
        
    def redrawAll(mode,canvas):
        global winner
        canvas.create_rectangle(0,0,mode.width, mode.height, fill = fill)
        canvas.create_text(mode.width / 2, mode.height / 2, text = f'{winner.name} Wins!', font = 'Arial 40')
        
############################  Modal App Setup  ################################# 

class MyModalApp(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.gameOverMode = GameOverMode()
        app.AIMode = AIMode()
        app.AIAIMode = AIAIMode()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 50

app = MyModalApp(width=1200, height=714)