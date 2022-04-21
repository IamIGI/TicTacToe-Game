def printBoard(board):

    """
    board(dictionary)
    """

    print(f"{board['TOP-L']} | {board['TOP-M']} | {board['TOP-R']}")
    print('--+---+--')
    print(f"{board['MID-L']} | {board['MID-M']} | {board['MID-R']}")
    print('--+---+--')
    print(f"{board['LOW-L']} | {board['LOW-M']} | {board['LOW-R']}")


def clearboard(board):
    board = board.fromkeys(board, ' ')
    return board