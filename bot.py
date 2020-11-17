from board import Board
from piece import Piece
import copy
import sys

iMaxStackSize = 50000
sys.setrecursionlimit(iMaxStackSize)

class Bot:

    def __init__(self, board, color="b", whiteScore=0, blackScore=0, level=0, movesList = [], botColor = "b", ):
        self.board = board[:]
        self.setBoard = board[:]

        self.color = color
        self.botColor = botColor


        # score tracker
        self.whiteScore = whiteScore
        self.blackScore = blackScore
        self.level = level

        self.movesList=[]

    # the weighted bias for each piece
    def attackWeight(self, moveSpace):
        piece = moveSpace[1]
        if (piece == "k"): # attack king
            return 99999
        if (piece == "q"): # attack queen
            return 15
        if (piece == "b"): # attack bishop
            return 10
        if (piece == "n"):  # attack knight
            return 7
        if (piece == "r"):  # attack rook
            return 5
        if (piece == "p"):  # attack pawn
            return 2

        return 0

    def findMove(self):

        board = copy.deepcopy(self.board)  # store current board

        # create new board instance
        # boardClass = Board(setBoard)
        # boardClass.printBoard()

        # get all moves for board for color
        x = 0
        y = 0
        movesPerPiece = []
        weightList = [0]

        # search over all board
        for i in board:
            for j in i:

                piece = board[x][y]

                # check side case
                if str(piece)[0] == self.color:

                    # set selectedPiece
                    selectedPiece = [x, y]

                    # get all the moves
                    pieceClass = Piece(board, selectedPiece)
                    moves = pieceClass.getMoves()

                    # print list
                    movesPerPiece += [[str(board[x][y]), moves]]

                    # print("-------------" + piece + "-------------")

                    # boardClass.setSelectedPiece(selectedPiece)

                    # print(boardClass.selectedPiece)

                    # create boards for each move
                    for move in moves:
                        # print("-------------" + str(move) + "-------------")
                    #
                        # boardClass.setBoard(board) # start with current bord
                        # boardClass.move(move[0], move[1]) # make move


                        # the move space
                        moveSpace = board[move[0]][move[1]]

                        whiteScore = 0
                        blackScore = 0
                        # weight score

                        weightScore = 0
                        if moveSpace != False:
                            weightScore = self.attackWeight(moveSpace)

                            whiteScore = (weightScore if self.color == "w" else 0) + self.whiteScore
                            blackScore = (0 if self.color == "w" else weightScore) + self.blackScore

                        # make the move
                        board[move[0]][move[1]] = str(piece)
                        board[x][y] = False # clear the old space

                        # if  >= the max level depth go one leve deeper
                        if self.level < 2:

                            # go one leve deeper with recursion
                            newBot = Bot(
                                board,
                                ("b" if self.color == "w" else "w"), # color
                                whiteScore, # whiteScore
                                blackScore, # blackScore
                                self.level + 1, # level
                                []
                            )
                            scoreTest = newBot.findMove()
                            weightScore = [scoreTest[0] + whiteScore, scoreTest[1] + blackScore]
                            weightList.append(weightScore)
                            # print(weightList)


                        if self.level == 0:
                            print("-------------" + piece + ":"  + str(move) + "-------------")
                            print("Total attack Weight:")
                            print(str(whiteScore - blackScore) )
                            # print("blackScore: " + str(blackScore))

                        # if self.level == 1:
                        #     return weightScore

                        # print board
                        # for i in board:
                        #     print(i)

                        # reset board
                        board = copy.deepcopy(self.board)

                        # reset board
                        # board = ([:])
                        # self.board = self.setBoard

                        # board[move[0]][move[1]] = self.board[self.selectedPiece[0]][self.selectedPiece[1]]
                        # board[self.selectedPiece[0]][self.selectedPiece[1]] = False
                        # print(board)

                    #
                    #     boardClass.printBoard()

                # board = Board(setBoard)


                y += 1
            y = 0
            x += 1

        # if self.level != 0:
        largestLoss = 0
        keyForLargestLoss = 0
        for i in range(len(weightList)):

            loss = weightList[i][0] - weightList[i][1]

            if (loss > largestLoss):
                largestLoss = loss
                keyForLargestLoss = i


        return weightList[keyForLargestLoss]


        # self.selectedPiece = False

        # print (movesPerPiece)

        # return scoreList[0]

        # allMoves = board.getAllMoves(self.botColor)
        # # print(allMoves)
        #
        # # generate a bord with each move
        # for i in range(5):
        #     piece = allMoves[i][0]
        #     print(allMoves[i][1])
        #
        #     # test all moves for pice
        #     for j in range(allMoves[i][1]):
        #         print(allMoves[i])

        # print(board.selectPiece("bn1").moves())

        # print(allMoves[i])

        # for i in allMoves:
        #
        #     # boardClass = Board(board)
        #     # # boardClass.printBoard()
        #     # test = boardClass.selectPiece("wn2").moves()
        #
        #     print(test)


    #
    # def bfs(graph, initial):
    #
    #     visited = []
    #
    #     queue = [initial]
    #
    #     while queue:
    #
    #         node = queue.pop(0)
    #         if node not in visited:
    #
    #             visited.append(node)
    #             neighbours = graph[node]
    #
    #             for neighbour in neighbours:
    #                 queue.append(neighbour)
    #     return visited

    # print(bfs(graph, 'A'))

    # def testMove(self, board):




        # board.selectPiece("wp5").move(5, 5)
        # board.printBoard()
