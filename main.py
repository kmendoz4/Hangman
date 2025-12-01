# Hangman in python

import random # random module

words = ("apple", "orange", "banana", "coconut", "pineapple") #random set of words

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

#dictionary is working

def display_man(wrong_guesses): #display man function
    
    print("--------")
    for line in hangman_art[wrong_guesses]: #for each line in hangman_art dictionary at key wrong_guesses
        print(line) #print each line of hangman_art

    print("--------")

def display_hint(hint): #going to be a list  of letters and underscores
    
    print(" ".join(hint)) #string has built in join method -- the hint will be joined by a space and underscores

def display_answer(answer): #display answer whether lose or win game
    
    print(" ".join(answer))

def main(): #to run the game
    
    answer = random.choice(words) #randomly choose word 
    
    hint = ["_"] * len(answer) #print the hint -- multiply the underscore by length of answer
    #hint is a list of underscores

    wrong_guesses = 0 #0 wrong guesses to start the game

    guessed_letters = set() #set of guessed letters

    is_running = True #Boolean variable - while game is running is_running = True


    while is_running: #while loop - while game is running
        display_man(wrong_guesses) #call function display_man and pass wrong_guesses
        display_hint(hint) #call function display_hint and pass hint -- list of letters and underscores
        guess = input("Guess a letter: ").lower() #input guess from user -- .lower() to make letter lowercase

        #input validation

        if guess in answer: #if guess is in answer -- in is a membership operator
            for i in range(len(answer)): #for i in range of length of answer
                if answer[i] == guess: #if we guess a correct letter 
                    hint[i] = guess #show the letter in the hint
    

if __name__ == "__main__":
    main() #call main function to run the game