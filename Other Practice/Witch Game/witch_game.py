'''
Use the witch to catch spiders. Move the witch using the left and right arrow keys.
If the witch catches enough spiders, you win.
'''
from graphics2 import *
import time
import random
import math

SPIDER_SPEED = 5
WITCH_SPEED = 25
NUM_WIN = 10
STALL_TIME = 0.05
THRESHOLD = 50

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


def is_close_enough(witch_img, spider_img):
    '''
    Determines if the witch is close enough to the spider to say the witch
    caught the spider.
    
    Params:
    witch_img (Image): the image of the witch
    spider_img (Image): the image of the spider
    
    Returns:
    True if the witch catches the spider
    '''
    witch_center = witch_img.getCenter()
    spider_center = witch_img.getCenter()
    distance = distance_between_points(witch_center, spider_center)
    if distance < THRESHOLD:
        return True
    else:
        return False
    ...
    
def move_spiders(spider_img_list):
    '''
    Moves every spider one SPIDER_SPEED unit down the window
    
    Params:
    sprider_img_list (list): the list of falling spiders
    '''
    for spider in spider_img_list:
        spider.move(0, SPIDER_SPEED)
        

def move_witch(window, witch_img):
    '''
    Each time the left arrow key is pressed the witch moves WITCH_SPEED units left and
    each time the right arrow key is pressed the witch moves WITCH_SPEED units right.
    
    window (GraphWin): the window where game play takes place
    witch_img (Image): the witch image
    '''
    key_press = window.checkKey()
    if key_press == 'Left':
        witch_img.move(-WITCH_SPEED, 0)
    elif key_press  == 'Right':
        witch_img.move(WITCH_SPEED, 0)
    elif key_press  == 'Up':
        witch_img.move(0, -WITCH_SPEED)
    elif key_press  == 'Down':
        witch_img.move(0, WITCH_SPEED)
        
    #checkMousepointer
    #abc = window.checkMousePOinter
    #dddd.setCenter(abc)

def add_spider_to_window(window):
    '''
    Adds one spider to the top of the window at a random location
    
    Params:
    window (GraphWin): the window where game play takes place
    
    Returns:
    the spider added to the window
    '''
    x_location = random.randrange(40, 620)
    spider_point = Point(x_location, 50)
    spider_img = Image(spider_point, 'spider.gif')
    print(spider_img)
    spider_img.draw(window)
    return spider_img

def game_loop(window, witch):
    '''
    Loop continues to allow the spiders to fall and the witch to move
    until enough spiders escape or the witch catches enough spiders to
    end the game.
    
    Params:
    window (GraphWin): the window where game play takes place
    witch (Image): the witch image
    '''
    
    spider_list = []
    count_collisions = 0
    
    
    #infinete loop to change later
    while count_collisions < NUM_WIN:
        move_witch(window, witch)
        if random.randrange(100) < 6: #6% of a time I will get a spider
            print("in here")
            spider = add_spider_to_window(window)
            print(spider)
            spider_list.append(spider)
                    
        move_spiders(spider_list)
        
        for spider in spider_list: #ADD
            if is_close_enough(witch, spider):
                count_collisions = count_collisions + 1
                spider.undraw()
                spider_list.remove(spider)
        
        for spider in spider_list: #ADD
            if spider.getCenter().getY > 600:
                spider.undraw()
                spider_list.remove(spider)
        
        time.sleep(STALL_TIME)
        
        
def main():
    # setup the game 
    window = GraphWin("Arachnophobia!!!", 666,666)
    window.setBackground("white")
    directions = Text(Point(333, 650), 'Use the left/right arrow keys to move the witch.')
    directions.setSize(16)
    directions.draw(window)
    
    witch = Image(Point(333,580), "witch.gif")
    witch.draw(window)
    
    game_loop(window, witch)


main()
    
