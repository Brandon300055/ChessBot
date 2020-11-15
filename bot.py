from board import Board
from piece import Piece


class Bot:

    def __init__(self, board, botColor = "b", whiteScore=0, blackScore=0, level=0):
        self.board = board[:]
        self.setBoard = board[:]

        self.botColor = botColor

        # score tracker
        self.whiteScore = whiteScore
        self.blackScore = blackScore
        self.level = level

    def findMove(self):

        # max level depth
        if self.level == 4:
            return

        board = self.board[:]   # store current board

        # create new board instance
        # boardClass = Board(setBoard)
        # boardClass.printBoard()

        # get all moves for board for color
        x = 0
        y = 0
        movesPerPiece = []

        # search over all board
        for i in board:
            for j in i:

                piece = board[x][y]

                # check side case
                if str(piece)[0] == self.botColor:

                    # set selectedPiece
                    selectedPiece = [x, y]

                    # get all the moves
                    pieceClass = Piece(board, selectedPiece)
                    moves = pieceClass.getMoves()

                    # print list
                    movesPerPiece += [[str(board[x][y]), moves]]

                    print("-------------" + piece + "-------------")

                    # boardClass.setSelectedPiece(selectedPiece)

                    # print(boardClass.selectedPiece)

                    # create boards for each move
                    for move in moves:
                        print("-------------" + str(move) + "-------------")
                    #
                        # boardClass.setBoard(board) # start with current bord
                        # boardClass.move(move[0], move[1]) # make move


                        # the move space
                        moveSpace = board[move[0]][move[1]]

                        # weight score
                        if moveSpace != False:
                            pass

                        # make the move
                        board[move[0]][move[1]] = str(piece)
                        board[x][y] = False # clear the old space

                        for i in self.setBoard:
                            print(i)


                        # reset board
                        board = self.setBoard[:]
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
        # self.selectedPiece = False

        print (movesPerPiece)





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
