import random
import game_resources
from game_resources import hangman_pics


def play_hangman():
    clue = random.choice(list(game_resources.categories))
    word = random.choice(game_resources.categories[clue]).lower()
    fill_in = []
    good_letters = set()
    for char in word:
        if char == '_':
            fill_in.append(' ')
        elif char.isalpha() is True:
            fill_in.append('_')
            good_letters.add(char)
        else:
            fill_in.append(char)
    strikes = 0
    used_letters = set()
    while strikes < len(hangman_pics)-1 and good_letters:
        print(hangman_pics[strikes])
        for char in fill_in:
            print(char, end=' ')
        print()
        while True:
            print()
            print(f"Clue: {clue}")
            letter = input("Guess a letter: ").lower()
            if letter.isalpha() is False or len(letter) > 1:
                print('Sorry, that was not a valid letter, try again!')
            elif letter not in used_letters:
                break
            else:
                print("You've already guessed this letter, try again!")
        used_letters.add(letter)
        if letter in good_letters:
            good_letters.remove(letter)
            print(f"Good guess, {letter} is correct!")
            for idx in range(len(word)):
                if letter == word[idx]:
                    fill_in[idx] = letter
        else:
            print(f"Sorry, your guess, {letter}, is incorrect.")
            if strikes == len(hangman_pics) -2:
                print(hangman_pics[-1])
            strikes += 1
    print()
    if strikes == len(hangman_pics)-1:
        return f"You Lost: The answer is {word}. \nBetter luck next time!"
    elif not good_letters:
        for char in fill_in:
            print(char, end=' ')
        print()
        return f"You won: You correctly guessed {word}." 


print(play_hangman())