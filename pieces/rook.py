import pygame

from piece import Piece

class Rook(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if self.isWhite:
            self.img = pygame.image.load('imgs/w_rook.png')
        else:
            self.img = pygame.image.load('imgs/b_rook.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))
        self.has_moved = False
        
    def get_available_moves(self, board):
        available_moves = []
        current_x, current_y = self.x, self.y
        
        # Up
        for n in range(1, 8):
            if current_y - n > -1:
                up_column = board.get_square((current_x, current_y - n))
                if up_column.occupying_piece is not None:
                    if up_column.occupying_piece.isWhite != self.isWhite: available_moves.append(up_column)
                    break
                else: available_moves.append(up_column)
                
        # Down
        for n in range(1, 8):
            if current_y + n < 8:
                down_column = board.get_square((current_x, current_y + n))
                if down_column.occupying_piece is not None:
                    if down_column.occupying_piece.isWhite != self.isWhite: available_moves.append(down_column)
                    break
                else: available_moves.append(down_column)
        
        # Left
        for n in range(1, 8):
            if current_x - n > -1:
                left_row = board.get_square((current_x - n, current_y))
                if left_row.occupying_piece is not None:
                    if left_row.occupying_piece.isWhite != self.isWhite: available_moves.append(left_row)
                    break
                else: available_moves.append(left_row)
                
        # Right
        for n in range(1, 8):
            if current_x + n < 8:
                right_row = board.get_square((current_x + n, current_y))
                if right_row.occupying_piece is not None:
                    if right_row.occupying_piece.isWhite != self.isWhite: available_moves.append(right_row)
                    break
                else: available_moves.append(right_row)
                
        return available_moves

    def can_move(self, new_square):
        delta_x = abs(new_square.x - self.pos[0])
        delta_y = abs(new_square.y - self.pos[1])
        return (delta_x == 0 or delta_y == 0) and (new_square.occupying_piece is None or new_square.occupying_piece.isWhite != self.isWhite)