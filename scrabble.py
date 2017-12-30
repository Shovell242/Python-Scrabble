import random, re
from operator import itemgetter

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwyxz'

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORD_LIST_FNAME = 'words.txt'

WORDS_INV_TOTAL = 9

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
    hand = []

    vowelTotal = WORDS_INV_TOTAL // 3
    for i in range(vowelTotal):
        hand.append(VOWELS[random.randrange(0, len(VOWELS))])
    for i in range(vowelTotal, WORDS_INV_TOTAL):
        hand.append(CONSONANTS[random.randrange(0, len(CONSONANTS))])
    random.shuffle(hand)    
    return hand

def validateUserGuess(hand, guess):
    '''
    Input: current hand of characters user is choosing from to create words
    as well as the actual word guess of the user
    Returns: True or False if the user has used only valid characters in their guess
    '''
    handCopy = hand.copy()
    for char in guess:
        if char in hand:
            handCopy.remove(char)
        else:
            return False
    return True

def mutateHand(hand, guess):
    for char in guess:
        hand.remove(char)

def validateWordExists(guess):
    '''
    Input: takes the users guess after validation of characaters
    and see if it matches any words within the our loaded words.txt
    Return: True or False if the word....is in fact a word
    '''
    return guess.upper() in loadWords()

def scoreUserGuess(guess):
    '''
    Input: string of the guess
    Returns: using the SCRABBLE_LETTER_VALUES constant, this will sum up
    the users guess with associated point total and add a bonus of 50 if 
    the WORDS_INV_TOTAL is used
    '''
    scoreTotal = 0
    for char in guess:
        scoreTotal += SCRABBLE_LETTER_VALUES[char]
    if len(guess) == WORDS_INV_TOTAL:
        scoreTotal = (scoreTotal * len(guess)) + 50
    else:
        scoreTotal *= len(guess)
    return scoreTotal

def userMenu():
    '''
    prints options for users between guesses during the game
    Returns: a character of user choice
    '''
    viableAnswers = ['n', 'r', 'e']
    while True:
        ans = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if ans in viableAnswers:
            break
        else:
            print('Sorry, that is not a viable answer. Please choose again')
    return ans

def gameInput():
    '''
    Input: the user will enter his word guesses here or a '.' to indicate 
    they are done guessing
    Returns: the user word guess or '.' to end guessing
    '''
    ans = input('Enter word, or a "." to indicate that you are finished: ')
    return ans

def getUsername():
    usrName = input('Please enter your initials!: ')
    return usrName

def outputScore(name, score):
    file = open('leaderboard.txt', 'a')
    file.write(name + ': ' + str(score) + '\n')
    file.close()

def formatLeaderboard():
    games = []
    file = open('leaderboard.txt', 'r')
    for line in file:
        initRegex = re.compile(r'.+:')
        init = initRegex.search(line)
        scoreRegex = re.compile(r'\d+')
        score = scoreRegex.search(line)
        games.append([init.group(), int(score.group())])  
    gamesSort = sorted(games, key = itemgetter(1), reverse = True)
    return gamesSort

def printLeaderboard():
    print('---LEADERBOARD---')
    arr = formatLeaderboard()
    for i in range(6):
        try:
            print(arr[i][0], arr[i][1])
        except:
            print(' ')

def game(prevHand = False):
    printLeaderboard()
    if prevHand:
        hand = prevHand
    else:
        hand = dealHand()
    score = 0
    name = getUsername()
    while True:
        print('Current Hand:', ' '.join(hand))
        guess = gameInput()
        if guess == '.':
            break
        if not validateWordExists(guess) or not validateUserGuess(hand, guess): 
            print('Invalid word, please try again.')
        else:
            mutateHand(hand, guess)
            points = scoreUserGuess(guess)
            print(guess, 'has earned', str(points), 'points!')
            score += points
    print('Total score:', score, 'points')
    outputScore(name, score)

game()

        

































