from board import *

def player_turn(player_symbol):
    valid = False
    while not valid:
        cell_number = input(f"Выберите куда ставим {player_symbol}?\n")
        try:
            cell_number = int(cell_number)
        except:
            print ("Нужно вводить число!")
            continue
        if cell_number > 0 and cell_number < 10:
            if (str(size_board[cell_number - 1]) not in "XO"):
                size_board[cell_number - 1] = player_symbol
                valid = True 
            else:
                print ("Клетка уже занята!")
        else:
            print ("Нужно вводить число соответствующее выбранной\
 свободной клетке.")