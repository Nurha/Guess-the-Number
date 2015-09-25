print'Wellcome to Guess The Number game'
print 'What is your name?'
yourName = input()
print 'Can you guess the right number between 1 and 100?'

import random
number = random.randint(1,100)
yourGuess = input()
yourGuess = int(yourGuess) # check if answer is an interger