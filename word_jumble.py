#Word Jumble
#The computer picks a random word and then 'jumbles' it
#The player has to guess the original word

import random

# choose a sequence of words to choose from
WORDS = ('python','jumble','easy','difficult','answer','xylophone')

# pick one word randomly from the sequence
word = random.choice(WORDS)


# create a variable to use later
correct = word
# create an jumbled version of the word
jumble = ''

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# Start the game
print('The jumble is ', jumble)

# getting the player's guess
guess = input('\nYour guess:')

# Scores players who never utilised a hint
if guess in WORDS:
    print('You scored 100% without any hint')

while guess != correct and guess !='':
    print('Sorry that is not it')
    ask = input('Do you want to see the hint for this word? Answer Y or N')
    if ask == 'Y':
        print('The available options are pyth..,eas..,diff...,ans... and xylo...')
        guess = input('Your guess now: ')
        # Score player who used hint
        if guess in WORDS:
            print('You scored nothing because you used hint')

    elif ask == 'N':
        guess = input('\nYour guess: ')
        if guess in WORDS:
            print('You scored 100% without any hint')



    else:
        print('Either type in Y or N')


