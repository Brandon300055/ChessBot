from board import Board

# Press the green button in the gutter to run the script.
from bot import Bot

if __name__ == '__main__':

    board = [
        #  0    #  1   # 2    # 3    # 4   # 5    # 6    # 7
        ["br1", "bn1", "bb1", "bk", "bq", "bb2", "bn2", "br2"],  # 0
        ["bp0", "bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7"],  # 1
        ["wp2", False, False, False, False, False, False, False],  # 2
        [False, False, False, False, False, False, False, False],  # 3
        [False, False, False, False, False, False, False, False],  # 4
        [False, False, False, False, False, False, False, False],  # 5
        ["wp0", "wp1", False, "wp3", "wp4", "wp5", "wp6", "wp7"],  # 6
        ["wr1", "wn1", "wb1", "wk", "wq", "wb2", "wn2", "wr2"],  # 7
    ]

    # board = Board(board)

    # print(board.selectPiece("wp5").moves())
    # print( board.selectPiece("bp1").moves() )
    # board.printBoard()

    # board.selectPiece("wn2").moves()



    # print(board.getAllMoves("w"))

    # board.printBoard()

    bot = Bot(board, "b")
    bot.findMove()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
