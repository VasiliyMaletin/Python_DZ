def check_win(size_board):
    winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in winning_combinations:
        if size_board[i[0]] == size_board[i[1]] == size_board[i[2]]:
            return size_board[i[0]]
    return False