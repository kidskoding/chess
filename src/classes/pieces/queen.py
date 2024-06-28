import pygame

from classes.Piece import Piece

class Queen(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if(self.isWhite):
            self.img = pygame.image.load('src/imgs/w_queen.png')
        else:
            self.img = pygame.image.load('src/imgs/b_queen.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))