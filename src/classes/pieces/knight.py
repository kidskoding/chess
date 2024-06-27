import pygame

from classes.Piece import Piece

class Knight(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if(self.isWhite):
            self.img = pygame.image.load('src/imgs/w_knight.png')
        else:
            self.img = pygame.image.load('src/imgs/b_knight.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))