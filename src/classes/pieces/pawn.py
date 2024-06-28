import pygame

from classes.Piece import Piece

class Pawn(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        self.x = pos[0]
        self.y = pos[1]
        if(self.isWhite):
            self.img = pygame.image.load('src/imgs/w_pawn.png')
        else:
            self.img = pygame.image.load('src/imgs/b_pawn.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))
           
    def get_available_moves(self, board):
        available_moves = []
        
        direction = -1 if self.isWhite else 1
        current_x, current_y = self.x, self.y
        
        original_square = board.get_square((current_x, current_y + direction))
        if(not original_square.is_occupied()):
            available_moves.append(original_square)        
            if(current_y == 6 or current_y == 1):
                direction = direction - 1 if self.isWhite else direction + 1
                available_moves.append(board.get_square((current_x, current_y + direction)))
        
        temp_y = current_y - 1 if self.isWhite else current_y + 1
        
        available_captures = []
        if(current_x > 0): available_captures.append(board.get_square((current_x - 1, temp_y)))
        if(current_x < 7): available_captures.append(board.get_square((current_x + 1, temp_y)))

        for capture in available_captures:
            if capture.occupying_piece != None:
                available_moves.append(capture)
        
        return available_moves