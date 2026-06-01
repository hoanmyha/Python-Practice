'''
Name: My Ha
CSC 201
Programming Project 2

This program draws a map to show presidential election results with subregions either colored
red/blue to show whether democrats/republicans won that subregion or colored a
shade of purple based on the proportion of deomocrat/republican/other votes. The
map can be chosen to display the USA subdivided by states or a state subdivided
by counties. The user will enter data to choose USA or a state, the election year,
and whether a red/blue or purple map will be drawn.

Document Assistance:
Professor Mueller helped Prof Mueller helped me to find the width and height of the window
how to name a valid variable using str and int, and arrange my code to execute it
'''

from graphics2 import *

RED_BLUE_MAP = 1  # code for red/blue map
PURPLE_MAP = 2    # code for purple map
MAX_COLOR_NUM = 255   # maximum number for a color
MAX_SIZE = 700  # maximum dimension of the graphics window

# list of valid state postal codes and 'USA' 
ABBREV_LIST = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN',
               'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MH', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT','NE',
               'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD',
               'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'USA']

# valid years for election data
YEAR_LIST  = ['1960', '1964', '1968', '1972', '1976', '1980', '1984', '1988', '1992', '1996', '2000', '2004', '2008', '2012', '2016']

'''
Creates and returns a dictionary mapping the subregion
name to red or blue indictating whether republicans or
democrates had more votes in that subregion

Params:
fin_elect (file): file object connected to the data file with voting data

Returns:
a dictionary matching a subregion to either red (democrat) or blue (republican)
'''
def make_red_blue_dict(fin_elect):
    dict = {}
    first_line = fin_elect.readline()  # We're not using this line
    for line in fin_elect:
        line_data = line.split(',')
        subregion_name = line_data[0]
        republic_vote = int(line_data[1])
        democratic_vote = int(line_data[2])
        other_vote = int(line_data[3])
        
        # add code here to compare the election results
        # and store 'red' or 'blue' in variable color
        if republic_vote > democratic_vote:
            color = 'red'
        elif democratic_vote > republic_vote:
            color = 'blue'
   
        dict[subregion_name] = color  # associates 'red' or 'blue' with the subregion name in a dictionary
    return dict
        
'''
Creates and returns a dictionary mapping the subregion
name to a color representing the proportion of republican
(red) votes, democratic (blue) votes, and independent
(green) votes for a particular presidential election.

Params:
fin_elect (file): file object connected to the data file with voting data

Returns:
a dictionary matching a subregion to a shade of purple
'''
def make_purple_dict(fin_elect):
    dict = {}
    first_line = fin_elect.readline()   # We're not using this line
    for line in fin_elect:
        line_data = line.split(',')
        subregion_name = line_data[0]
        republic_vote = int(line_data[1])
        democratic_vote = int(line_data[2])
        other_vote = int(line_data[3])
        
        # add code here to compare the election results
        # and store a shade of purple in variable color
        red = int((republic_vote / (republic_vote + democratic_vote + other_vote)) * MAX_COLOR_NUM)
        blue = int((democratic_vote / (republic_vote + democratic_vote + other_vote)) * MAX_COLOR_NUM)
        green = int((other_vote / (republic_vote + democratic_vote + other_vote)) * MAX_COLOR_NUM)
        color = color_rgb(red, green, blue)
        
        dict[subregion_name] = color # associates a shade of purple with the subregion name in a dictionary
    return dict


def main():
    # Add statements in function main to prompt the user to enter USA or a state postal code.
    value_enter = input("Do you want a map of USA or a state? Enter USA or state postal code: ")
    value_enter = value_enter.upper()
    
    # Add statements in function main to prompt the user to enter the election year.
    if value_enter in ABBREV_LIST: 
        year_enter = input("Which year's election 1960-2012 do you want to see? ")
    else:
        print("Not a valid abbreviation. Exiting program.")
        exit(0)
        
    # Add statements in function main to prompt the user to enter 1 or 2 for red/blue or purple map    
    if year_enter in YEAR_LIST:
        map_type = int(input("Do you want a red/blue map(1) or purple map(2)? "))
    else:
        print("Not a valid year. Exiting program.")
        exit(0)
        
    # Creating code that will call the correct function 
    # which creates the dictionary mapping the subregion name to the color
    fin_elect = open(f"purple/{value_enter}{year_enter}.txt", 'r')    
    if map_type == RED_BLUE_MAP:
        dict = make_red_blue_dict(fin_elect)
    elif map_type == PURPLE_MAP:
        dict = make_purple_dict(fin_elect)
    else:
        print("Not a valid choice. Exiting program.")
        exit(0)
    
    # Open file to read through data
    fin = open(f"purple/{value_enter}.txt", 'r')    # change IL to another state or USA to draw its map
    # Read the first 2 lines in the file
    firstLine = fin.readline()
    firstLineSplit = firstLine.split()
    min_x = float(firstLineSplit[0])
    min_y = float(firstLineSplit[1])
    
    secondLine = fin.readline()
    secondLineSplit = secondLine.split()
    max_x = float(secondLineSplit[0])
    max_y = float(secondLineSplit[1])
        
    
    # Determine the width and height of the window proportional to the region's dimensions.
    # Create statement if that when region is wider than it is tall,
    # the width of the GraphWin should be MAX_SIZE and the height of the GraphWin will be a fraction of MAX_SIZE.
    # And Vice versa
    width = max_x - min_x
    height = max_y - min_y
    
    if height > width:
        window_height = MAX_SIZE
        window_width =  (width/height) * MAX_SIZE #* (69 / 55)
    else:
        window_width = MAX_SIZE
        window_height = (height/width) * MAX_SIZE #* (55 / 69)
        
    # Use window_width and window_height to draw window
    # set background color
    window = GraphWin("Draw Map", window_width, window_height)
    window.setBackground('white')
    
    # Use the setCoords method of the GraphWin class to set the coordinates of the window
    window.setCoords(min_x, min_y, max_x, max_y)
    
    # Reading data to draw the polygon
    num_subregions = int(fin.readline())
    # use loop to read through the data
    for count in range(num_subregions):
        blankLine = fin.readline()
        subregion_name = fin.readline().strip()
        region_name = fin.readline()
        num_lines_for_subregion = int(fin.readline())
        
        all_vertex = []
        
        # use loop to read through the data
        for num in range(num_lines_for_subregion):
            line_vertex = fin.readline()
            split_line_vertex = line_vertex.split()
            x = float(split_line_vertex[0])
            y = float(split_line_vertex[1])
  
            vertex = Point(x, y)
            all_vertex.append(vertex)
        
        polygon = Polygon(all_vertex)
        # using the dictionary to look up the color to fill the polygon       
        if subregion_name in dict:
            color = dict[subregion_name]
        else:
            color ='black'
        polygon.setFill(color)
        polygon.draw(window)


    fin.close()
  
main()