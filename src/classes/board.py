import pygame

from classes.Square import Square

class Board:
    # Board has a width and height of 640 pixels
    WIDTH = 640
    HEIGHT = 640
    
    '''
        A board has the following:
        - A 2D list of Squares
    '''
    def __init__(self):
        self.squares = [[Square(x, y) for y in range(8)] for x in range(8)]
    
    def draw(self, display):
        for row in self.squares:
            for square in row:
                square.draw(display)