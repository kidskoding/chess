import pygame

from classes.Piece import Piece

class Bishop(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if(self.isWhite):
            self.img = pygame.image.load('src/imgs/w_bishop.png')
        else:
            self.img = pygame.image.load('src/imgs/b_bishop.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))