import pygame

from classes.piece import Piece

class Bishop(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if(self.isWhite):
            self.img = pygame.image.load('src/imgs/w_bishop.png')
        else:
            self.img = pygame.image.load('src/imgs/b_bishop.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))
        
    def get_available_moves(self, board):
        available_moves = []
        current_x, current_y = self.x, self.y
        
        # Top right diagonal
        for n in range(1, 8):
            if(current_x + n < 8 and current_y - n > -1): 
                topright_diagonal = board.get_square((current_x + n, current_y - n))
                if(topright_diagonal.occupying_piece != None):
                    if(topright_diagonal.occupying_piece.color != self.color): available_moves.append(topright_diagonal)     
                    break
                else: available_moves.append(topright_diagonal)
                
        # Bottom right diagonal
        for n in range(1, 8):
            if(current_x + n < 8 and current_y + n < 8):
                bottomright_diagonal = board.get_square((current_x + n, current_y + n))
                if(bottomright_diagonal.occupying_piece != None):
                    if(bottomright_diagonal.occupying_piece.color != self.color): available_moves.append(bottomright_diagonal)
                    break
                else: available_moves.append(bottomright_diagonal)
        
        # Bottom left diagonal
        for n in range(1, 8):
            if(current_x - n > -1 and current_y + n < 8): 
                bottomleft_diagonal = board.get_square((current_x - n, current_y + n))
                if(bottomleft_diagonal.occupying_piece != None):
                    if(bottomleft_diagonal.occupying_piece.color != self.color): available_moves.append(bottomleft_diagonal)
                    break
                else: available_moves.append(bottomleft_diagonal)
                
        # Top left diagonal
        for n in range(1, 8):
            if(current_x - n > -1 and current_y - n > -1): 
                topleft_diagonal = board.get_square((current_x - n, current_y - n))
                if(topleft_diagonal.occupying_piece != None):
                    if(topleft_diagonal.occupying_piece.color != self.color): available_moves.append(topleft_diagonal)
                    break
                else: available_moves.append(topleft_diagonal)
                
        return available_moves