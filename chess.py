'''
Chess figure Horse move check
Not long time ago Vasya started programming and diceded to make his own program for playing chess.
But, he has a problem with detecting the right move of the Horse, which user does.
If user inputs value "C7-D5", then program must detect the right move, if input is "E2-E4", then move is not correct.
Also there must be check if input is correct, for examle if input is "D9-N5", then program must show that this input is mistaken.
Help him make this check!

Совсем недавно Вася занялся программированием и решил реализовать собственную программу для игры в шахматы.
Но у него возникла проблема определения правильности хода конем, который делает пользователь.
Т.е. если пользователь вводит значение «C7-D5», то программа должна определить это как правильный ход,
если же введено «E2-E4», то ход неверный.
Так же нужно проверить корректность записи ввода: если например, введено «D9-N5»,
то программа должна определить данную запись как ошибочную. Помогите ему осуществить эту проверку!
'''

alphabet = "ABCDEFGH"
num = "12345678"

def input_check(move):
    if len(move) == 5:
        if (move[0] in alphabet and
            move[1] in num and
            move[2] == "-" and
            move[3] in alphabet and
            move[4] in num):
            return True
        else:
            return False
    else:
        return False

def move_check(move):
    start_move = [alphabet.index(move[0]) + 1, int(move[1])]
    end_move = [alphabet.index(move[3]) + 1, int(move[4])]
    if (abs(start_move[0]-end_move[0]) == 2 and
        abs(start_move[1]-end_move[1]) == 1):
        return True
    elif (
        abs(start_move[0]-end_move[0]) == 1 and
        abs(start_move[1]-end_move[1]) == 2):
        return True



while True:
    move = input("Походите конем(Например C7-D5): ")
    if move == "exit":
        break
    if input_check(move):
        if move_check(move):
            print("Верный ход!")
        else:
            print("Сударь, печален сий факт конем хождения!")
            continue
