import pygame

from classes.Board import Board

pygame.init()

screen = pygame.display.set_mode((Board.WIDTH, Board.HEIGHT))
pygame.display.set_caption('Chess')
board = Board()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                board.handle_click(mouse_x, mouse_y)

    clock.tick(60)
    board.draw(screen)
    pygame.display.update()

pygame.quit()