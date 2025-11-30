# Hangman in python

import random # random module

words = ("apple", "orange", "banana", "coconut", "pineapple")

#dictionary of key:() --> ASCII art 
hangman_art = {0: ("   ",
                   "   ",
                   "   "), 
               1: (" o ",
                   "   ",
                   "   "), 
               2: (" o ",
                   " | ",
                   "   "), 
               3: (" o ",
                   "/| ",
                   "   "), 
               4: ( " o ",
                   "/|\\", #backslash means escape string so you need double backslash to print one
                   "   "), 
               5: ( " o ",
                   "/|\\",
                   "/  "), 
               6: ( " o ",
                   "/|\\",
                   "/ \\")} #after 6 incorrect guesses - lose game