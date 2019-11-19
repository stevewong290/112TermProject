from cmu_112_graphics import *
from tkinter import *
import random, math, copy, string, time

class Player(object):
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []
        self.numRailroads = 0
        self.inJail = False
        self.jailCounter = 0
        self.colorBuild = []

    def numRail(self):
        counter = 0
        for property in self.properties:
            if ininstance(property, Railroad):
                counter += 1
        self.numRailroads = counter
    
    def doubleRent(self):
        #brown properties
        if mediterranean in self.properties and baltic in self.properties:
            self.colorBuild.append('brown')
            mediterranean.double = True
            baltic.double = True
        else:
            mediterranean.double = False
            baltic.double = False
        #grey properties
        if (oriental in self.properties and vermont in self.properties and 
              connecticut in self.properties):
            self.colorBuild.append('grey')
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
            self.colorBuild.append('pink')
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
            self.colorBuild.append('orange')
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
            self.colorBuild.append('red')
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
            self.colorBuild.append('yellow')
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
            self.colorBuild.append('green')
            pacific.double = True
            northCarolina.double = True
            pennsylvania.double = True
        else:
            pacific.double = False
            northCarolina.double = False
            pennsylvania.double = False
        #blue properties
        if (parkPlace in self.properties and boardwalk in self.properties):
            self.colorBuild.append('blue')
            parkPlace.double = True
            boardwalk.double = True
        else:
            parkPlace.double = False
            boardwalk.double = False
        #utilities
        if (electric in self.properties and water in self.properties):
            electric.double = True
            water.double = True
        else:
            electric.double = False
            water.double = False
            
            
            
class Property(object):
    def __init__(self, name, cost, rent, h1, h2, h3, h4, hotel, houseCost):
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
        
class Railroad(object):
    def __init__(self, name):
        self.name = name
        self.cost = 200
        self.r1 = 25
        self.r2 = 50
        self.r3 = 100
        self.r4 = 200
        
class CommunityChance(object):
    def __init__(self, name):
        self.name = name

class CornerSpace(object):
    def __init__(self, name):
        self.name = name

class Tax(object):
    def __init__(self, name, tax):
        self.name = name
        self.tax = tax
        
class Utilities(object):
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.double = False

        
    

#instantiated properties        
mediterranean = Property('Mediterranean Avenue', 60, 2, 10, 30, 90, 160, 250, 50)
baltic = Property('Baltic Avenue', 60, 4, 20, 60, 180, 320, 450, 50)
oriental = Property('Oriental Avenue', 100, 6, 30, 90, 270, 400, 550, 50)
vermont = Property('Vermont Avenue', 100, 6, 30, 90, 270, 400, 550, 50)
connecticut = Property('Connecticut Avenue', 120, 8, 40, 100, 300, 450, 600, 50)
stCharles = Property('St. Charles Place', 140, 10, 50, 150, 450, 625, 750, 100)
state = Property('State Avenue', 140, 10, 50, 150, 450, 625, 750, 100)
virginia = Property('Virginia Avenue', 160, 12, 60, 180, 500, 700, 900, 100)
stJames = Property('St. James Place', 180, 14, 70, 200, 550, 750, 950, 100)
tennessee = Property('Tennessee Avenue', 180, 14, 70, 200, 550, 750, 950, 100)
newYork = Property('New York Avenue', 200, 16, 80, 220, 600, 800, 1000, 100)
kentucky = Property('Kentucky Avenue', 220, 18, 90, 250, 700, 875, 1050, 150)
indiana = Property('Indiana Avenue', 220, 18, 90, 250, 700, 875, 1050, 150)
illinois = Property('Illinois Avenue', 240, 20, 100, 300, 750, 925, 1100, 150)
atlantic = Property('Atlantic Avenue', 260, 22, 110, 330, 800, 975, 1150, 150)
vetnor = Property('Vetnor Avenue', 260, 22, 110, 330, 800, 975, 1150, 150)
marvin = Property('Marvin Avenue', 280, 24, 120, 360, 850, 1025, 1200, 150)
pacific = Property('Pacific Avenue', 300, 26, 130, 390, 900, 1100, 1275, 200)
northCarolina = Property('North Carolina Avenue', 300, 26, 130, 390, 900, 1100, 1275, 200)
pennsylvania = Property('Pennsylvania Avenue', 320, 28, 150, 450, 1000, 1200, 1400, 200)
parkPlace = Property('Park Place',350, 35, 175, 500, 1100, 1300, 1500, 200)
boardwalk = Property('Boardwalk', 400, 50, 200, 600, 1400, 1700, 2000, 200)

#instantiated railroads
readingRail = Railroad('Reading Railroad')
pennsylvaniaRail = Railroad('Pennsylvania Railroad')
boRail= Railroad('B & O Railroad')
shortRail = Railroad('Short Line')

#instantiated utilities
electric = Utilities('Electric Company', 150)
water = Utilities('Water Works', 150)

#instantiated corner spaces
passGo = CornerSpace('Pass Go')
jailCell = CornerSpace('Jail Cell')
freeParking = CornerSpace('Free Parking')
goToJail = CornerSpace('Go To Jail')

#instantiated community chest / chance spaces
communitySide1 = CommunityChance('Community Chest Side 1')
communitySide2 = CommunityChance('Community Chest Side 2')
communitySide4 = CommunityChance('Community Chest Side 4')
chanceSide1 = CommunityChance('Community Chest Side 1')
chanceSide3 = CommunityChance('Community Chest Side 3')
chanceSide4 = CommunityChance('Community Chest Side 4')

#instantiated tax space
incomeTax = Tax('Income Tax', 200)
luxuryTax = Tax('Luxury Tax', 100)


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
        
#brown houses
mediterraneanHouse = []
for house in range(4):
    mediterraneanHouse.append((791 + 12 * house, 595))
    
balticHouse = []    
for house in range(4):
    balticHouse.append((686 + 12 * house, 595))
    
orientalHouse = []
for house in range(4):
    orientalHouse.append((529.5 + 12 * house, 595))
    
vermontHouse = []
for house in range(4):
    vermontHouse.append((424.5 + 12 * house, 595))
    
connecticutHouse = []
for house in range(4):
    connecticutHouse.append((372 + 12 * house, 595))
     
stCharlesHouse = []
for house in range(4):
    stCharlesHouse.append((352, 542 + 12 * house))
    
stateHouse = []
for house in range(4):
    stateHouse.append((352, 437 + 12 * house))
    
viriginiaHouse = []
for house in range(4):
    stateHouse.append((352, 384.5 + 12 * house))
    
stJamesHouse = []
for house in range(4):
    stJamesHouse.append((352, 279.5 + 12 * house))
    
tennesseeHouse = []
for house in range(4):
    tennesseeHouse.append((352, 174.5 + 12 * house))
    
newYorkHouse = []
for house in range(4):
    newYorkHouse.append((352, 122 + 12 * house))
    
kentuckyHouse = []
for house in range(4):
    kentuckyHouse.append((408 - 12 * house, 102))
    
indianaHouse = []
for house in range(4):
    indianaHouse.append((513 - 12 * house, 102))
    
illinoisHouse = []
for house in range(4):
    illinoisHouse.append((565.5 - 12 * house, 102))
    
atlanticHouse = []
for house in range(4):
    atlanticHouse.append((670.5 - 12 * house, 102))
    
vetnorHouse = []
for house in range(4):
    vetnorHouse.append((723 - 12 * house, 102))
    
marvinHouse = []
for house in range(4):
    marvinHouse.append((828 - 12 * house, 102))
    
pacificHouse = []
for house in range(4):
    pacificHouse.append((845, 157 - 12 * house))
    
northCarolinaHouse = []
for house in range(4):
    northCarolinaHouse.append((845, 209.5 - 12 * house))
    
pennsylvaniaHouse = []
for house in range(4):
    pennsylvaniaHouse.append((845, 314.5 - 12 * house))
    
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
housePosition.append(viriginiaHouse)
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

numHouse = [None, 0, None, 0, None, None, 0, None, 0, 0, None, 0, None, 0, 0, 
            None, 0, None, 0, 0, None, 0, None, 0, 0, None, 0, 0, None, 0, 
            None, 0, 0, None, 0, None, None, 0, None, 0]








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
        print(mode.counter)
        
    def redrawAll(mode, canvas):
        font = 'Arial 60 bold'
        font1 = 'Arial 24 bold'
        canvas.create_rectangle(0,0,mode.width, mode.height, fill = '#D5EFB5')
        canvas.create_image(600, 250, image = ImageTk.PhotoImage(mode.background))
        canvas.create_rectangle(mode.width / 2 - 166, 532, mode.width / 2 + 166, 568, 
                                fill = 'white', outline = 'red', width = 2)
        if (mode.counter // 8) % 2 == 0:
            canvas.create_text(mode.width/2, 550, text='Press any key for the game!', 
                               fill = 'red', font=font1)

                           

    def keyPressed(mode, event):
        if (event.key == 'h'):
            mode.app.setActiveMode(mode.app.helpMode)
        else:
            mode.app.setActiveMode(mode.app.gameMode)

class GameMode(Mode):
    def appStarted(mode):
        mode.player1 = Player('Player 1')
        mode.player2 = Player('Player 2')
        
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
        
        #THESE ARE THE POSSIBLE LOCATIONS OF PLAYER 2
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
        
    def buyProperty(mode):
        #player 1 turn
        if mode.turnCounter % 2 == 0:
            space = board[mode.player1.position % 40]
            if space in propertySet: 
                if mode.player1.money >= space.cost:
                    mode.player1.money -= space.cost
                    mode.player1.properties.append(space)
                    propertySet.remove(space)
        #player 2 turn
        else:
            space = board[mode.player2.position % 40]
            if space in propertySet: 
                if mode.player2.money >= space.cost:
                    mode.player2.money -= space.cost
                    mode.player2.properties.append(space)
                    propertySet.remove(space)
                    
    #this function takes in a property and returns how much to pay
    def rentPriceProperty(mode, property):
        if property.numHouse == 0:
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
                elif isinstance(space, Utility):
                    rent = mode.rentPriceUtility(space)
                    mode.player1.money -= rent
                    mode.player2.money += rent
                elif isinstance(space, Railroad):
                    rent = mode.rentPriceRailroad(space)
                    mode.player1.money -= rent
                    mode.player2.money += rent
            elif isinstance(space, Tax):
                mode.player1.money -= space.tax
        else:
            #redefine location as space
            space = board[mode.player2.position % 40]
            #if where you landed is owned by the opponent, pay rent
            if space in mode.player1.properties:
                if isinstance(space, Property):
                    rent = mode.rentPriceProperty(space)
                    mode.player2.money -= rent
                    mode.player1.money += rent
                elif isinstance(space, Utility):
                    rent = mode.rentPriceUtility(space)
                    mode.player2.money -= rent
                    mode.player1.money += rent
                elif isinstance(space, Railroad):
                    rent = mode.rentPriceRailroad(space)
                    mode.player2.money -= rent
                    mode.player1.money += rent
            elif isinstance(space, Tax):
                mode.player2.money -= space.tax
   
    def rollDice(mode):
        if mode.rollCounter == 0:
            mode.rollCounter += 1
            dice1, dice2 = mode.diceRoll()
            double = False
            if dice1 == dice2:
                double == True
            #stores the previous dice in the app
            mode.prevRoll = dice1 + dice2
            diceTotal = dice1 + dice2
            mode.didRollAndPassGo(diceTotal, double)
            
            mode.landOpponentOrTax()
    
                    
    def endTurn(mode):
        if mode.rollCounter == 1:
            mode.turnCounter += 1
            mode.rollCounter = 0
        mode.player1.doubleRent()
        mode.player2.doubleRent()
        

    def timerFired(mode):
        pass

    def mousePressed(mode, event):
        #pressed buy button
        if (event.x >= mode.width - 180 and event.x <= mode.width - 10 and 
            event.y >= 10 and event.y <= 50):
            mode.buyProperty()
            print('you pressed the buy button')
            
        #pressed roll dice button
        if (event.x >= mode.width - 136 and event.x <= mode.width - 10 and 
            event.y >= 60 and event.y <= 100):
            print('you pressed the roll dice button')
            mode.rollDice()
            
        #pressed end turn button
        if (event.x >- mode.width - 138 and event.x <= mode.width - 10 and 
            event.y >= mode.height - 50 and event.y <= mode.height - 10):
            mode.endTurn()
            print('you pressed the end turn button')
            

    def keyPressed(mode, event):
        pass
        
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
        canvas.create_text(125,200,text = (
                           f'player 1 money:{mode.player1.money}'))
        canvas.create_text(125,220,text = 'properties')
        counter = 0
        for element in player1.properties:
            canvas.create_text(125, 240 + (20 * counter), text = element.name)
            counter += 1
        
    def drawPlayer2Values(mode, canvas, player2):
        canvas.create_text(1075,200,text = (
                           f'player 2 money:{mode.player2.money}'))
        canvas.create_text(1075,220,text = 'properties')
        counter = 0
        for element in player2.properties:
            canvas.create_text(1075, 240 + (20 * counter), text = element.name)
            counter += 1
            
    def drawCommunityChance(mode, canvas):
        pass
        
    #this draw function runs through the entire board and checks whether or not 
    #it is a property; then it draws the number of houses there is. 

                
        
    
    '''    
    def drawDice(mode, canvas, twodice):
        (dice1, dice2) = twodice
        if dice1 == 1:
    '''
    
    def drawTurn(mode, canvas):
        canvas.create_text(125, 150, text = 'Turn:')
        if mode.turnCounter % 2 == 0:
            canvas.create_text(125, 170, text = 'Player 1')
        else:
            canvas.create_text(125, 170, text = 'Player 2')
        
        
    def drawHouse(mode, canvas):
        for property in housePosition:
            if property != None:
                for houseCoor in property:
                    x, y = houseCoor
                    canvas.create_rectangle(x-4.5,y-4.5,x+4.5,y+4.5,fill = 'green')
            
        
    

    def redrawAll(mode, canvas):
        #draw turn
        mode.drawTurn(canvas)
        
        #draw logo
        canvas.create_image(140, 65, image = ImageTk.PhotoImage(mode.logo))
        
        #draw board
        canvas.create_image(mode.width / 2,mode.height / 2,
                            image=ImageTk.PhotoImage(mode.board))
        #draw buy button 
        canvas.create_image(mode.width - 95, 30, image =
                            ImageTk.PhotoImage(mode.buy))
                            
        #draw turn button
        canvas.create_image(mode.width - 74, mode.height - 30, image = 
                            ImageTk.PhotoImage(mode.turn))
                            
        #draw roll dice button
        canvas.create_image(mode.width - 73, 80, image = 
                            ImageTk.PhotoImage(mode.roll))
        
        #draw players
        mode.drawPlayer1(canvas, mode.player1)
        mode.drawPlayer2(canvas, mode.player2)
        
        #draw players values
        mode.drawPlayer1Values(canvas, mode.player1)
        mode.drawPlayer2Values(canvas, mode.player2)
        
        #finding coordinates for houses
        
        mode.drawHouse(canvas)
        
        
        
        '''
        #help find player location on the board
        for location in mode.player1Locations:
            (xcor, ycor) = location
            mode.drawPlayer1Path(canvas,xcor,ycor)
            
        for location in mode.player2Locations:
            (xcor, ycor) = location
            mode.drawPlayer2Path(canvas,xcor,ycor)
        '''

class HelpMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2, 150, text='This is the help screen!', font=font)
        canvas.create_text(mode.width/2, 250, text='(Insert helpful message here)', font=font)
        canvas.create_text(mode.width/2, 350, text='Press any key to return to the game!', font=font)

    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.gameMode)

class MyModalApp(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 50

app = MyModalApp(width=1200, height=700)