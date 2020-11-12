from board import Board

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board()
    board.printBoard()
    # board.selectPiece("wp5").move(3, 4)
    board.selectPiece("wp7").moves()
    # board.printBoard()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
