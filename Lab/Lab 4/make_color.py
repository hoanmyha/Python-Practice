"""
Name(s): My, Rhys
CSC 201
Lab 4--make_color.py

Enter red, green, and blue components to mix a color,
then fill the rectangle with that color

Did you complete this lab file during the class period Yes


    
"""
from graphics2 import *

def main():
    #create window and show directions
    window = GraphWin("What's the color?", 600, 600)
    window.setBackground('white')
    directions = Text(Point(300, 30), "Enter the amounts of red, green, and blue.")
    directions.draw(window)
    clickDirections = Text(Point(300, 60), "Click mouse when done.")
    clickDirections.draw(window)
    
    #draw the rectangle
    colorRect = Rectangle(Point(100, 250), Point(500, 550))
    colorRect.draw(window)
    
    #setup labels and entry boxes for input
    redLabel = Text(Point(110, 150), "red")
    redLabel.draw(window)
    inputRed = Entry(Point(160, 150), 5)
    inputRed.setTextColor('red')
    inputRed.draw(window)
    
    greenLabel = Text(Point(260, 150), "green")
    greenLabel.draw(window)
    inputGreen = Entry(Point(310, 150), 5)
    inputGreen.setTextColor('green')
    inputGreen.draw(window)
    
    blueLabel = Text(Point(410, 150), "blue")
    blueLabel.draw(window)
    inputBlue = Entry(Point(460, 150), 5)
    inputBlue.setTextColor('blue')
    inputBlue.draw(window)
    
    window.getMouse()
    
    #get numbers from entry boxes to mix the color
    num_red = int(inputRed.getText())
    num_green = int(inputGreen.getText())
    num_blue = int(inputBlue.getText())
    
    # make color from red, green, blue numbers
    red = int(inputRed.getText())
    green = int(inputGreen.getText())
    blue = int(inputBlue.getText())
    
    # add the color to the rectangle that is already drawn
    color = color_rgb(red, green, blue)
    colorRect.setFill(color)




    
main()