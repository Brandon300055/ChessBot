class Piece:
    board = []
    selectedPiece = []
    moves = [] # moves that piece can make

    def __init__(self, board, selectedPiece):
        self.board = board
        self.selectedPiece = selectedPiece
        self.piece = board[selectedPiece[0]][selectedPiece[1]]
        self.white = (self.piece[0] == 'w')
        self.color = ("w" if  self.white else "b")

    # returns all moves from selected piece is pawn
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

    # returns all moves from selected piece is rook
    def rook(self):

        # return self.board[self.selectedPiece[0] - -3][self.selectedPiece[1] - -9]

        for i in range(4):
            Ycheck = [-1, 0, 0, 1][i]
            Xcheck = [0, -1, 1, 0][i]
            addY = [-1, 0, 0, 1][i]
            addX = [0, -1, 1, 0][i]

            spaceChecking = self.board[self.selectedPiece[0] - Ycheck][self.selectedPiece[1] - Xcheck]

            # print(1 - ((i + 1) % 2))
            # print(1 - (i % 2))
            # print( ((i ) % 3))
            # print (self.selectedPiece[0] - Ycheck)

            while (spaceChecking == False):
                # set definitions
                move = [[self.selectedPiece[0] - Ycheck, self.selectedPiece[1] - Xcheck]]

                # check if in range of board
                if (self.selectedPiece[0] - Ycheck) < 0 or (self.selectedPiece[0] - Ycheck) > 7 or (self.selectedPiece[1] - Xcheck) < 0 or (self.selectedPiece[1] - Xcheck) > 7:
                    spaceChecking = True
                else:
                    spaceChecking = self.board[self.selectedPiece[0] - Ycheck][self.selectedPiece[1] - Xcheck]

                    # checking space is empty
                    if (spaceChecking == False):
                        self.moves += move
                        Ycheck += addY
                        Xcheck += addX

                    else:  # hit a piece
                        # attack case
                        if ((str(spaceChecking)[0] != ("w" if self.white else "b"))):
                            self.moves += move
                        spaceChecking = True  # stop checking

        return self.moves