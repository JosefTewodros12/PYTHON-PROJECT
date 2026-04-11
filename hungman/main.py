import random
from hangman_art import logo, stages
from hangman_words import word_list

# word_list = ['ardvark', 'baboon', 'camel']
display = []

chosen_word = random.choice(word_list)
print(logo)
for i in chosen_word:
    display += "_"

end_of_game = False

life = 6

while not end_of_game:
    print(f"{'  '.join(display)}")
    guess = input("Guess a letter? ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess in chosen_word:
        print(f"You already guess {guess}")
    elif guess not in chosen_word:
        life -= 1
        if (life == 0):
            end_of_game = True
            print(
                f"You guessed {guess}, that's not in the word. You lose a life.")
    print(stages[life])
    if "_" not in display:
        print("You win")
        end_of_game = True
