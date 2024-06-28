import pygame

from classes.Square import Square
from classes.pieces.Bishop import Bishop
from classes.pieces.King import King
from classes.pieces.Knight import Knight
from classes.pieces.Pawn import Pawn
from classes.pieces.Queen import Queen
from classes.pieces.Rook import Rook

class Board:
    # Board has a width and height of 640 pixels
    WIDTH = 640
    HEIGHT = 640
    
    '''
        A board has the following:
        - A 2D list of Squares
        - A 2D list configuration of the starting board
    '''
    def __init__(self):
        self.tile_width = self.WIDTH // 8
        self.tile_height = self.HEIGHT // 8
        self.white_turn = True
        self.squares = [[Square(x, y) for y in range(8)] for x in range(8)]
        self.config = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.setup_board()
    
    def get_square(self, pos):
        for row in self.squares:
            for square in row:
                if (square.x, square.y) == (pos[0], pos[1]):
                    return square
                
    def get_piece(self, pos):
        return self.get_square(self, pos).occupying_piece
                
    def highlight_square(self, square):
        square.isHighlighted = True
    
    def handle_click(self, mx, my):
        for row in self.squares:
            for square in row:
                square.isHighlighted = False
        x, y = mx // self.tile_width, my // self.tile_height
        clicked_square = self.get_square((x, y))
        if clicked_square.occupying_piece != None:
            self.highlight_square(clicked_square)
            available_moves = clicked_square.occupying_piece.get_available_moves(self)
            for square in available_moves:
                self.highlight_square(square)
    
    def draw(self, display):
        for row in self.squares:
            for square in row:
                square.draw(display)
                
    def setup_board(self):
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                self.get_square((2, 5)).occupying_piece = Pawn(
                    (2, 5),
                    False,
                    self
                )
                if(piece != ''):
                    square = self.get_square((x, y))
                      
                    if(piece[1] == 'R'):
                        square.occupying_piece = Rook(
                            (x, y), 
                            True if piece[0] == 'w' else False,
                            self
                        )
                    elif(piece[1] == 'N'):
                        square.occupying_piece = Knight(
                            (x, y), 
                            True if piece[0] == 'w' else False,
                            self
                        )
                    elif(piece[1] == 'B'):
                        square.occupying_piece = Bishop(
                            (x, y), 
                            True if piece[0] == 'w' else False,
                            self
                        )
                    elif(piece[1] == 'Q'):
                        square.occupying_piece = Queen(
                            (x, y), 
                            True if piece[0] == 'w' else False,
                            self
                        )
                    elif(piece[1] == 'K'):
                        square.occupying_piece = King(
                            (x, y), 
                            True if piece[0] == 'w' else False,
                            self
                        )
                    elif(piece[1] == 'P'):
                        square.occupying_piece = Pawn(
                            (x, y), 
                            True if piece[0] == 'w' else False,
                            self
                        )