import pygame

from piece import Piece

class Pawn(Piece):
    def __init__(self, pos, isWhite, board):
        super().__init__(pos, isWhite, board)
        if self.isWhite:
            self.img = pygame.image.load('imgs/w_pawn.png')
        else:
            self.img = pygame.image.load('imgs/b_pawn.png')
        self.img = pygame.transform.scale(self.img, (board.tile_width / 2, board.tile_height / 2))
        self.last_moved_two = False

    def get_available_moves(self, board):
        available_moves = []
        
        direction = -1 if self.isWhite else 1
        current_x, current_y = self.x, self.y
        
        default_move = board.get_square((current_x, current_y + direction))
        if 0 <= current_y + direction <= 7:
            if self.can_move(default_move):
                available_moves.append(default_move)
                if current_y == 6 or current_y == 1:
                    direction = direction - 1 if self.isWhite else direction + 1
                    extra_move = board.get_square((current_x, current_y + direction))
                    if 0 <= current_y + direction <= 7:
                        if self.can_move(extra_move):
                            available_moves.append(extra_move)
        
        temp_y = current_y - 1 if self.isWhite else current_y + 1
        
        available_captures = []
        if 0 < current_x <= 7 and 0 <= temp_y <= 7:
            available_captures.append(board.get_square((current_x - 1, temp_y)))
        if 0 <= current_x < 7 and 0 <= temp_y <= 7:
            available_captures.append(board.get_square((current_x + 1, temp_y)))

        for capture in available_captures:
            if self.can_move(capture):
                available_moves.append(capture)

        available_special_captures = []
        if 3 <= current_y <= 4:
            if board.white_turn:
                if current_x > 0 and isinstance(board.get_square((current_x - 1, current_y)).occupying_piece, Pawn) and board.get_square((current_x - 1, current_y)).occupying_piece.isWhite != self.isWhite:
                    if board.get_square((current_x - 1, current_y)).occupying_piece.last_moved_two:
                        available_special_captures.append(board.get_square((current_x - 1, current_y - 1)))

                if current_x < 7 and isinstance(board.get_square((current_x + 1, current_y)).occupying_piece, Pawn) and board.get_square((current_x + 1, current_y)).occupying_piece.isWhite != self.isWhite:
                    if board.get_square((current_x + 1, current_y)).occupying_piece.last_moved_two:
                        available_special_captures.append(board.get_square((current_x + 1, current_y - 1)))
            else:
                if current_x > 0 and isinstance(board.get_square((current_x - 1, current_y)).occupying_piece, Pawn) and board.get_square((current_x - 1, current_y)).occupying_piece.isWhite != self.isWhite:
                    if board.get_square((current_x - 1, current_y)).occupying_piece.last_moved_two:
                        available_special_captures.append(board.get_square((current_x - 1, current_y + 1)))

                if current_x < 7 and isinstance(board.get_square((current_x + 1, current_y)).occupying_piece, Pawn) and board.get_square((current_x + 1, current_y)).occupying_piece.isWhite != self.isWhite:
                    if board.get_square((current_x + 1, current_y)).occupying_piece.last_moved_two:
                        available_special_captures.append(board.get_square((current_x + 1, current_y + 1)))

        for capture in available_special_captures:
            available_moves.append(capture)

        return available_moves

    def can_move(self, new_square):
        delta_x = new_square.x - self.pos[0]
        delta_y = abs(new_square.y - self.pos[1])

        match delta_y:
            case 1:
                if new_square.x == 7 and new_square.y == 3:
                    print(delta_x, new_square.occupying_piece)
                if delta_x == 0 and new_square.occupying_piece is None:
                    return True
                if abs(delta_x) == 1 and new_square.occupying_piece is not None and new_square.occupying_piece.isWhite != self.isWhite:
                    return True
            case 2:
                if (self.pos[1] == 6 or self.pos[1] == 1) and delta_x == 0 and new_square.occupying_piece is None and not self.last_moved_two:
                    return True

        return False

