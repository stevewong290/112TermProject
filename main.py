from cmu_112_graphics import *
from tkinter import *
import random, math, copy, string, time

class Player(object):
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0
        self.properties = []

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
        





class SplashScreenMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2, 150, text='This demos a ModalApp!', font=font)
        canvas.create_text(mode.width/2, 200, text='This is a modal splash screen!', font=font)
        canvas.create_text(mode.width/2, 250, text='Press any key for the game!', font=font)

    def keyPressed(mode, event):
        if (event.key == 'h'):
            mode.app.setActiveMode(mode.app.helpMode)
        else:
            mode.app.setActiveMode(mode.app.gameMode)

class GameMode(Mode):
    def appStarted(mode):
        mode.player1 = Player('Player 1')
        mode.player2 = Player('Player 2')
        
        #turn counter
        #if divisible by 2 then it is player 2's turn
        mode.turnCounter = 0
        
        #this is the board image that we are uploading
        board = ('https://i.imgur.com/VmStLDi.jpg')
        mode.board = mode.loadImage(board)
        
        #this is the buy button that we are uploading
        buyButton = ('https://i.imgur.com/yu2NQTg.png')
        mode.buy = mode.loadImage(buyButton)
        
        #this is the end turn button
        turnButton = ('https://i.imgur.com/sffBHbo.png')
        mode.turn = mode.loadImage(turnButton)
        
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
        
    def buyProperty(mode):
        #player 1 turn
        if mode.turnCounter % 2 == 1:
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

   
    def doMove(mode):
        dice1, dice2 = mode.diceRoll()
        #this implements moving the player and tracking whether or not it 
        #passed or landed on go
        if mode.turnCounter % 2 == 1:
            prev = mode.player1.position // 40
            mode.player1.position += (dice1 + dice2)
            newPos = mode.player1.position // 40
            if mode.player1.position % 40 == 0:
                mode.player1.money += 400
            elif prev != newPos:
                mode.player1.money += 200
        else:
            prev = mode.player2.position // 40
            mode.player2.position += (dice1 + dice2)
            newPos = mode.player2.position // 40
            if mode.player2.position % 40 == 0:
                mode.player2.money += 400
            elif prev != newPos:
                mode.player2.money += 200
        

    def timerFired(mode):
        pass

    def mousePressed(mode, event):
        #pressed buy button
        if (event.x >= mode.width - 180 and event.x <= mode.width - 10 and 
            event.y >= 10 and event.y <= 50):
            mode.buyProperty()
            print('you pressed the buy button')
            
        #pressed end turn button
        if (event.x >= mode.width - 138 and event.x <= mode.width - 10 and 
            event.y >= 60 and event.y <= 100):
            mode.turnCounter += 1
            print('you pressed the end turn button')
            mode.doMove()
            print(mode.turnCounter)
            

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
        canvas.create_text(125,150,text = (
                           f'player 1 money:{mode.player1.money}'))
        canvas.create_text(125,170,text = 'properties')
        counter = 0
        for element in player1.properties:
            canvas.create_text(125, 190 + (20 * counter), text = element.name)
            counter += 1
        
    def drawPlayer2Values(mode, canvas, player2):
        canvas.create_text(1075,150,text = (
                           f'player 2 money:{mode.player2.money}'))
        canvas.create_text(1075,170,text = 'properties')
        counter = 0
        for element in player2.properties:
            canvas.create_text(1075, 190 + (20 * counter), text = element.name)
            counter += 1
        
    
    '''    
    def drawDice(mode, canvas, twodice):
        (dice1, dice2) = twodice
        if dice1 == 1:
    '''
    
    def drawTurn(mode, canvas):
        if mode.turn % 2 == 1:
            print("Player 1's turn")   
        else:
            print("Player 2's turn")
        
    

    def redrawAll(mode, canvas):
        #draw board
        canvas.create_image(mode.width / 2,mode.height / 2,
                            image=ImageTk.PhotoImage(mode.board))
        #draw buy button 
        canvas.create_image(mode.width - 95, 30, image =
                            ImageTk.PhotoImage(mode.buy))
                            
        #draw turn button
        canvas.create_image(mode.width - 74, 80, image = 
                            ImageTk.PhotoImage(mode.turn))
        
        #draw players
        mode.drawPlayer1(canvas, mode.player1)
        mode.drawPlayer2(canvas, mode.player2)
        
        #draw players values
        mode.drawPlayer1Values(canvas, mode.player1)
        mode.drawPlayer2Values(canvas, mode.player2)
        
        
        
        
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