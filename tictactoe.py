# -*- coding: utf-8 -*-
"""
Created on Mon May 22 17:57:52 2023

@author: Zedo "Zanj" Ragas
"""

nums = [' '] * 9

def board():
    print('+---+---+---+')
    print('|', nums[0], '|', nums[1], '|', nums[2], '|')
    print('+---+---+---+')
    print('|', nums[3], '|', nums[4], '|', nums[5], '|')
    print('+---+---+---+')
    print('|', nums[6], '|', nums[7], '|', nums[8], '|')
    print('+---+---+---+')


def win(player):

    if nums[0] == nums[1] == nums[2] == player:
        return True
    if nums[3] == nums[4] == nums[5] == player:
        return True
    if nums[6] == nums[7] == nums[8] == player:
        return True
    if nums[0] == nums[3] == nums[6] == player:
        return True
    if nums[1] == nums[4] == nums[7] == player:
        return True
    if nums[2] == nums[5] == nums[8] == player:
        return True
    if nums[0] == nums[4] == nums[8] == player or nums[2] == nums[4] == nums[6] == player:
        return True
    return False


def run_game():
    cplayer = 'X'
    game_over = False
    print("Tic Tac Toe!")
    while not game_over:
        board()
        pos = int(input("Player " + cplayer + "(1-9): ")) - 1
        if 0 <= pos <= 8 and nums[pos] == ' ':
            nums[pos] = cplayer
            if win(cplayer):
                board()
                print("Player", cplayer, "wins!")
                game_over = True
            elif ' ' not in nums:
                board()
                print("Draw!")
                game_over = True
            else:
                cplayer = 'O' if cplayer == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

run_game()