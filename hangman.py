import random

someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut
watermelon cherry papaya berry peach lychee muskmelon kiwi blueberry raspberry blackberry
pear plum guava pomegranate dragonfruit avocado melon fig date grapefruit tangerine
carrot potato tomato onion garlic ginger spinach cabbage broccoli cauliflower cucumber
pumpkin radish beetroot peas corn mushroom lettuce celery
elephant tiger lion monkey giraffe zebra kangaroo panda rabbit dolphin whale shark
penguin crocodile turtle leopard cheetah wolf fox deer horse
computer keyboard monitor laptop printer scanner software hardware python java javascript
programming algorithm database network internet school college teacher student classroom
library notebook pencil football cricket tennis basketball volleyball swimming badminton hockey'''

someWords = someWords.split(' ')
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: The word is known to you.')

    for i in word:
        print('_', end=' ')
    print()

    letterGuessed = ''
    chances = len(word) + 2
    flag = False
    hangman = [
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
]

wrongGuesses = 0
chances = len(hangman) - 1
    
try:
        while chances > 0 and not flag:
            print()
            guess = input('Enter a letter to guess: ').lower()

            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) != 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            letterGuessed += guess

            if guess in word:
                print("Good guess!")
            else:
                print("Wrong guess!")
                chances -= 1
                wrongGuesses += 1
                print(hangman[wrongGuesses])
                print(f"You have {chances} chances left.")
                

            # Show current progress
            display = ''
            flag = True  # Assume player guessed all correctly
            for char in word:
                if char in letterGuessed:
                    display += char + ' '
                else:
                    display += '_ '
                    flag = False  # Found a letter not guessed yet

            print("Word so far:", display.strip())

        if flag:
            print("\nCongratulations! You guessed the word:", word)
        else:
            print("\n💀 You lost! The word was:", word)

except KeyboardInterrupt:
        print('\n\nBye! Try again.')
        exit()
