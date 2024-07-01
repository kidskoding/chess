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
    
    def __init__(self):
        self.tile_width = self.WIDTH // 8
        self.tile_height = self.HEIGHT // 8
        self.white_turn = True
        self.first_click_occurred = False
        self.squares = [[Square(x, y) for y in range(8)] for x in range(8)]
        self.previous_square = None
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
    
    def select_square(self, square):
        square.isSelected = True
        
    def clear_highlights(self):
        for row in self.squares:
            for square in row:
                if square.isSelected: square.isSelected = False
                elif square.isHighlighted: square.isHighlighted = False
    
    def handle_click(self, mx, my):
        x, y = mx // self.tile_width, my // self.tile_height
        selected_square = self.get_square((x, y))
        if(selected_square.occupying_piece != None 
            and ((self.white_turn and selected_square.occupying_piece.isWhite) 
            or (not self.white_turn and not selected_square.occupying_piece.isWhite))):
                self.handle_first_click(selected_square)
                self.previous_square = selected_square
                self.first_click_occurred = True
        if(self.first_click_occurred and (selected_square.occupying_piece == None 
            or (self.previous_square.occupying_piece.color != selected_square.occupying_piece.color))):
                self.handle_second_click(selected_square)
                self.clear_highlights()
                self.first_click_occurred = False
    
    # Handle first click (select a piece of one's color)
    def handle_first_click(self, selected_square):
        self.clear_highlights()
        
        # highlight square and show available moves
        self.select_square(selected_square)
        for square in selected_square.occupying_piece.get_available_moves(self):
            self.highlight_square(square)
                
    # Handle second click (moving/capturing a piece)
    def handle_second_click(self, selected_square):
        for square in self.previous_square.occupying_piece.get_available_moves(self):
            if selected_square == square:
                if selected_square.occupying_piece == None: self.previous_square.occupying_piece.move(selected_square)
                elif selected_square.occupying_piece.color != self.previous_square.occupying_piece.color: 
                    self.previous_square.occupying_piece.capture(selected_square)
                self.previous_square.occupying_piece = None
                self.previous_square = None
                return
    
    def draw(self, display):
        for row in self.squares:
            for square in row:
                square.draw(display)
                
    def setup_board(self):
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                if(piece != ''):
                    square = self.get_square((x, y))
                    self.get_square((2, 5)).occupying_piece = Pawn(
                        (2, 5),
                        False,
                        self
                    )
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