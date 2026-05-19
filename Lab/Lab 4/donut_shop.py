"""
Name(s): My, Rhys
CSC 201
Lab 4--donut_shop.py

When completed, the user will click in the window 3 times
to draw 3 donuts (with sprinkles if you got to the bonus!).

Did you complete this lab file during the class period : No

    I completed donut_shop.py without my partner from class.

    Document any assistance you get if you complete the lab after the class period:
    
"""

from graphics2 import *
import random
import math

COLOR_LIST = ['red','blue','lime','black', 'magenta', 'darkviolet', 'deeppink3', 'dodgerblue1', 'firebrick2']
NUM_SPRINKLES = 150
SPRINKLE_RADIUS = 3
HOLE_RATIO = 1/3

def drawOneDonut(window, glazeColor, backgroundColor, radius, center):
    """
    The function draws one donut with color, size, and placement given by the parameters.
    
    Parameters:
    window (GraphWin): the window to draw the donut in
    glazeColor (str): a string for the color of the donut
    backgroundColor (str): a string for the color of the background used to draw the hole
    radius (int): the outer radius of the donut
    center (Point): the center point of the donut
    """
    
    circle = Circle(center, radius)
    circle.setFill(glazeColor)
    circle.setOutline(glazeColor)
    circle.draw(window)
    
    circle = Circle(center, radius/3)
    circle.setFill(backgroundColor)
    circle.setOutline(backgroundColor)
    circle.draw(window) 

def drawSprinkles(window, donut):
    """
    The function draws sprinkles(circles) with a randomly chosen color and position
    so that all are draw on the donut's surface.
    
    Parameters:
    window (GraphWin): the window to draw the sprinkles in
    donut (Circle): the large circle making the donut
    """
    pass



def main():
    # create window
    window = GraphWin("Donut Shop", 500, 500)
    window.setBackground('cyan')
    
    # draw donuts in window
    donutOneCenter = window.getMouse()
    drawOneDonut(window, 'pink', 'cyan', 100, donutOneCenter)
    
    donutTwoCenter = window.getMouse()
    drawOneDonut(window, 'yellow', 'cyan', 75, donutTwoCenter)
    
    donutThreeCenter = window.getMouse()
    drawOneDonut(window, 'red', 'cyan', 85, donutThreeCenter)
    

main()
    
    