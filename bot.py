from board import Board

class Bot:

    def __init__(self, board, botColor = "b"):
        self.board = board
        self.botColor = botColor

    def findMove(self):
        board = Board(self.board)
        board.printBoard()
        # print(board.selectPiece("bn1").moves())
        allMoves = board.getAllMoves(self.botColor)
        # print(allMoves)
        #
        # for i in allMoves:
        #
        #     # print(allMoves[i])
        #     # boardClass = Board(board)
        #     # # boardClass.printBoard()
        #     # test = boardClass.selectPiece("wn2").moves()
        #
        #     print(test)



    # def testMove(self, board):




        # board.selectPiece("wp5").move(5, 5)
        # board.printBoard()
