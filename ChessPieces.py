# Mihir Kaushal

# parent class for all chess pieces
class ChessPiece:
    def __init__(self, isWhite, points):
        self.isWhite = isWhite
        self.points = points

class Pawn(ChessPiece):
    def __init__(self, isWhite):
        super().__init__(isWhite, 1)

    def __repr__(self):
        if self.isWhite:
            return "\u2659"
        else:
            return "\u265F"
        
class King(ChessPiece):
    def __init__(self, isWhite):
        super().__init__(isWhite, 67)

    def __repr__(self):
        if self.isWhite:
            return "\u2654"
        else:
            return "\u265A"
        
class Queen(ChessPiece):
    def __init__(self, isWhite):
        super().__init__(isWhite, 9)

    def __repr__(self):
        if self.isWhite:
            return "\u2655"
        else:
            return "\u265B"

class Rook(ChessPiece):
    def __init__(self, isWhite):
        super().__init__(isWhite, 5)

    def __repr__(self):
        if self.isWhite:
            return "\u2656"
        else:
            return "\u265C"

class Bishop(ChessPiece):
    def __init__(self, isWhite):
        super().__init__(isWhite, 3)

    def __repr__(self):
        if self.isWhite:
            return "\u2657"
        else:
            return "\u265D"

class Knight(ChessPiece):
    def __init__(self, isWhite):
        super().__init__(isWhite, 3)

    def __repr__(self):
        if self.isWhite:
            return "\u2658"
        else:
            return "\u265E"

