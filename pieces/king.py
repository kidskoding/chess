import pygame

from piece import Piece

class King(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if self.isWhite:
            self.img = pygame.image.load('imgs/w_king.png')
        else:
            self.img = pygame.image.load('imgs/b_king.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))
        self.has_moved = False
        
    def get_available_moves(self, board):
        global left, top_left
        available_moves = []
        current_x, current_y = self.x, self.y
        
        # Up
        if current_y - 1 > -1:
            up = board.get_square((current_x, current_y - 1))
            if self.can_move(up) or self.can_move(up) and not board.is_in_check(up, board.white_turn):
                available_moves.append(up)
                
        # Down
        if current_y + 1 < 8:
            down = board.get_square((current_x, current_y + 1))
            if self.can_move(down) or self.can_move(down) and not board.is_in_check(down, board.white_turn):
                available_moves.append(down)
                
        # Left
        if current_x - 1 > -1:
            left = board.get_square((current_x - 1, current_y))
            if self.can_move(left) or self.can_move(left) and not board.is_in_check(left, board.white_turn):
                available_moves.append(left)
                
        # Right
        if current_x + 1 < 8:
            right = board.get_square((current_x + 1, current_y))
            if self.can_move(right) or self.can_move(left) and not board.is_in_check(right, board.white_turn):
                available_moves.append(right)
                
        # Top Left Diagonal
        if current_x - 1 > -1 and current_y - 1 > -1:
            top_left = board.get_square((current_x - 1, current_y - 1))
            if self.can_move(top_left) or self.can_move(top_left) and not board.is_in_check(top_left, board.white_turn):
                available_moves.append(top_left)
                
        # Top Right Diagonal
        if current_x + 1 < 8 and current_y - 1 > -1:
            top_right = board.get_square((current_x + 1, current_y - 1))
            if self.can_move(top_right) or self.can_move(top_right) and not board.is_in_check(top_right, board.white_turn):
                available_moves.append(top_right)
        
        # Bottom Left Diagonal
        if current_x - 1 > -1 and current_y + 1 < 8:
            bottom_left = board.get_square((current_x - 1, current_y + 1))
            if self.can_move(bottom_left) or self.can_move(bottom_left) and not board.is_in_check(top_left, board.white_turn):
                available_moves.append(bottom_left)
                
        # Bottom Right Diagonal
        if current_x + 1 < 8 and current_y + 1 < 8:
            bottom_right = board.get_square((current_x + 1, current_y + 1))
            if self.can_move(bottom_right) or self.can_move(bottom_right) and not board.is_in_check(bottom_right, board.white_turn):
                available_moves.append(bottom_right)
                
        return available_moves

    def can_move(self, new_square):
        delta_x = abs(new_square.x - self.pos[0])
        delta_y = abs(new_square.y - self.pos[1])
        return (delta_x == 1 or delta_y == 1) and (new_square.occupying_piece is None or new_square.occupying_piece.isWhite != self.isWhite)