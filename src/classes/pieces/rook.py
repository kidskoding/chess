import pygame

from classes.piece import Piece

class Rook(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if(self.isWhite):
            self.img = pygame.image.load('src/imgs/w_rook.png')
        else:
            self.img = pygame.image.load('src/imgs/b_rook.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))
        
    def get_available_moves(self, board):
        available_moves = []
        current_x, current_y = self.x, self.y
        
        # Up
        for n in range(1, 8):
            if(current_y - n > -1): 
                up_column = board.get_square((current_x, current_y - n))
                if(up_column.occupying_piece != None):
                    if(up_column.occupying_piece.color != self.color): available_moves.append(up_column)     
                    break
                else: available_moves.append(up_column)
                
        # Down
        for n in range(1, 8):
            if(current_y + n < 8): 
                down_column = board.get_square((current_x, current_y + n))
                if(down_column.occupying_piece != None):
                    if(down_column.occupying_piece.color != self.color): available_moves.append(down_column)
                    break
                else: available_moves.append(down_column)
        
        # Left
        for n in range(1, 8):
            if(current_x - n > -1): 
                left_row = board.get_square((current_x - n, current_y))
                if(left_row.occupying_piece != None):
                    if(left_row.occupying_piece.color != self.color): available_moves.append(left_row)
                    break
                else: available_moves.append(left_row)
                
        # Right
        for n in range(1, 8):
            if(current_x + n < 8): 
                right_row = board.get_square((current_x + n, current_y))
                if(right_row.occupying_piece != None):
                    if(right_row.occupying_piece.color != self.color): available_moves.append(right_row)
                    break
                else: available_moves.append(right_row)
                
        return available_moves