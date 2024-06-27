import pygame

class Piece():
    def __init__(self, pos, isWhite, board):
        self.pos = pos
        self.isWhite = isWhite
        self.board = board