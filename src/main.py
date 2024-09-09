import pygame

from classes.board import Board

pygame.init()

screen = pygame.display.set_mode((Board.WIDTH, Board.HEIGHT))
pygame.display.set_caption('Chess')
board = Board()
clock = pygame.time.Clock()

running = True
while running:
    white_king_square = board.get_king_square('white')
    black_king_square = board.get_king_square('black')
    if(white_king_square is None or black_king_square is None):
        pygame.quit()
        raise TimeoutError('Game cannot be played! In order to play Chess, both colors must have a king on the board!')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                board.handle_click(mouse_x, mouse_y)

    clock.tick(60)
    board.draw_board(screen)
    pygame.display.update()

pygame.quit()