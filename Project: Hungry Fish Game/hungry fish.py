from graphics2 import *
import time
import random
import math

SHARK_SPEED = 5
FISH_SPEED = 25
YELLOW_SPEED = 7
ORCA_SPEED = 4
NUM_WIN = 10
STALL_TIME = 0.05
THRESHOLD = 50

def move_yellow(yellow_img_list):
    '''
    Moves every yellow one yellow_SPEED unit down the window
    
    Params:
    yellow_img_list (list): the list of falling spiders
    '''
    for yellow in yellow_img_list:
        yellow.move(-YELLOW_SPEED, 0)
        
def move_orca(orca_img_list):
    '''
    Moves every orca one ORCA_SPEED unit down the window
    
    Params:
    orca_img_list (list): the list of falling spiders
    '''
    for orca in orca_img_list:
        orca.move(-ORCA_SPEED, 0)

def move_shark(shark_img_list):
    '''
    Moves every shark one SHARK_SPEED unit down the window
    
    Params:
    shark_img_list (list): the list of falling spiders
    '''
    for shark in shark_img_list:
        shark.move(SHARK_SPEED, 0)
        
def move_fish(window, fish_gif):
    '''
    Each time the left arrow key is pressed the witch moves WITCH_SPEED units left and
    each time the right arrow key is pressed the witch moves WITCH_SPEED units right.
    
    window (GraphWin): the window where game play takes place
    witch_img (Image): the witch image
    '''
    key_press = window.checkKey()
    if key_press == 'Left':
        fish_gif.move(-FISH_SPEED, 0)
    elif key_press  == 'Right':
        fish_gif.move(FISH_SPEED, 0)

def add_yellow_to_window(window):
    '''
    Adds one yellow to the left of the window at a random location
    
    Params:
    window (GraphWin): the window where game play takes place
    
    Returns:
    the yellows added to the window
    '''
    y_location = random.randrange(40, 620)
    yellow_point = Point(666, y_location)
    yellow_img = Image(yellow_point, 'yellow.gif')
    yellow_img.draw(window)
    return yellow_img

def add_orca_to_window(window):
    '''
    Adds one orca to the left of the window at a random location
    
    Params:
    window (GraphWin): the window where game play takes place
    
    Returns:
    the orcas added to the window
    '''
    y_location = random.randrange(40, 620)
    orca_point = Point(666, y_location)
    orca_img = Image(orca_point, 'orca.gif')
    orca_img.draw(window)
    return orca_img

def add_shark_to_window(window):
    '''
    Adds one shark to the left of the window at a random location
    
    Params:
    window (GraphWin): the window where game play takes place
    
    Returns:
    the sharks added to the window
    '''
    y_location = random.randrange(40, 620)
    shark_point = Point(0, y_location)
    shark_img = Image(shark_point, 'shark(5).gif')
    shark_img.draw(window)
    return shark_img

def game_loop(window, fish):
    '''
    Loop continues to allow the sharks to move and the fish to move
    until enough spiders escape or the witch catches enough spiders to
    end the game.
    
    Params:
    window (GraphWin): the window where game play takes place
    witch (Image): the witch image
    '''
    
    shark_list = []
    yellow_list = []
    orca_list = []
    #infinete loop to change later
    while True:
        move_fish(window, fish)
        if random.randrange(100) < 4: #% of a time I will get a shark 
            shark = add_shark_to_window(window)
            shark_list.append(shark)
        if random.randrange(100) < 7: #% of a time I will get a yellow   
            yellow = add_yellow_to_window(window)
            yellow_list.append(yellow)
        if random.randrange(100) < 1: #% of a time I will get an orca  
            orca = add_orca_to_window(window)
            orca_list.append(orca)
                                 
        move_shark(shark_list)
        time.sleep(STALL_TIME)
        
        move_yellow(yellow_list)
        time.sleep(STALL_TIME)

        move_orca(orca_list)
        time.sleep(STALL_TIME)

def main():
    # setup the game 
    window = GraphWin("Hungry Fish", 666,666)
    window.setBackground("white")
    
    #directions = Text(Point(333, 650), 'Use the left/right arrow keys to move the witch.')
    #directions.setSize(16)
    #directions.draw(window)
    
    fish = Image(Point(333,580), "big_fish1.gif")
    fish.draw(window)
    
    game_loop(window, fish)

main()