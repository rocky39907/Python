import random
import hangman_words
import hangman_arts

print(hangman_arts.logo)
# Randomly picked word by system
system_picked_word = random.choice(hangman_words.word_list)

system_picked_word_len = len(system_picked_word)

display = list(system_picked_word)


for pos in range(system_picked_word_len):
    if pos != 0 and pos != 3 and pos != (system_picked_word_len-1):
        display[pos] = "_"


print(f"\nSystem Picked word is: {display}")

lives = 7

while list(system_picked_word) != display:
    user_input = input("Enter a letter to guess the system picked word: \n")
    lives_reduced = True
    for letter_pos in range(system_picked_word_len):
        if user_input == system_picked_word[letter_pos]:
            lives_reduced = False
            display[letter_pos] = user_input
    if lives_reduced == True:
        lives -= 1
        if lives == 0:
            print("\nNo Life left. You Loose the Game!!")
            print("---------")
            print(hangman_arts.stages[lives])
            break
        print(f"You loose a life. Lives remaining: {lives}")
        print("---------")
        print(hangman_arts.stages[lives])
    else:
        print(f"Word is: {display}")

if list(system_picked_word) == display:
    print("You WIN the Game!")


