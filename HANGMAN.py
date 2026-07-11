import random

# Hangman stages
stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
game_over = False
guessed_letters = []

print(f"DEBUG: The word is {chosen_word}") # Remove in final version
print("_" * word_length)

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'.")
        continue
    
    guessed_letters.append(guess)

    # Build the display string
    display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    
    print(display)

    # Check if guess is wrong
    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in the word.")
        print(stages[lives])
        if lives == 0:
            game_over = True
            print("You Lose!")
    else:
        # Check if user has won
        if "_" not in display:
            game_over = True
            print("You Win!")