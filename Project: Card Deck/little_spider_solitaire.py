'''
Name: My Ha
CSC 201
Programming Project 4

This program plays a version of Little Spider Solitaire. In this
version the foundation piles of two red aces and two black kings
are created when the game begins. The eight tableau piles are in
one horizontal line. At any time, cards can be moved from the
tableau to the foundation piles or to another tableau, as long as
it is a valid move. One point is earned for every valid move to
a foundation pile.

Document Assistance (who and what or declare no assistance):
Tutor Kansakar helped me to figure out the way to begin the gameloop
Professor Mueller helped me to do the gameloop and run the code

'''

from board import *
from button import *
from deck import *
import time

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 500
FAKE_CARD = Card('cards/0j.gif')

def displayDirections():
    """
    Gives the directions for Skip 3 Solitaire. The "Click to begin" button
    must be clicked to continue to the game.

    """
    win = GraphWin("Directions", 700, 600)
    win.setBackground("white")
    string = ("Welcome to Little Spider Solitaire\n\n"
                "The objective is to get all cards\n"
                "into the foundation piles which are built\n"
                "sequentially from cards of the same suit.\n\n"
                "The top card in any tableau can be moved\n"
                "either to a foundation pile, to another\n"
                "tableau if its rank is one above or\n"
                "below the tableau's current top card, or\n"
                "moved to an empty tableau.\n\n"
                "No more moves? Click the stock pile to get\n"
                "eight more cards.\n\n"
                "Good luck!")
    directions = Text(Point(win.getWidth()/ 2, win.getHeight()/2), string)
    directions.setSize(16)
    directions.draw(win)
    startButton = Button(Point(350, 525), 120, 40, "Click to Begin")
    startButton.draw(win)
    startButton.activate()
    click = win.getMouse()
    while not startButton.isClicked(click):
        click = win.getMouse()
    win.close()

def setUpGame():
    '''
    Creates the window with a start button, the tableaus, the stock pile, the
    foundation, and the label for scoring an Aces Up solitaire game. When the
    start button is clicked one card is dealt to each tableau and the button
    is renamed Quit.
    
    Returns:
    the window where the game will be played, the board managing the cards,
    the button now labeled Quit, and the scoring label.
    '''
    window = GraphWin('Little Spider Solitaire', WINDOW_WIDTH, WINDOW_HEIGHT)
    window.setBackground('lightgreen')
    
    board = LittleSpiderBoard(window)
    
    button = Button(Point(675, 50), 80, 40, "Start")
    button.draw(window)
    button.activate()
    
    scoreLabel = Text(Point(70, 450), "Score: 0")
    scoreLabel.setSize(16)
    scoreLabel.draw(window)
    
    click = window.getMouse()
    while not button.isClicked(click):
        click = window.getMouse()
    
    button.setLabel("Quit")
    
    board.dealFromStock(window)
    return window, board, button, scoreLabel

def playGame(window, board, button, scoreLabel):
    '''
    Plays the Spider solitaire game enforcing the rules
    
    Params:
    window (GraphWin): the window where the game is played
    board (LittleSpiderBoard): the board managing the cards
    button (Button): the button to click to end the game
    scoreLabel (Text): the label showing the game score as the game progresses
    '''
    click = window.getMouse()
    firstCard = FAKE_CARD
    secondCard = FAKE_CARD
    score = 0

    while not button.isClicked(click):

        if board.isPointInStockCard(click):
            board.dealFromStock(window) 
        
        elif firstCard != FAKE_CARD and board.isPointInFoundationCard(click):
            secondCard = board.getCardAtPoint(click)
            if firstCard.isRed():
                if firstCard.getSuit() == secondCard.getSuit() and firstCard.getRank() == secondCard.getRank() + 1:
                    board.moveCardToFoundationPile(firstCard, click, window)
                    firstCard = FAKE_CARD
                    score = score + 1
                    scoreLabel.setText(f"Score: {score}")
            else:
                if firstCard.getSuit() == secondCard.getSuit() and firstCard.getRank() == secondCard.getRank() - 1:
                    board.moveCardToFoundationPile(firstCard, click, window)
                    firstCard = FAKE_CARD
                    score = score + 1
                    scoreLabel.setText(f"Score: {score}")
                    
        elif firstCard != FAKE_CARD and board.isPointInTableauCard(click):
            secondCard = board.getCardAtPoint(click)
            if firstCard.getRank() == secondCard.getRank() - 1 or firstCard.getRank() == secondCard.getRank() + 1:
                board.moveCardToAnotherTableauPile(firstCard, click, window)
                firstCard = FAKE_CARD
            if firstCard.getRank() == secondCard.getRank() + 12 or firstCard.getRank() == secondCard.getRank() - 12:
                board.moveCardToAnotherTableauPile(firstCard, click, window)
                firstCard = FAKE_CARD
            
        elif firstCard != FAKE_CARD and board.isPointInEmptyTableau(click):
            board.moveCardToAnotherTableauPile(firstCard, click, window)
            firstCard = FAKE_CARD
            
        elif board.isPointInTableauCard(click):
            firstCard = board.getCardAtPoint(click)
        


        click = window.getMouse()     
        

def flashingResultDisplay(window, result):
    '''
    Flashes text in the Graphics window
    
    Params:
    window (GraphWin): the window that will display the flashing text
    result (str): the String that will flash in the window
    '''
    resultText = Text(Point(300, 450), result)
    resultText.setSize(32)
    resultText.setTextColor('red')
    resultText.draw(window)
    for i in range(20):
        if i % 2 == 0:
            resultText.undraw()
        else:
            resultText.draw(window)
        time.sleep(.2)
    
def main():
    displayDirections()
    
    window, board, button, scoreLabel = setUpGame()
    
    playGame(window, board, button, scoreLabel)
    
    if board.isWin():
        result = 'Winner!'
    else:
        result = 'Loser :('
    flashingResultDisplay(window, result)
    
    time.sleep(2)    
    window.close()

if __name__ == '__main__':
    main()