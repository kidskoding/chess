import pygame
import os

from classes.Board import Board
from classes.Square import Square

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

    clock.tick(60)
    board.draw(screen)
    pygame.display.update()

pygame.quit()