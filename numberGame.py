print'\tWellcome to Guess The Number Game'
print 'What is your name?'
yourName = input()
print 'Can you guess the right number between 1 and 100?'

import random
number = random.randint(1,100)
yourGuess = input('Go ahead and guess:')
yourGuess = int(yourGuess) # check if answer is an interger
numberOfTries = 1

while yourGuess != number:
    if yourGuess > number:
        print 'Think of a lower number'
    else:
        print 'Think of a higher number'

    yourGuess = input('Take another guess:')
    yourGuess = int(yourGuess)
    numberOfTries += 1
    if numberOfTries == 10:
        print 'Oh gosh you are not good at guessing at all, try playing something else!'
        break
    if yourGuess == number:
        print 'Awesome you guessed the right number!!!'

raw_input("\n\nPress the enter key to exit.")