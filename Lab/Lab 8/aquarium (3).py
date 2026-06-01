'''
Name(s):My, Eliana
CSC 201
Lab 8

The program displays a virtual aquarium with animated fish and floating bubbles.
It utilizes a Fish and Bubble class.

Did you complete this lab file during the class period (yes or no)?

If no, leave the one that applies. If yes, delete this entire section!
    I completed aquarium.py without my partner from class.
    I completed aquarium_game.py with my partner from class.

    Document any assistance you get if you complete the lab after the class period:
    
'''

from graphics2 import *
import random
import time

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
DEFAULT_FISH_NUM = 10
DEFAULT_BUBBLE_NUM = 25
MAX_COLOR_NUM = 255

#***********
# FISH CLASS
#***********

class Fish:
    def __init__(self, x, y, speed, color):  
        self.speed = speed
        self.body = Oval(Point(x-30, y-20), Point(x+30, y+20))
        self.tail = Oval(Point(x-25, y-30), Point(x-15, y+30))
        self.eye = Circle(Point(x+15, y-5), 3)
        
        self.body.setFill(color)
        self.tail.setFill(color)
        self.eye.setFill('white')
        

    def draw(self, window):
        self.tail.draw(window)
        self.body.draw(window)
        self.eye.draw(window)
    
    def move(self):
        self.body.move(-self.speed, 0)
        if self.body.getCenter().getX() > WINDOW_WIDTH:
             self.body.move(-WINDOW_WIDTH - 5, 0)
             
        self.tail.move(-self.speed, 0)
        if self.tail.getCenter().getX() > WINDOW_WIDTH:
             self.tail.move(-WINDOW_WIDTH - 5, 0)
             
        self.eye.move(-self.speed, 0)
        if self.eye.getCenter().getX() > WINDOW_WIDTH:
             self.eye.move(-WINDOW_WIDTH - 5, 0)
    
#*************
# BUBBLE CLASS
#*************

class Bubble:
    def __init__(self, x, y, speed):
        self.speed = speed
        self.circle = Circle(Point(x, y), 5)
        self.circle.setFill('white')
        
    def draw(self, window):
        self.circle.draw(window)
        
    def move(self):
        self.circle.move(0, self.speed)
        if self.circle.getCenter().getY() < 0:
             self.circle.move(0, WINDOW_HEIGHT + 5)
    

#*****************
# HELPER FUNCTIONS
#*****************

def setupInput(win, point, text):
    '''
    creates an Entry box with a label
    
    Params:
    win (GraphWin): the window the Entry box and label with be drawn in.
    point (Point): the location od the center of the text label
    text (str): the words that will be used to label the Entry box
    
    Returns:
    the Entry object created
    '''
    winText = Text(point, text)
    winText.setSize(18)
    winText.draw(win)
    winBox = Entry(Point(point.getX() + 225, point.getY()), 5)
    winBox.setSize(18)
    winBox.draw(win)
    return winBox

def getInput(win):
    '''
    Allows the user to enter the number of fish and bubbles for the aquarium.
    If a value is not entered or an invalid value (like a letter) is entered,
    the default number is used for that value.
    
    Params:
    win (GraphWin): the window the Entry box is in
    
    Returns:
    the number of fish and number of bubbles that will be drawn in the aquarium
    as a tuple
    '''
    directions = Text(Point(WINDOW_WIDTH/2 , 400), 'Enter the number of fish and bubbles, then click in the window.')
    directions.draw(win)
    fishEntry = setupInput(win, Point(300, 200), "Enter number of fish:")
    bubbleEntry = setupInput(win, Point(300, 300), "Enter number of bubbles:")
    win.getMouse()
    if fishEntry.getText().isdigit() and int(fishEntry.getText()) >= 0:
        numFish = int(fishEntry.getText())
    else:
        numFish = DEFAULT_FISH_NUM
    if bubbleEntry.getText().isdigit() and int(bubbleEntry.getText()) >= 0:
        numBubbles = int(bubbleEntry.getText())
    else:
        numBubbles = DEFAULT_BUBBLE_NUM
    fishEntry.undraw()
    bubbleEntry.undraw()
    directions.undraw()
    cover = Rectangle(Point(0, 0), Point(WINDOW_WIDTH, WINDOW_HEIGHT))
    cover.setFill("cyan")
    cover.draw(win)
    return numFish, numBubbles

def randColor():
    '''
    Returns a random color created from randomly generated red, green, and blue values
    '''
    red = random.randrange(0,MAX_COLOR_NUM + 1)
    green = random.randrange(0,MAX_COLOR_NUM + 1)
    blue = random.randrange(0,MAX_COLOR_NUM + 1)
    return color_rgb(red, green, blue)


def setupFish(numFish):
    '''
    Creates the list of fish with random position, color and speed
    
    Params:
    numFish (int): the number of fish to be added to the list
    
    Returns:
    the list of fish
    '''
    
    fishList = []
    
    for i in range(numFish):
        fishX = random.randrange(WINDOW_WIDTH)
        fishY = random.randrange(WINDOW_HEIGHT)
        fish_speed = random.randrange(-5, 0)
        fish = Fish(fishX, fishY, fish_speed, randColor())
        
        fishList.append(fish)
    
    return fishList


def setupBubbles(numBubbles):
    '''
    Creates the list of bubbles with random position and speed
    
    Params:
    numBubbles (int): the number of bubbles to be added to the list
    
    Returns:
    the list of bubbbles
    '''
    bubbleList = []
    
    for i in range(numBubbles):
        bubbleX = random.randrange(WINDOW_WIDTH)
        bubbleY = random.randrange(WINDOW_HEIGHT)
        bubble_speed = random.randrange(-5, 0)
        bubble = Bubble(bubbleX, bubbleY, bubble_speed)
        bubbleList.append(bubble)
    
    return bubbleList

#*****
# MAIN
#*****
def main():

    # make the graphics window (use autoflush=False to update more frequently)
    # makes the animation move more smoothly
    win = GraphWin("Swimming Fish", WINDOW_WIDTH, WINDOW_HEIGHT, autoflush=False)
    win.setBackground("cyan2")

    numFish, numBubbles = getInput(win)
                      
    # call helper functions to setup the fish and bubble lists
    bubbleList = setupBubbles(numBubbles)
    fishList = setupFish(numFish)
    
    
    # draw the fish and bubbles in their initial locations
    for bubble in bubbleList:
        bubble.draw(win)
        
    for fish in fishList:
        fish.draw(win)
        
    # continue swimming until the user clicks
    keepSwimming = True
    
    while keepSwimming:
        # loop through all the fish calling move method on each fish
        for fish in fishList:
            fish.move()

        # loop through all the bubbles calling move method on each bubble
        for bubble in bubbleList:
            bubble.move()
        
        # The bubble are after the fish so that the bubbles are drawn in front of the fish

        
        update(50) # call update to flush the window
        # if user clicks: stop swimming
        if win.checkMouse() != None:
            keepSwimming = False

    win.close()

if __name__ == '__main__':
    main()
