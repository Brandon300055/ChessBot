class Piece:
    board = []
    selectedPiece = []
    moves = [] # moves that piece can make

    def __init__(self, board, selectedPiece):
        self.board = board
        self.selectedPiece = selectedPiece
        self.piece = board[selectedPiece[0]][selectedPiece[1]]

    # returns all moves that pawn can move
    def pawn(self):
        # case for white or black
        white = (self.piece[0] == 'w')
        color = ("w" if white else "b")

        # the first space in front of the piece
        firstSpace = [self.selectedPiece[0] + (-1 if white else 1), self.selectedPiece[1]]
        firstSpacePiece = self.board[firstSpace[0]][firstSpace[1]]
        # left right attack attract case if space is not off the bord and an enemy unit is in a left diagonal space
        leftAttack = [self.selectedPiece[0] + (-1 if white else 1), self.selectedPiece[1] - 1]
        rightAttack = [self.selectedPiece[0] + (-1 if white else 1), self.selectedPiece[1] + 1]


        # check if firstSpace is empty
        blocked = True # boolean for if path is blocked
        if (firstSpacePiece == False) and (str(firstSpacePiece)[0] != color):
            blocked = False
            self.moves += [firstSpace]

        # case for second space move by checking if selectedPiece is on starting line and
        if blocked == False and ((white and self.selectedPiece[0] == 6) or (white == False and self.selectedPiece[0] == 1)):
            # is not blocked and is on print first line
            self.moves += [[self.selectedPiece[0] + (-2 if white else 2), self.selectedPiece[1]]]

        # check left attach
        if self.selectedPiece[1] - 1 >= 0:
            leftAttactPiece = self.board[leftAttack[0]][leftAttack[1]]
            if (leftAttactPiece != False) and (str(leftAttactPiece)[0] != color):
                self.moves += [leftAttack]

        # check right attach
        if self.selectedPiece[1] + 1 <= 7:
            rightAttactPiece = self.board[rightAttack[0]][rightAttack[1]]
            if (rightAttactPiece != False) and (str(rightAttactPiece)[0] != color):
                self.moves += [rightAttack]

        return self.moves