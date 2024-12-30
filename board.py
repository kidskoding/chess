import pygame

from square import Square

from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook

def highlight_square(square):
    square.isHighlighted = True

def select_square(square):
    square.isSelected = True

def highlight_king(king_square, shouldHighlight):
    king_square.isInCheck = shouldHighlight

class Board:
    # Board has a width and height of 640 pixels
    WIDTH = 640
    HEIGHT = 640

    def __init__(self):
        self.tile_width = self.WIDTH // 8
        self.tile_height = self.HEIGHT // 8
        self.white_turn = True
        self.first_click_occurred = False
        self.successful_move = False
        self.squares = [[Square(x, y) for y in range(8)] for x in range(8)]
        self.original_square = None
        self.config = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ]
        self.setup_board()

    def get_square(self, pos):
        for row in self.squares:
            for square in row:
                if (square.x, square.y) == (pos[0], pos[1]):
                    return square

    def get_piece(self):
        return self.get_square(self).occupying_piece

    def get_pieces_on_board(self):
        pieces = []
        for row in self.squares:
            for square in row:
                if square.occupying_piece is not None:
                    pieces.append(square.occupying_piece)
        return pieces

    def get_king_square(self, color):
        for row in self.squares:
            for square in row:
                if isinstance(square.occupying_piece, King) and square.occupying_piece.isWhite is (color is True):
                    return square
        return None

    def set_pawn_movement(self, ignore_square = None):
        for row in self.squares:
            for square in row:
                if isinstance(square.occupying_piece, Pawn) and square.occupying_piece.isWhite is (self.white_turn is True):
                    if ignore_square is not None and square == ignore_square:
                        continue
                    square.occupying_piece.last_moved_two = False
        return None

    def clear_highlights(self):
        for row in self.squares:
            for square in row:
                if square.isSelected: square.isSelected = False
                elif square.isHighlighted: square.isHighlighted = False
                if not (square.occupying_piece and isinstance(square.occupying_piece, King) and self.is_in_check(self.white_turn)):
                    square.isInCheck = False

    def handle_click(self, mx, my, screen):
        x, y = mx // self.tile_width, my // self.tile_height
        selected_square = self.get_square((x, y))
        if(((self.is_in_check(self.white_turn) and isinstance(selected_square.occupying_piece, King))
            or (not self.is_in_check(self.white_turn) and selected_square.occupying_piece is not None))
            and ((self.white_turn and selected_square.occupying_piece.isWhite)
            or (not self.white_turn and not selected_square.occupying_piece.isWhite))):
            self.handle_first_click(selected_square)
            self.original_square = selected_square
            self.first_click_occurred = True

        if self.first_click_occurred and (selected_square.occupying_piece is None or (self.original_square.occupying_piece.isWhite != selected_square.occupying_piece.isWhite)):
            self.handle_second_click(selected_square, screen)
            self.clear_highlights()
            self.first_click_occurred = False

    # Handle first click (select a piece of one's color)
    def handle_first_click(self, selected_square):
        self.clear_highlights()
        self.original_square = selected_square

        # highlight square and show available moves
        if not self.is_in_check(self.white_turn):
            select_square(selected_square)
        for square in selected_square.occupying_piece.get_available_moves(self):
            highlight_square(square)

    # Handle second click (moving/capturing a piece)
    def handle_second_click(self, selected_square, screen):
        for square in self.original_square.occupying_piece.get_available_moves(self):
            if selected_square == square:
                if selected_square.occupying_piece is None:
                    if isinstance(self.original_square.occupying_piece, Pawn) and self.original_square.x != selected_square.x and selected_square.occupying_piece is None:
                        self.original_square.occupying_piece.move(selected_square, self, True, True)
                    else:
                        self.original_square.occupying_piece.move(selected_square, self, isinstance(self.original_square.occupying_piece, Pawn), False)
                    self.successful_move = True

                    if isinstance(self.original_square.occupying_piece, King) or isinstance(self.original_square.occupying_piece, Rook):
                        self.original_square.occupying_piece.has_moved = True
                    if (isinstance(self.original_square.occupying_piece, Pawn) and self.original_square.occupying_piece.isWhite and selected_square.y == 0) or (isinstance(self.original_square.occupying_piece, Pawn) and (not self.original_square.occupying_piece.isWhite) and selected_square.y == 7):
                        self.promote_pawn(selected_square, screen)
                elif selected_square.occupying_piece.isWhite != self.original_square.occupying_piece.isWhite:
                    self.original_square.occupying_piece.capture(selected_square, self)
                    self.successful_move = True

                    if isinstance(self.original_square.occupying_piece, King) or isinstance(self.original_square.occupying_piece, Rook):
                        self.original_square.occupying_piece.has_moved = True
                    if (isinstance(self.original_square.occupying_piece, Pawn) and self.original_square.occupying_piece.isWhite and selected_square.y == 0) or (isinstance(self.original_square.occupying_piece, Pawn) and (not self.original_square.occupying_piece.isWhite) and selected_square.y == 7):
                        self.promote_pawn(selected_square, screen)

                if self.successful_move:
                    self.original_square.occupying_piece = None
                    self.original_square = None
                    self.white_turn = not self.white_turn
                    if self.is_in_check(self.white_turn):
                        highlight_king(self.get_king_square(self.white_turn), True)
                    self.successful_move = False

    def draw_board(self, display):
        for row in self.squares:
            for square in row:
                square.draw(display)

    def is_in_check(self, color, new_square = None):
        king_square = self.get_king_square(color)
        if king_square is None:
            pygame.quit()
            raise TimeoutError('Game cannot be played! In order to play Chess, both colors must have a king on the board!')

        if new_square is not None and hasattr(new_square, 'occupying_piece'):
            piece = new_square.occupying_piece
            if piece is not None:
                available_moves = piece.get_available_moves(self)
                for move in available_moves:
                    if move.occupying_piece is not None and move.occupying_piece.can_move(king_square):
                        return True
        else:
            for piece in self.get_pieces_on_board():
                if piece.isWhite != color:
                    available_moves = piece.get_available_moves(self)
                    if king_square in available_moves:
                        return True
        return False

    def setup_board(self):
        for y, row in enumerate(self.config):
            for x, piece in enumerate(row):
                if piece != '':
                    square = self.get_square((x, y))

                    match piece[1]:
                        case 'R':
                            square.occupying_piece = Rook((x, y), True if piece[0] == 'w' else False, self)
                        case 'N':
                            square.occupying_piece = Knight((x, y), True if piece[0] == 'w' else False, self)
                        case 'B':
                            square.occupying_piece = Bishop((x, y), True if piece[0] == 'w' else False, self)
                        case 'Q':
                            square.occupying_piece = Queen((x, y), True if piece[0] == 'w' else False, self)
                        case 'K':
                            square.occupying_piece = King((x, y), True if piece[0] == 'w' else False, self)
                        case 'P':
                            square.occupying_piece = Pawn((x, y), True if piece[0] == 'w' else False, self)

    def promote_pawn(self, square, display):
        # Create a dialog in the center of the screen
        dialog_width, dialog_height = 320, 250
        dialog_x = (self.WIDTH - dialog_width) // 2
        dialog_y = (self.HEIGHT - dialog_height) // 2
        dialog_rect = pygame.Rect(dialog_x, dialog_y, dialog_width, dialog_height)

        # Create font and text
        font = pygame.font.Font(None, 36)
        text = font.render("Pick a piece to promote to", True, (0, 0, 0))
        text_rect = text.get_rect(center = (dialog_x + dialog_width // 2, dialog_y + 30))

        # Create buttons for choices
        button_width, button_height = 150, 30
        buttons = {
            "queen": pygame.Rect(dialog_x + 85, dialog_y + 70, button_width, button_height),
            "rook": pygame.Rect(dialog_x + 85, dialog_y + 110, button_width, button_height),
            "bishop": pygame.Rect(dialog_x + 85, dialog_y + 150, button_width, button_height),
            "knight": pygame.Rect(dialog_x + 85, dialog_y + 190, button_width, button_height)
        }

        # Draw the dialog and buttons
        running = True
        choice = None
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for key, button in buttons.items():
                        if button.collidepoint(mouse_pos):
                            choice = key
                            running = False

            # Draw dialog
            pygame.draw.rect(display, (255, 255, 255), dialog_rect)
            pygame.draw.rect(display, (0, 0, 0), dialog_rect, 2)
            display.blit(text, text_rect)

            # Draw buttons
            for key, button in buttons.items():
                pygame.draw.rect(display, (200, 200, 200), button)
                pygame.draw.rect(display, (0, 0, 0), button, 2)
                button_text = font.render(key.capitalize(), True, (0, 0, 0))
                button_text_rect = button_text.get_rect(center = button.center)
                display.blit(button_text, button_text_rect)

            pygame.display.flip()

        # Promote the pawn based on the choice
        match choice:
            case 'queen':
                square.occupying_piece = Queen((square.x, square.y), square.occupying_piece.isWhite, self)
            case 'rook':
                square.occupying_piece = Rook((square.x, square.y), square.occupying_piece.isWhite, self)
            case 'bishop':
                square.occupying_piece = Bishop((square.x, square.y), square.occupying_piece.isWhite, self)
            case 'knight':
                square.occupying_piece = Knight((square.x, square.y), square.occupying_piece.isWhite, self)