# beangame

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 20:53:27 2021

@author: manor
"""

# Two players who alternately take 1,2, or 3 beans from the pile of beans. Whichever of the 2 players who takes the last bean loses.

# General Idea:

# Prompt the number of beans to start (how many beans are in the pile at the start)
# Players take turns removing beans from pile.
# write function for player1 and a fucntion for player2.
# Each of the player functions will have a parameter showing the number of beans currently in the pile. 

# Each player function will return the number of beans removed.

# You can make the player1 function as simple as you would like. For example, always remove one bean.

# The player2 function should be smarter than player1. 
You could randomly choose a number of beans (from 1 to 3 beans) to remove, or your function could even be smarter than this.

# The main program will prompt for the initial number of beans. 
It will call the player1 and player2 functions, printing the current state of the game at each step. For example:
Player1: 13 beans remaining. Player takes 2 beans. 11 beans left.
Player2: 11 beans remaining. Player takes 3 beans. 8 beans left.

# At the end of the game (when there are no beans left), the main program will print the winning player.
