class Piece:
    def __init__(self, pos, isWhite, board):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.isWhite = isWhite

    # Gets the available moves for a piece.
    # MUST OVERRIDE BY CLASSES THAT EXTEND IT!
    def get_available_moves(self, board):
        pass

    # Checks if the piece can move/capture to a specific square.
    # MUST OVERRIDE BY CLASSES THAT EXTEND IT!
    def can_move(self, new_square):
        pass

    def move(self, new_square, board, is_pawn = False, en_passant = False):
        if is_pawn:
            self.last_moved_two = (abs(new_square.y - self.y) == 2)
        board.set_pawn_movement(board.get_square((self.x, self.y)))
        self.x, self.y = new_square.pos
        new_square.occupying_piece = self
        if en_passant:
            board.get_square((new_square.x, new_square.y + 1 if board.white_turn else new_square.y - 1)).occupying_piece = None

    def capture(self, new_square, board):
        new_square.occupying_piece = None
        self.move(new_square, board)
