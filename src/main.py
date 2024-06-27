import pygame

from classes.Board import Board
from classes.Square import Square

pygame.init()

screen = pygame.display.set_mode((Board.WIDTH, Board.HEIGHT))
pygame.display.set_caption('Chess')
board = Board()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                square_x = mouse_x // Square.WIDTH
                square_y = mouse_y // Square.HEIGHT
                if 0 <= square_x < 8 and 0 <= square_y < 8:
                    square = board.squares[square_x][square_y]
                    print(square.get_coord())
    
    screen.fill((255, 255, 255))
    board.draw(screen)
    pygame.display.update()
            
pygame.quit()