'''
Name: My Ha & Anh Le
CSC 201
Programming Project 3

This is a different of hungry fish game. At the beginning of the game, you will start with a small fish and you need to catch 10 yellow fishes to upgrade to the next fish size, and your fish will grow bigger.
After your fish grows bigger, you need to catch 10 sharks to upgrade to the final fish size.
At the final fish size you can eat the orca and win the game.
Attempting to eat the shark while you are not in the size allowed to eat will make you lose the game.
Reach 30 points to win the game and enjoy the funny winning sounds at the end!
Good luck gamers !!!

Bonus: sound effects and music, levels of the game, changes in the size of the fish due to the level,
    progress bars, have different images and options to play again when the game ends,
    extra image: orca, the quit button running away when approaching it.

Document Assistance:
    Professor Mueller helped me to get the mouse in the instruction window and gave me hints for the instructions, and progress bars.
    Tutor Dennis helped me figure out how to execute the after-game window
    and the while loop to play the game again
    Tutor Kansakar helped me move the target fish in the proper direction
    Tutor Farrukh helped me to check the mistakes in my code in order to execute them. 
 
     
'''
from graphics2 import *
import time
import random
import math
import pygame
from button import Button

# Initialize pygame
pygame.mixer.init()

# Sound effects
bite = pygame.mixer.Sound('Bite.mp3')
grow = pygame.mixer.Sound('grow.mp3')
yay = pygame.mixer.Sound('yay.mp3')
bg_music = pygame.mixer.Sound('bg_music.mp3') 

LEVEL_UP = 10
SHARK_SPEED = 10
FISH_SPEED = 26
YELLOW_SPEED = 10
ORCA_SPEED = 8
NUM_WIN = LEVEL_UP * 3
STALL_TIME = 0.05
LOW_THRESHOLD = 50
MID_THRESHOLD = 90
HIGH_THRESHOLD = 150

BAR_WIDTH = 200
BAR_HEIGHT = 20
BAR_X = 10
BAR_Y = 10 

def mouseRun(window, mousepoint, quit_button):
    '''
    Determines if the mousepoint is close enough to the quit button that it would run away.
    
    Params:
    mousepoint (Point): the mouse
    quit_button (Point): the quit button
    '''
    buttonCenter = quit_button.getButtonCenter()
    buttonX = buttonCenter.getX()
    buttonY = buttonCenter.getY()
    mouseX = mousepoint.getX()
    mouseY = mousepoint.getY()
    
    if (distance_between_points(buttonCenter, mousepoint) < 150):
        if buttonX < mouseX:
            quit_button.move(-10,0)
        else:
            quit_button.move(10,0)
        if buttonY < mouseY:
            quit_button.move(0,-10)
        else:
            quit_button.move(0,10)
            
def instructions():
    '''
    Creates instruction window to displays the game's rules and descriptions
    Creates menu for player to choose play or quit
    However, it will not allow player to click the quit button before playing
    '''
    instructions_window = GraphWin("Game Instructions", 666, 666)
    background = Image(Point(333, 333), "back.png")
    background.draw(instructions_window)
      
    instruction_text = Text(Point(333, 50), "Hungry Fish")
    instruction_text.setSize(20)
    instruction_text.setStyle("bold")
    instruction_text.draw(instructions_window)
    
    level1_instructions = Text(Point(330, 100), f'Catch {LEVEL_UP} yellow fishes to upgrade to level 2.')
    level1_instructions.setSize(15)
    level1_instructions.setTextColor("#ba8b25")
    level1_instructions.draw(instructions_window)
    
    level2_instructions = Text(Point(330, 120), f'Catch {LEVEL_UP} sharks to upgrade to level 3. ')
    level2_instructions.setSize(15)
    level2_instructions.setTextColor("#ba8b25")
    level2_instructions.draw(instructions_window)
    
    level3_instructions = Text(Point(330, 140), f'Catch {LEVEL_UP} orcas to win the game. ')
    level3_instructions.setSize(15)
    level3_instructions.setTextColor("#ba8b25")
    level3_instructions.draw(instructions_window)
    
    eat_instructions = Text(Point(333, 200), 'If you are not in level 2, you can not eat the sharks. ')
    eat_instructions.setSize(15)
    eat_instructions.draw(instructions_window)
    
    lose_instructions = Text(Point(333, 220), 'Attempt to eat the sharks and orcas will make you lose the game. ')
    lose_instructions.setSize(15)
    lose_instructions.draw(instructions_window)
    
    eat_instructions = Text(Point(333, 260), 'If you are not in level 3, you can not eat the orcas. ')
    eat_instructions.setSize(15)
    eat_instructions.draw(instructions_window)
    
    lose_instructions = Text(Point(333, 280), 'Attempt to eat the orcas will make you lose the game. ')
    lose_instructions.setSize(15)
    lose_instructions.draw(instructions_window)
    
    start_instructions = Text(Point(333, 330), 'Click Play button to start the game and use mouse pad to control the blue fish.')
    start_instructions.setSize(12)
    start_instructions.setTextColor("#f06b18")
    start_instructions.setStyle("bold italic")
    start_instructions.draw(instructions_window)
    
    play_button = Button(Point(333, 420), 100, 50, "Play")
    quit_button = Button(Point(333, 520), 100, 50, "Quit")
    play_button.activate()
    quit_button.activate()
    play_button.draw(instructions_window)
    quit_button.draw(instructions_window)
    
    notPlay = True
    while notPlay:
        mousepoint = instructions_window.checkMousePointer()
        mouseRun(instructions_window, mousepoint, quit_button)
        
        get_mouse = instructions_window.checkMouse()
        if get_mouse != None and play_button.isClicked(get_mouse):
            notPlay = False
    
    instructions_window.close()
    
           
def distance_between_points(point1, point2):
    '''
    Calculates the distance between two points
    
    Params:
    point1 (Point): the first point
    point2 (Point): the second point
    
    Returns:
    the distance between the two points
    '''
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    return math.sqrt(dx**2 + dy**2)

def is_close_enough(fish, target, is_yellow_caught, is_shark_caught):
    '''
    Determines if the fish is close enough to the target fishes to say the fish
    caught the target.
    
    Params:
    is_yellow_caught (Boolean): determines if the yellow fish is caught
    is_shark_caught (Boolean): determines if the yellow fish is caught
    
    Returns:
    True if the fish catches the targets
    '''
    fish_center = fish.getCenter()
    target_center = target.getCenter()
    distance = distance_between_points(fish_center, target_center)

    if not is_yellow_caught:
        if distance < LOW_THRESHOLD:
            return True
        else:
            return False
    elif is_yellow_caught and not is_shark_caught:
        if distance < MID_THRESHOLD:
            return True
        else:
            return False
    else:
        if distance < HIGH_THRESHOLD:
            return True
        else:
            return False
        
def add_yellow_to_window(window):
    '''
    Adds one yellow to the right of the window at a random location
    
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
    shark_img = Image(shark_point, 'shark(5).gif')
    shark_img.draw(window)
    return shark_img

def add_orca_to_window(window):
    '''
    Adds one orca to the right of the window at a random location
    
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

def move_yellow(yellow_img_list):
    '''
    Moves every yellow one YELLOW_SPEED unit down the window
    
    Params:
    yellow_img_list (list): the list of moving yellow fishes
    '''
    for yellow in yellow_img_list:
        yellow.move(-YELLOW_SPEED, 0)

def move_shark(shark_img_list):
    '''
    Moves every shark one SHARK_SPEED unit down the window
    
    Params:
    shark_img_list (list): the list of moving sharks
    '''
    for shark in shark_img_list:
        shark.move(SHARK_SPEED, 0)
        
def move_orca(orca_img_list):
    '''
    Moves every orca one ORCA_SPEED unit down the window
    
    Params:
    orca_img_list (list): the list of moving orcas
    '''
    for orca in orca_img_list:
        orca.move(-ORCA_SPEED, 0)
        
def game_loop(window, fish):
    '''
    Loop continues to allow the target fishes to move and the fish to move
    until the fish catches enough yellow fishes, sharks, and orcas to
    end the game.
    
    Params:
    window (GraphWin): the window where game play takes place
    fish (Image): the witch image
    
    Return:
    Return hasNOTLost 
    '''
    
    shark_list = []
    yellow_list = []
    orca_list = []
    yellow_caught = 0
    shark_caught = 0
    orca_caught = 0
    hasNOTLost = True
    is_yellow_caught = False
    is_shark_caught = False
    
    bg_music.play()
    
    while orca_caught < LEVEL_UP and hasNOTLost:
        mousepoint = window.checkMousePointer()
        
        fish.setCenter(mousepoint)
        if random.randrange(100) < 8: #% of a time I will get a shark 
            shark = add_shark_to_window(window)
            shark_list.append(shark)
        if random.randrange(100) < 10: #% of a time I will get a yellow   
            yellow = add_yellow_to_window(window)
            yellow_list.append(yellow)
        if random.randrange(100) < 7: #% of a time I will get an orca  
            orca = add_orca_to_window(window)
            orca_list.append(orca)
                                 
        move_shark(shark_list)
        move_yellow(yellow_list)  
        move_orca(orca_list)
        
        for orca in orca_list:
            if is_close_enough(fish, orca, is_yellow_caught, is_shark_caught):
                if not is_shark_caught:
                    hasNOTLost = False
                else:
                    orca_caught = orca_caught + 1
                    bite.play()
                    orca.undraw()
                    orca_list.remove(orca)
                
                
        for shark in shark_list:
            if is_close_enough(fish, shark, is_yellow_caught, is_shark_caught):
                if not is_yellow_caught:
                    hasNOTLost = False
                else:
                    shark_caught = shark_caught + 1
                    bite.play()
                    shark.undraw()
                    shark_list.remove(shark)
                    
                    if shark_caught == LEVEL_UP:
                        is_shark_caught = True
                        point_fish = fish.getAnchor()
                        fish.undraw()
                        grow.play()
                        fish = Image(point_fish, "big_fish2.gif")
                        fish.draw(window)
        
        for yellow in yellow_list: 
            if is_close_enough(fish, yellow, is_yellow_caught, is_shark_caught):
                yellow_caught = yellow_caught + 1
                bite.play()
                yellow.undraw()
                yellow_list.remove(yellow)
        
                if yellow_caught == LEVEL_UP:
                    is_yellow_caught = True
                    point_fish = fish.getAnchor()
                    fish.undraw()
                    grow.play()
                    fish = Image(point_fish, "big_fish1.gif")
                    fish.draw(window)
        label(window)            
        progress_bars(window, yellow_caught, shark_caught, orca_caught)
        time.sleep(STALL_TIME)
        
    return hasNOTLost 
 
def progress_bars(window, yellow_caught, shark_caught, orca_caught):
    '''
    Creates progress bars to let players see the level they are in
    and the number of target fishes they need to catch in order to win
    
    Params:
    window (GraphWin): the window where game play takes place
    fish (Image): the fish image  
    '''
    if yellow_caught > LEVEL_UP:
        yellow_caught = LEVEL_UP
        
    if shark_caught > LEVEL_UP:
        shark_caught = LEVEL_UP
    
    if orca_caught > LEVEL_UP:
        orca_caught = LEVEL_UP
        
    yellow_bar = Rectangle(Point(BAR_X, BAR_Y), Point(BAR_X + BAR_WIDTH, BAR_Y + BAR_HEIGHT))
    yellow_bar.setFill('white')
    yellow_bar.draw(window)  
    
    yellow_progress = Rectangle(Point(BAR_X, BAR_Y), Point(BAR_X + (BAR_WIDTH * yellow_caught / LEVEL_UP), BAR_Y + BAR_HEIGHT))
    yellow_progress.setFill('yellow')
    yellow_progress.draw(window)
                                                            
    shark_bar = Rectangle(Point(BAR_X, BAR_Y + BAR_HEIGHT + 10), Point(BAR_X + BAR_WIDTH, BAR_Y + 2 * BAR_HEIGHT + 10))
    shark_bar.setFill('white')
    shark_bar.draw(window)
                                                            
    shark_progress = Rectangle(Point(BAR_X, BAR_Y + BAR_HEIGHT + 10), Point(BAR_X + (BAR_WIDTH * shark_caught/ LEVEL_UP), BAR_Y + 2 * BAR_HEIGHT + 10))
    shark_progress.setFill('blue')
    shark_progress.draw(window)
    
    orca_bar = Rectangle(Point(BAR_X, BAR_Y + BAR_HEIGHT + 40), Point(BAR_X + BAR_WIDTH, BAR_Y + 2 * BAR_HEIGHT + 40))
    orca_bar.setFill('white')
    orca_bar.draw(window)
                                                            
    orca_progress = Rectangle(Point(BAR_X, BAR_Y + BAR_HEIGHT + 40), Point(BAR_X + (BAR_WIDTH * orca_caught/ LEVEL_UP), BAR_Y + 2 * BAR_HEIGHT + 40))
    orca_progress.setFill('black')
    orca_progress.draw(window)
    
def label(window):
    
    yellow_label = Text(Point(260, 20), "yellow fish")
    yellow_label.setSize(12)
    yellow_label.setStyle("bold")
    yellow_label.setTextColor("orange")
    yellow_label.draw(window)
    
    shark_label = Text(Point(250, 50), " shark")
    shark_label.setSize(12)
    shark_label.setStyle("bold")
    shark_label.setTextColor("orange")
    shark_label.draw(window)
    
    orca_label = Text(Point(250, 80), " orca")
    orca_label.setSize(12)
    orca_label.setStyle("bold")
    orca_label.setTextColor("orange")
    orca_label.draw(window)
 
def after_game_window(window, hasNOTLost):
    '''
    Displays different images depending on whether player lose or win
    and offer options to quit or play again
    
    Params:
    window (GraphWin): the window where game play takes place
    hasNOTLost (Boolean): determines if the player lose or not
    
    Returns:
    returns the play_again_button, and quit_button 
    '''
    after_game_bg = Rectangle(Point(0,0), Point(666,666))
    after_game_bg.setFill("white")
    after_game_bg.draw(window)
    if hasNOTLost:
        yay.play()
        winner_image = Image(Point(333, 333), "win_back.gif")
        winner_image.draw(window)
        winner_text = Text(Point(333, 90),"You win!!!")
        winner_text.setFace("times roman")
        winner_text.setSize(50)
        winner_text.draw(window)
    else:
        loser_image = Image(Point(333, 333), "lose_back.gif")
        loser_image.draw(window)
        loser_text = Text(Point(333, 100),"You lose!!!")
        loser_text.setFace("times roman")
        loser_text.setSize(50)
        loser_text.draw(window)
        
    play_again_button = Button(Point(233, 550), 100, 50, "Play Again")
    quit_button = Button(Point(433, 550), 100, 50, "Quit")
    
    play_again_button.activate()
    quit_button.activate()
    
    play_again_button.draw(window)
    quit_button.draw(window)
    
    return play_again_button, quit_button           
        

def main():
    # setup the game
    instructions()
    window = GraphWin("Hungry Fish", 666,666)
    
    #While loop for playing again
    again = True
    while again:
        
        background = Image(Point(333, 333), "back.png")
        background.draw(window)
        
        fish = Image(Point(333,580), "small_fish.gif")
        fish.draw(window)
        
        hasNOTLost = game_loop(window, fish)
        bg_music.stop()
        
        play_again_button, quit_button = after_game_window(window, hasNOTLost)
        mousepoint = window.getMouse()
        if play_again_button.isClicked(mousepoint):
            again = True
        elif quit_button.isClicked(mousepoint):
            window.close()
            exit(0)
            again = False
              
main()
