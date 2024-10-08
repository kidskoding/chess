import pygame

class Piece():
    def __init__(self, pos, isWhite, board):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.isWhite = isWhite
        self.color = 'white' if self.isWhite else 'black'
        
    # Gets the available moves for a piece.
    # MUST OVERRIDE BY CLASSES THAT EXTEND IT!
    def get_available_moves(self, board):
        pass
    
    def move(self, new_square):
        self.x, self.y = new_square.pos
        new_square.occupying_piece = self
        
    def capture(self, new_square):
        new_square.occupying_piece = None
        self.move(new_square)
    
    # Checks if the piece can move to a different square on the board
    def can_move(self, new_square):
        return new_square.occupying_piece == None
    
    # Checks if the piece can capture a different piece on a different square
    def can_capture(self, new_square):
        return new_square.occupying_piece != None and self.color != new_square.occupying_piece.color