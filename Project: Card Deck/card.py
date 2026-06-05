'''
Name: My Ha
CSC 201
Programming Project 4--Card Class

The Card class represents one standard poker card for a card game. Cards have a rank,
a suit, and an image. The card stores its position in a graphics window. It can be drawn and
undrawn in the graphics window.

Document Assistance (who and what or declare no assistance):
Tutor Farrukh helped me to run the function containsPoint 

'''
from graphics2 import *
import time

class Card:
    # Add your methods above __eq__
    def __init__(self, fileName):
        '''
        Using filename to create image and extract rank and suit
        
        Params:
        fileName (string): The image's file name will be received as, for
        example, 'cards/13h.gif' (for the king of hearts)
        '''
        self.image = Image(Point(0,0), fileName)
        fileName = fileName.split('/')
        rank_and_suit = fileName[1]
        self.rank = rank_and_suit[:-5]
        self.rank = int(self.rank)
        self.suit = rank_and_suit[-5]
        
    def getRank(self):
        '''
        Returns the rank of cards
        
        Returns:
            the rank number of cards
        '''
        return self.rank
    
    def getSuit(self):
        '''
        Returns the suit of cards
        
        Returns:
            the suit of cards (for example: 'h', 'd')
        '''
        return self.suit
    
    def getImage(self):
        '''
        Returns the image of cards
        
        Returns:
            the image of cards
        '''
        return self.image
    
    def draw(self, window):
        '''
        Draw the card's image on the window
        
        Params:
            window (GraphWin): the window where the card is draw
        '''
        self.image.draw(window)
        
    def undraw(self):
        '''
        Remove the card's image on the window
        '''
        self.image.undraw()
    
    def isRed(self):
        '''
        Check to see if the cards' suit are heart and diamond which all have red color
        
        Returns:
            True if it is red
            False if it is black
        '''
        if self.suit == 'h' or self.suit == 'd':
            return True
        else:
            return False
        
    def move(self, dx, dy):
        '''
        Moves the card dx pixels in the horizontal direction and dy pixels in the vertical direction
    
        Params:
            dx, dy (int): to show the horizontal and vertical direction when the image move
        '''
        self.image.move(dx, dy)
        
    def containsPoint(self, point):
        '''
        Returns True if the point received as a parameter is within the bounds of the card.
        Otherwise, it returns False.
        
        Params:
            point(Point Object): the point that is clicked
        
        Returns:
            True if the point received as a parameter is within the bounds of the card.
            False if the point received as a parameter is not within the bounds of the card.
        '''
        image_centerX = self.image.getCenter().getX()
        image_centerY = self.image.getCenter().getY()
        
        imageWidth = self.image.getWidth()
        imageHeight = self.image.getHeight()
        
        if point.getX() > (image_centerX - 0.5 * imageWidth) and point.getX() < (image_centerX + 0.5 * imageWidth) and point.getY() < (image_centerY + 0.5 * imageHeight) and point.getY() > (image_centerY - 0.5 * imageHeight):
            return True
        else:
            return False
        
    def __eq__(self, cardToCompare):
        '''
        Allows users of the Card class to compare two cards using ==
        
        Params:
        cardToCompare (Card): the Card to check for equality with this Card
        
        Returns:
        True if the two cards have the same rank and suit. Otherwise, False
        '''
        return self.suit == cardToCompare.suit and self.rank == cardToCompare.rank

    def __str__(self):
        '''
        Return a string representation following required form
        
        Returns:
            a string representation following required form
        '''
        image_centerX = self.image.getCenter().getX()
        image_centerY = self.image.getCenter().getY()
        
        return f'suit = {self.suit}, rank = {self.rank}, center = Point({image_centerX}, {image_centerY})'
        
        
def main():  
    window = GraphWin("Testing Card", 500, 500)
    
    # create King of Hearts card
    fileName = 'cards/13h.gif'
    card = Card(fileName)

    # print card using __str__ and test getRank, getSuit, getImage
    print(card)
    print(card.getRank())
    print(card.getSuit())
    print(card.getImage())
    print(card.isRed())
    
    # move card to center of window and display it
    card.move(250, 250)
    card.draw(window)
    
    # click only on the card should move it 100 pixels left
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(-100, 0)
    
    # click only on the card should move it 200 pixels right and 100 pixels down
    point = window.getMouse()
    while not card.containsPoint(point):
        point = window.getMouse()
    card.move(200, 100)
    
    # print the card using __str__
    print(card)
    
    # stall 2 seconds
    time.sleep(2)
    
    # create 2 of Spades card
    fileName = 'cards/2s.gif'
    card2 = Card(fileName)

    # print card2 using __str__ and test getRank, getSuit
    print(card2)
    print(card2.getRank())
    print(card2.getSuit())
    print(card2.isRed())
    
    # move card2 to center of window and display it
    card2.move(250, 250)
    card2.draw(window)
    
    # stall 2 seconds then remove both cards from the window
    time.sleep(2)
    card.undraw()
    card2.undraw()
    
    # stall 2 seconds then close the window
    time.sleep(2)
    window.close()
    
if __name__ == '__main__':
    main()
        
        