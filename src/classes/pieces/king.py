import pygame

from classes.Piece import Piece

class King(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if(self.isWhite):
            self.img = pygame.image.load('src/imgs/w_king.png')
        else:
            self.img = pygame.image.load('src/imgs/b_king.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))
        
    def get_available_moves(self, board):
        available_moves = []
        current_x, current_y = self.x, self.y
        
        # Up
        if(current_y - 1 > -1):
            up = board.get_square((current_x, current_y - 1))
            if(self.can_move(up) or self.can_capture(up) 
                and not board.is_in_check(up, board.current_color)):
                    available_moves.append(up)
                
        # Down
        if(current_y + 1 < 8):
            down = board.get_square((current_x, current_y + 1))
            if(self.can_move(down) or self.can_move(down) 
                and not board.is_in_check(down, board.current_color)):
                    available_moves.append(down)
                
        # Left
        if(current_x - 1 > -1):
            left = board.get_square((current_x - 1, current_y))
            if(self.can_move(left) or self.can_capture(left) 
                and not board.is_in_check(left, board.current_color)):
                    available_moves.append(left)
                
        # Right
        if(current_x + 1 < 8):
            right = board.get_square((current_x + 1, current_y))
            if(self.can_move(right) or self.can_capture(left) 
                and not board.is_in_check(right, board.current_color)):
                    available_moves.append(right)
                
        # Top Left Diagonal
        if(current_x - 1 > -1 and current_y - 1 > -1):
            top_left = board.get_square((current_x - 1, current_y - 1))
            if(self.can_move(top_left) or self.can_capture(top_left) 
                and not board.is_in_check(top_left, board.current_color)):
                    available_moves.append(top_left)
                
        # Top Right Diagonal
        if(current_x + 1 < 8 and current_y - 1 > -1):
            top_right = board.get_square((current_x + 1, current_y - 1))
            if(self.can_move(top_right) or self.can_capture(top_right) 
                and not board.is_in_check(top_right, board.current_color)):
                    available_moves.append(top_right)
        
        # Bottom Left Diagonal
        if(current_x - 1 > -1 and current_y + 1 < 8):
            bottom_left = board.get_square((current_x - 1, current_y + 1))
            if(self.can_move(bottom_left) or self.can_capture(bottom_left) 
                and not board.is_in_check(top_left, board.current_color)):
                    available_moves.append(bottom_left) 
                
        # Bottom Right Diagonal
        if(current_x + 1 < 8 and current_y + 1 < 8):
            bottom_right = board.get_square((current_x + 1, current_y + 1))
            if(self.can_move(bottom_right) or self.can_capture(bottom_right) 
                and not board.is_in_check(bottom_right, board.current_color)):
                    available_moves.append(bottom_right)
                
        return available_moves