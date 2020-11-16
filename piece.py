class Piece:
    board = []
    selectedPiece = []

    def __init__(self, board, selectedPiece, side = False):
        self.board = board
        self.selectedPiece = selectedPiece
        self.piece = self.board[selectedPiece[0]][selectedPiece[1]]
        self.white = (self.piece[0] == 'w')
        self.color = ("w" if self.white else "b")

    # def setSelectedPiece(self, selectedPiece):
    #
    #
    #     return self

    # returns all moves from selected piece is pawn
    def pawn(self):
        moves = []

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
            moves += [firstSpace]

            # case for second space move
            secondSpace = [self.selectedPiece[0] + (-2 if white else 2), self.selectedPiece[1]]
            secondPiece = self.board[secondSpace[0]][secondSpace[1]]
            if secondPiece == False and ((white and self.selectedPiece[0] == 6) or (white == False and self.selectedPiece[0] == 1)):
                moves += [secondSpace]

        # # case for second space move by checking if selectedPiece is on starting line and
        # if blocked == False and ((white and self.selectedPiece[0] == 6) or (white == False and self.selectedPiece[0] == 1)):
        #     # is not blocked and is on print first line
        #     moves += [[self.selectedPiece[0] + (-2 if white else 2), self.selectedPiece[1]]]

        # check left attach
        if self.selectedPiece[1] - 1 >= 0:
            leftAttactPiece = self.board[leftAttack[0]][leftAttack[1]]
            if (leftAttactPiece != False) and (str(leftAttactPiece)[0] != color):
                moves += [leftAttack]

        # check right attach
        if self.selectedPiece[1] + 1 <= 7:
            rightAttactPiece = self.board[rightAttack[0]][rightAttack[1]]
            if (rightAttactPiece != False) and (str(rightAttactPiece)[0] != color):
                moves += [rightAttack]

        return moves

    # returns all moves from selected piece is rook
    def rook(self):

        # return self.board[self.selectedPiece[0] - -3][self.selectedPiece[1] - -9]
        moves = []

        for i in range(4):
            Ycheck = [-1, 0, 0, 1][i]
            Xcheck = [0, -1, 1, 0][i]
            addY = [-1, 0, 0, 1][i]
            addX = [0, -1, 1, 0][i]
            if (self.selectedPiece[0] - Ycheck) <= 0 or (self.selectedPiece[0] - Ycheck) > 7 or (
                    self.selectedPiece[1] - Xcheck) <= 0 or (self.selectedPiece[1] - Xcheck) > 7:
                spaceChecking = True
            else:
                spaceChecking = self.board[self.selectedPiece[0] - Ycheck][self.selectedPiece[1] - Xcheck]

                while (spaceChecking == False):

                    # check if in range of board
                    if (self.selectedPiece[0] - Ycheck) < 0 or (self.selectedPiece[0] - Ycheck) > 7 or (
                            self.selectedPiece[1] - Xcheck) < 0 or (self.selectedPiece[1] - Xcheck) > 7:
                        spaceChecking = True
                    else:

                     # set definitions
                        move = [[self.selectedPiece[0] - Ycheck, self.selectedPiece[1] - Xcheck]]
                        spaceChecking = self.board[self.selectedPiece[0] - Ycheck][self.selectedPiece[1] - Xcheck]

                        # checking space is empty
                        if (spaceChecking == False):
                            moves += move
                            Ycheck += addY
                            Xcheck += addX

                        else:  # hit a piece
                            # attack case
                            if ((str(spaceChecking)[0] != ("w" if self.white else "b"))):
                                moves += move
                            spaceChecking = True  # stop checking

        return moves

    # returns all moves from selected piece is knight
    def knight(self):

        moves = []

        for i in range(8):
            firstVal = 2 if (i >= 4) else 1
            secondVal = 1 if (i >= 4) else 2
            firstSign = "-" if (i % 4) == 2 or (i % 4) == 3 else "+"
            secondSign = "+" if (i % 2) else "-"

            jump = [int(firstSign + str(firstVal)), int(secondSign + str(secondVal))]
            move = [self.selectedPiece[0] + jump[0], self.selectedPiece[1] + jump[1]]

            # check if move is on the board
            if(move[0] >= 0 ) and (move[1] >= 0 ) and (move[0] <= 7 ) and (move[1] <= 7 ):
                piece = self.board[move[0]][move[1]] # get the piece

                # check if move is in the rules of the game
                if (piece == False) or (str(piece)[0] == ("b" if self.white else "w") ):
                    moves += [move]

        return moves

    # returns all moves from selected piece is bishop
    def bishop(self):

        moves = []

        # check all 4 diagonal directions
        for i in range(4):
            sign1 = "-" if (i >= 2) else "+"
            sign2 = "-" if (i % 2) else "+"

            # jump1 = int(sign1 + str(1))
            # jump2 = int(sign2 + str(1))

            jump1 = 1
            jump2 = 1

            spaceChecking = False

            # print([jump1, jump2])

            while (spaceChecking == False):
                jump = ([int(sign1 + str(jump1)), int(sign2 + str(jump2))])
                move = [self.selectedPiece[0] + jump[0], self.selectedPiece[1] + jump[1]]

                # print([int(sign1 + str(jump1)), int(sign2 + str(jump2))])



                # check if move is on the board
                if(move[0] < 0 ) or (move[1] < 0 ) or (move[0] > 7 ) or (move[1] > 7 ):
                    spaceChecking = True
                else:
                    piece = self.board[move[0]][move[1]] # get the piece

                    # empty space case
                    if (piece == False):
                        moves += [move]

                    # attack case
                    if str(piece)[0] == ("b" if self.white else "w"):
                        moves += [move]
                        spaceChecking = True

                    # friendly case
                    if str(piece)[0] == ("w" if self.white else "b"):
                        spaceChecking = True

                    # increment jump
                    jump1 += 1
                    jump2 += 1

        return moves

    # returns all moves from selected piece is bishop
    def queen(self):
        return self.rook() + self.bishop()

    def king(self):
        return []

    # calls right method for piece
    def getMoves(self):
        if self.piece[1] == "p":
            return self.pawn()
        if self.piece[1] == "r":
            return self.rook()
        if self.piece[1] == "n":
            return self.knight()
        if self.piece[1] == "b":
            return self.bishop()
        if self.piece[1] == "q":
            return self.queen()
        if self.piece[1] == "k":
            return self.king()


    def getAllMoves(self):
        pass