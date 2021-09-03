# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 10:23:37 2021

@author: manor
"""

#bean game
import random

def player1(beans_int):
    if (beans_int - 1) % 4 == 0:
        return 1
    else:
        return (beans_int -1) % 4
    
def player2(beans_int):
    beans_remove = random.randint(1,3)
    if beans_int == 1:
        return 1
    elif beans_int == 2:
        return 1
    elif beans_int == 3:
        return 2
    else: 
        return beans_remove
    
beans_str = input("Enter number of beans for the game: ")
beans_int = int(beans_str)

game_over = False

while not game_over:
    beans_remove = player1(beans_int)
    print("strarting beans", beans_int, "beans removed by player1", beans_remove, "beans remaining", beans_int- beans_remove )
    beans_int = beans_int - beans_remove
    if beans_int == 0:
        print("player 2 is the winner")
        game_over = True
    
    else:
        beans_remove = player2(beans_int)
        print("strarting beans", beans_int, "beans removed by player2", beans_remove, "beans remaining", beans_int - beans_remove )
        beans_int = beans_int - beans_remove
        if beans_int == 0:
            print("player 1 is the winner")
            game_over = True