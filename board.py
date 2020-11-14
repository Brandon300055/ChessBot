from piece import Piece


class Board:
    # board = []
    # removedPiece = []

    selectedPiece = False
    selectPieceName = False

    def __init__(self, board):
        self.board = board
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

    # get moves for selected piece
    def moves(self):
        # case for if no piece is select
        if self.selectedPiece == False:
            print("No Piece Select")
            return

        piece = Piece(self.board, self.selectedPiece)
        # print(piece.getMoves())
        return piece.getMoves()

    # updates board with select piece
    def move(self, toX, toY):
        # case for if no piece is select
        if self.selectedPiece == False:
            print("No Piece Select")
            return

        # check if move is available


        # move the piece
        self.board[toX][toY] = self.board[self.selectedPiece[0]][self.selectedPiece[1]]
        self.board[self.selectedPiece[0]][self.selectedPiece[1]] = False

    # returns list for all possible moves for piece
    def getAllMoves(self, color):
        x = 0
        y = 0
        movesPerPiece = []
        for i in self.board:
            for j in i:
                if str(self.board[x][y])[0] == color:
                    self.selectedPiece = [x, y] # return the coordinates
                    board = self.board
                    selectedPiece = self.selectedPiece
                    piece = Piece(board, selectedPiece)
                    moves = piece.getMoves()
                    movesPerPiece += [[str(self.board[x][y]), moves]]
                y += 1
            y = 0
            x += 1
        self.selectedPiece = False

        return movesPerPiece

    # def getMove
    #
    # def recursion(self):
    #     pass