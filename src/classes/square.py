import pygame

class Square:
    # Each square has a width and height of 80 pixels
    WIDTH = 80
    HEIGHT = 80
    
    ''' 
        Squares have 
        an x and y index
        coordinate ( (x, y) )
        occupying piece
        highlight state (True or False)
        a draw and highlight color 
        a pygame rectangle that defines the square
    '''
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        self.pos = (x, y)
        self.abs_x = x * Square.WIDTH
        self.abs_y = y * Square.HEIGHT
        self.abs_pos = (self.abs_x, self.abs_y)
        self.coord = self.get_coord()
        self.occupying_piece = None
        self.isHighlighted = False
        self.isSelected = False
        self.isInCheck = False
        self.color = 'light' if (x + y) % 2 == 0 else 'dark'
        self.draw_color = (220, 208, 194) if self.color == 'light' else (53, 53, 53)
        self.highlight_color = (100, 249, 83) if self.color == 'light' else (0, 228, 10)
        self.select_color = (253, 255, 50)
        self.check_color = (255, 0, 0)
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            Square.WIDTH,
            Square.HEIGHT
        )
    
    # Get coordinate of Square in Chess terms (Coordinate (0, 0) would be 'a1')
    def get_coord(self):
        files = 'abcdefgh'
        return files[self.x] + str(8 - self.y)
    
    def draw(self, display):
        # Draw the square
        if self.isSelected:
            pygame.draw.rect(display, self.select_color, self.rect)
        elif self.isHighlighted:
            pygame.draw.rect(display, self.highlight_color, self.rect)
        elif self.isInCheck:
            pygame.draw.rect(display, self.check_color, self.rect)
        else:
            pygame.draw.rect(display, self.draw_color, self.rect)
           
        # Draw the piece
        if self.occupying_piece is not None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)