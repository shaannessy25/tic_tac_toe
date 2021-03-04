"""This file creates a tic tac toe game that is playable on the terminal"""

import random

BOARD_SPACE = 10

def draw_board(board):
    """This method prints out the board"""
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def input_player_letter():
    """This method will assign letter to a player and returns players name and item"""
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    """This function randomly chooses who makes the first"""
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def play_again():
    """This function determines if palyer wants to play again"""

    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def make_move(board, letter, move):
    """Places the letter in correct spot"""
    board[move] = letter


def is_winner(bo, le):
    """This function determines who is the winner"""

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            # across the middle
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            # down the right side
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def get_board_copy(board):
    """This function returns a deplicate board list"""

    dupeBoard = []
    for i in range(0, len(board)):  # TODO: Clean this mess!
        dupeBoard.append(board[i])

    return dupeBoard


def is_space_free(board, move):
    """This function determines if the space is available"""
    return board[move] == ' '


def get_player_move(board):
    """This function gets the player moves"""

    player_move = ' '
    while player_move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(player_move)):
        print('What is your next move? (1-9)')
        player_move = input()
    return int(player_move)


def choose_random_move_from_list(board, movesList):
    """This function returns a valid move from the passed list onto the"""
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possible_moves = []
    for i in movesList:
        if is_space_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) is not 0:
        return random.choice(possible_moves)
    return None



def get_computer_move(board, computer_letter):
    """This function determines and returns the players move"""
    # Given a board and the computer's letter, determine where to move and return that move.
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'


    for i in range(1, BOARD_SPACE):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, BOARD_SPACE):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def is_board_full(board):
    """This function returns true if every space has been taken"""
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, BOARD_SPACE):
        if is_space_free(board, i):
            return False
    return True



def run_game():
    """This function will run the tic tac toe game"""

    print('Welcome to Tic Tac Toe!')
    #Resets the board
    while True:
        the_board = [' '] * BOARD_SPACE
        player_letter, computer_letter = input_player_letter()
        turn = who_goes_first()
        print('The ' + turn + ' will go first.')

        while True:
                if turn == 'player':
                    # Player’s turn.
                    draw_board(the_board)
                    move = get_player_move(the_board)
                    make_move(the_board, player_letter, move)

                    if is_winner(the_board, player_letter):
                        draw_board(the_board)
                        print('Hooray! You have won the game!')
                        break

                    if is_board_full(the_board):
                        draw_board(the_board)
                        print('The game is a tie!')
                        break
                    turn = 'computer'

                else:
                    # Computer’s turn.
                    move = get_computer_move(the_board, computer_letter)
                    make_move(the_board, computer_letter, move)

                    if is_winner(the_board, computer_letter):
                        draw_board(the_board)
                        print('The computer has beaten you! You lose.')
                        break
                    if is_board_full(the_board):
                        draw_board(the_board)
                        print('The game is a tie!')
                        break
                    turn = 'player'

        if not play_again():
            break

run_game()












