import glossary as g
import functions as f
import random
import sys

print('Tic-Tac-Toe Game')
print('Instruction:\nrows: top, mid, low\ncolumns: L, M, R\nWrite "top-l" to move top left field')
PLAYER_MOVES = []
COMPUTER_MOVES = []
COMPUTER_SEARCH_FOR_FIELDS = 0
COUNT_WIN_FIELDS_P = 0
COUNT_WIN_FIELDS_C = 0
PLAYER_SCORE = 0
COMPUTER_SCORE = 0
DRAWS = 0
PLAY_AGAIN = 'N'
END_GAME = False
last_turn = 'player'

while True:
    print(f.printBoard(g.TicTacDictionary))

    #make move section---------------
    if END_GAME is False:
        #player move
        while last_turn == 'player':
            playerTurn = input('Turn for X, Move on which space: ')
            try:
                if g.TicTacDictionary[playerTurn.upper()] != ' ':
                    print('Field is taken')
                    print(f.printBoard(g.TicTacDictionary))
                    continue
                else:
                    g.TicTacDictionary[playerTurn.upper()] = 'X'
                    last_turn = 'computer'
            except KeyError:
                print(f"Invalid field name, write again")
                continue

        #computer move
        while last_turn == 'computer':
            computerTurn = g.MappingTicTacDictionary[str(random.randint(1,9))]

            #BREAK WHEN COMPUTER CANT FIND empty field
            if COMPUTER_SEARCH_FOR_FIELDS == 100:
                break

            if g.TicTacDictionary[computerTurn] == 'X' or g.TicTacDictionary[computerTurn] == 'O':
                COMPUTER_SEARCH_FOR_FIELDS += 1
                continue
            else:

                g.TicTacDictionary[computerTurn] = 'O'
                last_turn = 'player'

    # follow player/computer moves seciton --------------------
    for key, value in g.TicTacDictionary.items():
        if value == 'X':
            if key not in PLAYER_MOVES:
                PLAYER_MOVES.append(key)
        elif value == 'O':
            if key not in COMPUTER_MOVES:
                COMPUTER_MOVES.append(key)

    # check for win end game combination or draw section ---------------------
    if len(PLAYER_MOVES) >= 3:
        for combinations in g.WinCombinations:

            COUNT_WIN_FIELDS_P = 0
            COUNT_WIN_FIELDS_C = 0
            for combination in combinations:
                if combination in PLAYER_MOVES:
                    COUNT_WIN_FIELDS_P += 1
                    if COUNT_WIN_FIELDS_P == 3:
                        print('!!! Player win game !!!')
                        PLAYER_SCORE += 1
                        END_GAME = True
                elif (combination in COMPUTER_MOVES) and END_GAME is False:
                    COUNT_WIN_FIELDS_C += 1
                    if COUNT_WIN_FIELDS_C == 3:
                        print('!!! Computer win game !!!')
                        COMPUTER_SCORE += 1
                        END_GAME = True

    if END_GAME is False:
        if ' ' not in g.TicTacDictionary.values():
            print('Draw')
            DRAWS += 1
            END_GAME = True


    #play again after win section -------------
    if END_GAME is True:
        print(f.printBoard(g.TicTacDictionary))
        print(f'Score:\nPlayer: {PLAYER_SCORE}\nComputer: {COMPUTER_SCORE}\nDraws: {DRAWS}')
        while END_GAME is True:
            PLAY_AGAIN = input('Do you wanna play again? Y/N: ').upper()
            if PLAY_AGAIN == 'Y':
                g.TicTacDictionary = f.clearboard(g.TicTacDictionary)
                PLAYER_MOVES.clear()
                COMPUTER_MOVES.clear()
                END_GAME = False
                continue
            elif PLAY_AGAIN == 'N':
                print('Thank you for game')
                sys.exit()
            else:
                print("Write Y or N as an ansewer")
                continue


