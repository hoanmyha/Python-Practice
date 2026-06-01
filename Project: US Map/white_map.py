"""
Name: My Ha
CSC 201
Programming Project 2-Checkpoint

This program reads a file in a specific format and draws
a map of a region using the latitude and longitude values
delineating the outline of subregions on the map. It is
either a map of the USA with subregions as states OR
a map of a state with subregions as counties.

Document Assistance: Professor Mueller helped me to execute the program

"""
MAX_SIZE = 700
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

from graphics2 import *
                           
def main():
    fin = open('purple/IL.txt', 'r')    # change IL to another state or USA to draw its map
    
    # Read the first 2 lines in the file
    firstLine = fin.readline()
    firstLineSplit = firstLine.split()
    min_x = float(firstLineSplit[0])
    min_y = float(firstLineSplit[1])
    
    secondLine = fin.readline()
    secondLineSplit = secondLine.split()
    max_x = float(secondLineSplit[0])
    max_y = float(secondLineSplit[1])
        
# Create window where subregions in polygon shape will be drawn
    window = GraphWin("White Map", MAX_SIZE, MAX_SIZE) #autoflush=False? 
    window.setBackground('white')
# Use the setCoords method of the GraphWin class to set the coordinates of the window
    window.setCoords(min_x, min_y, max_x, max_y)
    
    num_subregions = int(fin.readline())
    # use loop to read through the data
    for count in range(num_subregions):
        blankLine = fin.readline()
        subregion_name = fin.readline()
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
        polygon.draw(window)
        
    
    fin.close()
  
main()