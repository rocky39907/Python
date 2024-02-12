import random

def number_comparison(lives):
    """Takes number of allowed attempt and give User that many chances
    to guess a randomly picked number by system."""
    print(f"You have {lives} attempts to guess the number to Win the game!\n")
    sys_number = random.randint(1,100)
    if sys_number in range(1,25):
        print("Number is in between 1-25")
    elif sys_number in range(26,50):
        print("Number is in between 26-50")
    elif sys_number in range(51,75):
        print("Number is in between 51-75")
    else:
        print("Number is in between 76-100")

    while lives > 0:
        lives -= 1
        user_number = int(input("Guess a number: \n"))
        if user_number == sys_number:
            print(f"\nYou guessed the correct number. It's {user_number}. You WIN!")
            break
        elif lives == 0:
            print("You have no more attempt left. You Loose!")
        elif sys_number < user_number:
            print("Too High!")
            print(f"Attempt left: {lives}")
        else:
            print("Too Low!")
            print(f"Attempt left: {lives}")


invalid_level = True
while invalid_level:
    level = input("Please select the level you wish to play; 'easy' or 'hard':\n")
    if level.lower() == 'easy':
        number_comparison(10)
        invalid_level = False
    elif level.lower() == 'hard':
        number_comparison(5)
        invalid_level = False
    else:
        print("Invalid level selection. Please try again!")