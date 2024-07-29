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
        self.current_color = 'white'
        self.first_click_occurred = False
        self.successful_move = False
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
                if((square.x, square.y) == (pos[0], pos[1])):
                    return square
                
    def get_piece(self, pos):
        return self.get_square(self, pos).occupying_piece
    
    def get_pieces_on_board(self):
        pieces = []
        for row in self.squares:
            for square in row:
                if square.occupying_piece != None:
                    pieces.append(square.occupying_piece)
        return pieces
    
    def get_king_square(self, color):
        for row in self.squares:
            for square in row:
                if isinstance(square.occupying_piece, King) and square.occupying_piece.isWhite == (color == 'white'):
                    return square
        return None
                
    def highlight_square(self, square):
        square.isHighlighted = True
        
    def select_square(self, square):
        square.isSelected = True
        
    def highlight_king(self, king_square, shouldHighlight):
        king_square.isInCheck = shouldHighlight
    
    def clear_highlights(self):
        for row in self.squares:
            for square in row:
                if square.isSelected: square.isSelected = False
                elif square.isHighlighted: square.isHighlighted = False
                if not (square.occupying_piece and isinstance(square.occupying_piece, King) and self.is_in_check(self.current_color)):
                    square.isInCheck = False
    
    def handle_click(self, mx, my):
        x, y = mx // self.tile_width, my // self.tile_height
        selected_square = self.get_square((x, y))
        if( ((self.is_in_check(self.current_color) and isinstance(selected_square.occupying_piece, King)) 
            or (not self.is_in_check(self.current_color) and selected_square.occupying_piece != None))
            and ((self.white_turn and selected_square.occupying_piece.isWhite) 
            or (not self.white_turn and not selected_square.occupying_piece.isWhite)) ):
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
        if(not self.is_in_check(self.current_color)):
            self.select_square(selected_square)
        for square in selected_square.occupying_piece.get_available_moves(self):
            self.highlight_square(square)
                
    # Handle second click (moving/capturing a piece)
    def handle_second_click(self, selected_square):
        for square in self.previous_square.occupying_piece.get_available_moves(self):
            if selected_square == square:
                if selected_square.occupying_piece == None: 
                    self.previous_square.occupying_piece.move(selected_square)
                    self.successful_move = True
                elif selected_square.occupying_piece.color != self.previous_square.occupying_piece.color: 
                    self.previous_square.occupying_piece.capture(selected_square)
                    self.successful_move = True
                if self.successful_move:
                    self.previous_square.occupying_piece = None
                    self.previous_square = None
                    self.white_turn = not self.white_turn
                    self.current_color = 'white' if self.white_turn else 'black'
                    if(self.is_in_check(self.current_color)):
                        print(f'{self.current_color.capitalize()} king is in check!', )
                        self.highlight_king(self.get_king_square(self.current_color), True)
                    self.successful_move = False
    
    def draw_board(self, display):
        for row in self.squares:
            for square in row:
                square.draw(display)
    
    def is_in_check(self, new_square, color):
        piece = new_square.occupying_piece
        king_square = self.get_king_square(color)
        if piece is not None:
            available_moves = piece.get_available_moves(self)
            for move in available_moves:
                if(move.occupying_piece is not None 
                    and move.occupying_piece.can_capture(king_square)):
                        return True
        return False
    
    def is_in_check(self, color):
        pieces_on_board = self.get_pieces_on_board()
        king_square = self.get_king_square(color)
        if king_square is None:
            pygame.quit()
            raise TimeoutError('Game cannot be played! In order to play Chess, both colors must have a king on the board!')
        
        for piece in self.get_pieces_on_board():
            if piece.isWhite != (color == 'white'):
                available_moves = piece.get_available_moves(self)
                if king_square in available_moves:
                    return True
        return False
                
    def setup_board(self):
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
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