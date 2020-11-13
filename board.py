from piece import Piece


class Board:
    # board = []
    # removedPiece = []

    selectedPiece = False
    selectPieceName = False

    def __init__(self):
        self.board = [
            #  0    #  1   # 2    # 3    # 4   # 5    # 6    # 7
            ["br1", "bn1", "bb1", "bk",  "bq", "bb2", "bn2", "br2"],   #0
            ["bp0", "bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7"], #1
            [False, False, False, False, False, False, False, False], #2
            [False, False, False, False, False, False, False, False], #3
            [False, False, False, "wr1", False, False, False, False], #4
            [False, False, False, False, False, False, False, False], #5
            ["wp0", "wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7"], #6
            [False, "wn1", "wb1", "wk", "wq", "wb2", "wn2", "wr2"],  # 0
        ]

        self.removedPiece = [],

    def printBoard(self):
        for i in self.board:
            print(i)

    # returns the coordinates of the piece named
    def selectPiece(self, name):
        self.selectPieceName = name
        x = 0
        y = 0
        for i in self.board:
            for j in i:
                if self.board[x][y] == name:
                    self.selectedPiece = [x, y] # return the coordinates
                    return self
                y += 1
            y = 0
            x += 1
        self.selectedPiece = False
        return self # case for if piece not found

    # returns list for all possible moves for piece
    def moves(self):
        # case for if no piece is select
        if self.selectedPiece == False:
            print("No Piece Select")
            return

        piece = Piece(self.board, self.selectedPiece)
        print(piece.rook())
        return

    def move(self, toX, toY):
        # case for if no piece is select
        if self.selectedPiece == False:
            print("No Piece Select")
            return

        # move the piece
        self.board[toX][toY] = self.board[self.selectedPiece[0]][self.selectedPiece[1]]
        self.board[self.selectedPiece[0]][self.selectedPiece[1]] = False

