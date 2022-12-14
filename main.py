from board import *
from player import player_turn
from win import check_win

def main(size_board):
    count = 0
    win = False
    while not win:
        board_creation(size_board)
        if count % 2 == 0:
            player_turn("X")
        else:
            player_turn("O")
        count += 1
        if count > 4:
            temp = check_win(size_board)
            if temp:
                print (temp, "Выиграл!")
                win = True
                break
        if count == 9:
            print ("Ничья!")
            break
    board_creation(size_board)
