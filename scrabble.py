import random


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORD_LIST_FNAME = 'words.txt'

WORDS_INV_TOTAL = 7

def loadWords():
    '''
    Input: loads words from a file named in the constant 'WORD_LIST_FNAME'
    Returns: a list of all words within the file
    '''
    file = open(WORD_LIST_FNAME, 'r')
    text = file.read().splitlines()
    return text

def dealHand():
    '''
    Returns: a random set of lower case characters 
    based on the 'WORDS_INV_TOTAL' as quantity of random characters
    '''
    return random.sample(SCRABBLE_LETTER_VALUES.keys(), WORDS_INV_TOTAL)

def validateUserGuess(hand, guess):
    '''
    Input: current hand of characters user is choosing from to create words
    as well as the actual word guess of the user
    Returns: True or False if the user has used only valid characters in their guess
    '''
    handCopy = hand.copy()
    for char in guess:
        if char in handCopy:
            handCopy.remove(char)
        else:
            return False
    return True

def validateWordExists(guess):
    '''
    Input: takes the users guess after validation of characaters
    and see if it matches any words within the our loaded words.txt
    Return: True or False if the word....is in fact a word
    '''
    return guess.upper() in loadWords()



























