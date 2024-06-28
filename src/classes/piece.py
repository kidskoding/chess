import pygame

class Piece():
    def __init__(self, pos, isWhite, board):
        self.pos = pos
        self.isWhite = isWhite
        self.isClicked = False
        
    def get_available_moves(self, board):
        pass