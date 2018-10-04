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
while guess != correct and guess !='':
    print('Sorry that is not it')
    guess = input('Your guess: ')

# Congratulating the player
if guess == correct:
    print('That is it. You guessed it right')

print('Thanks for playing')