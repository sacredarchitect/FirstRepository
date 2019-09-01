# Problem Set 2
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    '''
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    '''
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    '''
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def unique_letters(secret_word):
    '''
    input: string
    output: list of unique letters in input
    '''
    secret = []
    for i in range(len(secret_word)):
        if secret_word[i] not in secret:
            secret.append(secret_word[i])
    return secret

def check_game_won(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    '''
    correct_letters = []
    secret = unique_letters(secret_word) #Only consider unique letters in secret_word
    
    for i in range(len(letters_guessed)):
        if letters_guessed[i] in secret:
            correct_letters.append(letters_guessed[i])
      
    secret.sort()
    correct_letters.sort()
    #Compare correct letters to secret word to see if done
    if secret == correct_letters:
        return True
    else:
        return False

def get_word_progress(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and underscores (_) that represents
      which letters in secret_word have not been guessed so far
    '''
    secret = list(secret_word)
    current = []
    
    for i in range(len(secret)):
        if secret[i] in letters_guessed:
            current.append(secret[i])
        else:
            current.append('_')
            
    strCurrent = ' '.join(current)
    return strCurrent

def get_remaining_possible_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which 
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    '''
    remaining = list(string.ascii_lowercase)
    
    for i in range(len(letters_guessed)):
        if letters_guessed[i] in remaining:
            remaining.remove(letters_guessed[i])
            
    strRemaining = ''.join(remaining)
    return strRemaining

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessesLeft = 10
    letters_guessed = []
    #Introduce the game
    print('Welcome to Hangman! \nI am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
   
    while check_game_won(secret_word, letters_guessed) == False and guessesLeft != 0:
        print(get_word_progress(secret_word, letters_guessed))
        print('You have ' + str(guessesLeft) + ' guesses left. \nAvailable letters: ' + get_remaining_possible_letters(letters_guessed))
        
        #Control user input
        while True:
            guess = input("Guess a letter:")
            guess = guess.lower()
            if guess in list(string.ascii_lowercase) and guess not in letters_guessed:
                break
            elif guess in letters_guessed:
                print("Only enter a letter you haven't already guessed.")
            else:
                print("Only enter a letter!")
        
        letters_guessed.append(guess)
        if guess in list(secret_word):
            print("Correct!")
        else:
            print("Sorry, not correct! Try again!")
            guessesLeft -= 1
    
    score = 3*guessesLeft + 2*(len(secret_word) + len(unique_letters(secret_word)))
    
    if guessesLeft == 0:
        print("Oh, no! You didn't guess the right number. \nThe word was " + str(secret_word) + "!")
    else:
        print("Thank you for playing! You had " + str(guessesLeft) + " guesses left! \nYour score is " + str(score) + ".")
           
#hangman(choose_word(wordlist))

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

# -----------------------------------

def hint_revealer(secret_word, remaining_letters):
    '''
    secret_word = string word from which a letter is revealed at random
    remaining_letters = string from get_remaining_possible_letters()
    output: a correct letter for the hangman game
    '''
    secret = list(secret_word)
    remaining = list(remaining_letters)
    choose_from = []
    
    for i in range(len(secret)):
        if secret[i] in remaining:
            choose_from.append(secret[i])
            
    strChooseFrom = ''.join(choose_from) #Available letters for a hint
    chosen = random.randint(0, len(strChooseFrom)-1)
    hint_letter = strChooseFrom[chosen] 
       
    return hint_letter

def hangman_with_help(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make sure that
      the user puts in a letter.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, you should reveal to the user one of the 
      letters missing from the word at the cost of 2 guesses. If the user does 
      not have 2 guesses remaining, print a warning message. Otherwise, add 
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessesLeft = 10
    letters_guessed = []
    uniqueSecret = len(unique_letters(secret_word))
    hintsUsed = 0
    
    #Limit number of hints available
    if uniqueSecret > 3:
        numHints = uniqueSecret - 1
        if numHints > 5:
            numHints = 5
    else:
        numHints = 1 
    
    #Introduce the game
    print("Welcome to Hangman! \nI am thinking of a word that is " + str(len(secret_word)) + " letters long. Enter '*' for a hint. They cost two guesses though! \nYou have " + str(numHints) + " hint(s) left.")
   
    while check_game_won(secret_word, letters_guessed) == False and guessesLeft != 0:
        print(get_word_progress(secret_word, letters_guessed))
        print('You have ' + str(guessesLeft) + ' guesses left. \nAvailable letters: ' + get_remaining_possible_letters(letters_guessed))
        
        #Control user input
        while True:
            guess = input("Guess a letter:")
            guess = guess.lower()
            if guess in list(string.ascii_lowercase) and guess not in letters_guessed:
                break
            elif guess == '*': #Control hints
                hint = hint_revealer(secret_word, get_remaining_possible_letters(letters_guessed)) 
                guess = hint
                
                if guessesLeft <= 2: 
                    print("You don't have enough guesses left to use a hint!")
                else:
                     numHints -= 1
                     hintsUsed += 1
                     guessesLeft -= 2
                     break
            elif guess in letters_guessed:
                print("Only enter a letter you haven't already guessed.")
            else:
                print("Only enter a letter!")
        
        letters_guessed.append(guess)
        if guess in list(secret_word):
            print("Correct!")
        else:
            print("Sorry, not correct! Try again!")
            guessesLeft -= 1
    
    score = 3*guessesLeft + 2*(len(secret_word) + len(unique_letters(secret_word))) - 4*hintsUsed
    
    if guessesLeft == 0:
        print("Oh, no! You didn't guess the right number. \nThe word was " + str(secret_word) + "!")
    else:
        print("Thank you for playing! You had " + str(guessesLeft) + " guesses left! \nYour score is " + str(score) + ".")

#hangman_with_help(choose_word(wordlist))
# When you've completed your hangman_with_help function, comment the two similar
# lines below that were used to run the hangman function, and then uncomment
# those two lines and run this file to test!

# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # To test part 2, uncomment the following two lines.

#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############

    # To test part 3, comment out the above lines and
    # uncomment the following two lines.

#    secret_word = choose_word(wordlist)
#    hangman_with_help(secret_word)

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass
