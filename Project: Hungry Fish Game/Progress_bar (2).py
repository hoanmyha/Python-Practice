from graphics2 import *
import time
import random
import math

SHARK_SPEED = 5
FISH_SPEED = 25
YELLOW_SPEED = 7
NUM_WIN = 10
STALL_TIME = 0.05
THRESHOLD = 50
NUM_YELLOW_FISH_TO_WIN = 10
NUM_SHARK_TO_WIN = 10
BAR_WIDTH = 200
BAR_HEIGHT = 20
BAR_X = 10
BAR_Y = 10 


def instructions():
    instructions_window = GraphWin("Game Instructions", 666, 666)
    instructions_window.setBackground("white")
    
    
    instruction_text = Text(Point(300, 50), "Hungry Fish")
    instruction_text.setSize(18)
    instruction_text.setStyle("bold")
    instruction_text.draw(instructions_window)
    
    level1_instructions = Text(Point(300, 100), f'Catch {NUM_YELLOW_FISH_TO_WIN} yellow fishes to upgrade to next level.')
    level1_instructions.draw(instructions_window)
    
    level2_instructions = Text(Point(300, 150), f'Catch  {NUM_SHARK_TO_WIN} sharks to win the game. ')
    level2_instructions.draw(instructions_window)
    
    lose_instructions = Text(Point(320, 200), 'If you are not in level 2 you can not eat the shark, attempt to eat the shark will make you lose the game')
    lose_instructions.setSize(10)
    lose_instructions.draw(instructions_window)
    
    start_instructions = Text(Point(300, 250), 'Click anywhere to start the game and use mouse pad to control the blue fish.')
    start_instructions.draw(instructions_window)
    
    
    instructions_window.getMouse()
    instructions_window.close()
    
    
    
def move_yellow(yellow_img_list):
    '''
    Moves every yellow one YELLOW_SPEED unit down the window
    
    Params:
    yellow_img_list (list): the list of falling spiders
    '''
    for yellow in yellow_img_list:
        yellow.move(-YELLOW_SPEED, 0)

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
    Each time the left arrow key is pressed the witch moves FISH_SPEED units left and
    each time the right arrow key is pressed the witch moves FISH_SPEED units right.
    
    window (GraphWin): the window where game play takes place
    fish_img (Image): the witch image
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
    shark_img = Image(shark_point, 'shark.gif')
    shark_img.draw(window)
    return shark_img

def progress_bars(window, yellow_caught, shark_caught):   
    
    yellow_bar = Rectangle(Point(BAR_X, BAR_Y), Point(BAR_X + BAR_WIDTH, BAR_Y + BAR_HEIGHT))
    yellow_bar.setFill('white')
    yellow_bar.draw(window)
    
    
    yellow_progress = Rectangle(Point(BAR_X, BAR_Y), Point(BAR_X + (BAR_WIDTH * yellow_caught / NUM_YELLOW_FISH_TO_WIN), BAR_Y + BAR_HEIGHT))
    yellow_progress.setFill('yellow')
    yellow_progress.draw(window)
    
                                                            
    shark_bar = Rectangle(Point(BAR_X, BAR_Y + BAR_HEIGHT + 10), Point(BAR_X + BAR_WIDTH, BAR_Y + 2 * BAR_HEIGHT + 10))
    shark_bar.setFill('white')
    shark_bar.draw(window)
                                                            
    shark_progress = Rectangle(Point(BAR_X, BAR_Y + BAR_HEIGHT + 10), Point(BAR_X + (BAR_WIDTH * shark_caught/ NUM_SHARK_TO_WIN), BAR_Y + 2 * BAR_HEIGHT + 10))
    shark_progress.setFill('blue')
    shark_progress.draw(window)                                                        
                                                            

def game_loop(window, fish):
    '''
    Loop continues to allow the sharks to move and the fish to move
    until enough spiders escape or the witch catches enough yellow to
    end the game.
    
    Params:
    window (GraphWin): the window where game play takes place
    witch (Image): the witch image
    '''
    
    shark_list = []
    yellow_list = []
    score = 0
    score_text = Text(Point(325,20), f"Player Score :{score}")
    score_text.draw(window)
    #infinete loop to change later
    while True:
        mousepoint = window.checkMousePointer()
        
        fish.setCenter(mousepoint)
        if random.randrange(100) < 4: #2% of a time I will get a shark 
            shark = add_shark_to_window(window)
            shark_list.append(shark)
        if random.randrange(100) < 7: #2% of a time I will get a yellow   
            yellow = add_yellow_to_window(window)
            yellow_list.append(yellow)
                                 
        move_shark(shark_list)
        time.sleep(STALL_TIME)
        
        move_yellow(yellow_list)
        time.sleep(STALL_TIME)
def main():        
    # setup the game
    instructions()
    
    
    window = GraphWin("Hungry Fish", 666,666)
    window.setBackground("white")
    
    
    fish = Image(Point(333,580), "big_fish1.gif")
    fish.draw(window)
    
    yellow_caught = 0
    shark_caught = 0
    progress_bars(window, yellow_caught, shark_caught)
    
    game_loop(window, fish)
    

main()