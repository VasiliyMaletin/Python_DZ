size_board = list(range(1, 10))

def board_creation(size_board):
    print("╔═══╦═══╦═══╗")
    count = 3
    for i in range(3):
        print(f"║ {size_board[0 + i * 3]} ║ {size_board[1 + i * 3]} ║\
 {size_board[2 + i * 3]} ║")
        if count > 1:
            print("╠═══╬═══╬═══╣")
        count -= 1
        if count < 1:
            print("╚═══╩═══╩═══╝")