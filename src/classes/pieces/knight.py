import pygame

from classes.piece import Piece

class Knight(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if(self.isWhite):
            self.img = pygame.image.load('src/imgs/w_knight.png')
        else:
            self.img = pygame.image.load('src/imgs/b_knight.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))
        self.img = pygame.transform.flip(self.img, True, False)
        
    def get_available_moves(self, board):
        available_moves = []
        
        current_x, current_y = self.x, self.y
        
        # Lower Side L shapes: left side and right side
        if(current_x - 2 > -1 and current_y + 1 < 8):
            lower_side_left_square = board.get_square((current_x - 2, current_y + 1))
            if(self.can_move(lower_side_left_square) or self.can_capture(lower_side_left_square)): 
                available_moves.append(lower_side_left_square)        
        if(current_x + 2 < 8 and current_y + 1 < 8):
            lower_side_right_square = board.get_square((current_x + 2, current_y + 1))
            if(self.can_move(lower_side_right_square) or self.can_capture(lower_side_right_square)):
                available_moves.append(lower_side_right_square)
        
        # Upper Side L shapes: left side and right side
        if(current_x - 2 > -1 and current_y - 1 > -1):
            upper_side_left_square = board.get_square((current_x - 2, current_y - 1))
            if(self.can_move(upper_side_left_square) or self.can_capture(upper_side_left_square)):
                available_moves.append(upper_side_left_square)
        if(current_x + 2 < 8 and current_y - 1 > -1):
            upper_side_right_square = board.get_square((current_x + 2, current_y - 1))
            if(self.can_move(upper_side_right_square) or self.can_capture(upper_side_right_square)):
                available_moves.append(upper_side_right_square)
        
        # Lower L shapes: left and right
        if(current_x - 1 > -1 and current_y + 2 < 8):
            lower_left_square = board.get_square((current_x - 1, current_y + 2))
            if(self.can_move(lower_left_square) or self.can_capture(lower_left_square)):
                available_moves.append(lower_left_square)
        if(current_x + 1 < 8 and current_y + 2 < 8):
            lower_right_square = board.get_square((current_x + 1, current_y + 2))
            if(self.can_move(lower_right_square) or self.can_capture(lower_right_square)):
                available_moves.append(lower_right_square)
        
        # Upper L shapes: left and right
        if(current_x - 1 > -1 and current_y - 2 > -1):
            upper_left_square = board.get_square((current_x - 1, current_y - 2))
            if(self.can_move(upper_left_square) or self.can_capture(upper_left_square)): 
                available_moves.append(upper_left_square)
        if(current_x + 1 < 8 and current_y - 2 > -1):
            upper_right_square = board.get_square((current_x + 1, current_y - 2))
            if(self.can_move(upper_right_square) or self.can_capture(upper_right_square)): 
                available_moves.append(upper_right_square)
        
        return available_moves