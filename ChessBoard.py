# Mihir Kaushal

import ChessPieces

# make ChessBoardSquare class, stores the color of square and the piece that is on it
class ChessBoardSquare:
    # constructor 
    def __init__(self, isWhite, piece):
        self.isWhite = isWhite
        self.piece = piece

    # print format
    def __repr__(self):
        if (self.piece == None) and (self.isWhite):
            return "\u25FB"
        elif(self.piece == None):
            return "\u25FC"
        else: 
            return str(self.piece)


# ChessBoard class
class ChessBoard:
    # constructor makes an empty board
    def __init__(self):
        # fills up empty 8x8 matrix with ChessBoardSquare objects, in check pattern
        self.board = [[None] * 8 for column in range(8)]
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if ((row + column) % 2 == 0):
                    self.board[row][column] = ChessBoardSquare(True, None)
                else:
                    self.board[row][column] = ChessBoardSquare(False, None)
        self.setBoard()

    # sets the borad up according to chess rules
    def setBoard(self):
        # first, fills the top row with the appropriate black pieces
        self.board[0][0] = ChessBoardSquare(True, ChessPieces.Rook(False))
        self.board[0][1] = ChessBoardSquare(False, ChessPieces.Knight(False))
        self.board[0][2] = ChessBoardSquare(True, ChessPieces.Bishop(False))
        self.board[0][3] = ChessBoardSquare(False, ChessPieces.Queen(False))
        self.board[0][4] = ChessBoardSquare(True, ChessPieces.King(False))
        self.board[0][5] = ChessBoardSquare(False, ChessPieces.Bishop(False))
        self.board[0][6] = ChessBoardSquare(True, ChessPieces.Knight(False))
        self.board[0][7] = ChessBoardSquare(False, ChessPieces.Rook(False))

        # second, fills up the second row with black pawns
        for column in range(len(self.board[1])):
            if (column % 2 == 0):
                self.board[1][column] = ChessBoardSquare(False, ChessPieces.Pawn(False))
            else:
                self.board[1][column] = ChessBoardSquare(True, ChessPieces.Pawn(False))
        
        # third, fills up second row from bottom with white pawns
        for column in range(len(self.board[6])):
            if (column % 2 == 0):
                self.board[6][column] = ChessBoardSquare(True, ChessPieces.Pawn(True))
            else:
                self.board[6][column] = ChessBoardSquare(False, ChessPieces.Pawn(True))

        # forth, fills up bottom row with the appropriate white pieces
        self.board[7][0] = ChessBoardSquare(False, ChessPieces.Rook(True))
        self.board[7][1] = ChessBoardSquare(True, ChessPieces.Knight(True))
        self.board[7][2] = ChessBoardSquare(False, ChessPieces.Bishop(True))
        self.board[7][3] = ChessBoardSquare(True, ChessPieces.Queen(True))
        self.board[7][4] = ChessBoardSquare(False, ChessPieces.King(True))
        self.board[7][5] = ChessBoardSquare(True, ChessPieces.Bishop(True))
        self.board[7][6] = ChessBoardSquare(False, ChessPieces.Knight(True))
        self.board[7][7] = ChessBoardSquare(True, ChessPieces.Rook(True))

    
    # TODO def move(fromRow, fromColumn, toRow, toColumn):

    
    def printBoard(self):
        for row in self.board:
            print(row)

obj = ChessBoard()
obj.printBoard()

