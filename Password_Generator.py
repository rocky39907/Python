# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+']

print("\nMaximum allowed Password length is 24. "
      "Please select your combination between Letters, Numbers and Symbols accordingly!\n")

answer = "yes"
while answer.lower() == "yes":
    nr_letters = int(input("How many letters do you want?\n"))
    nr_numbers = int(input("How Many Numbers you want?\n"))
    nr_symbols = int(input("How many symbols you want?\n"))

    pwd_length = nr_letters + nr_numbers + nr_symbols

    if pwd_length > 24:
        print("Password length can't be longer than maximum allowed 24 characters! Please try again!\n")
    else:
        pwd = ""
        # Looping till Pwd length to generate the pwd
        for l in range(pwd_length):
            # Keep checking and adding a letter to the pwd string
            # till it reaches number of letters user wished for in the pwd
            if l < nr_letters:
                position_letter = random.randint(0,51)
                pwd = pwd + letters[position_letter]
            # Keep checking and adding a number to the pwd string
            # till it reaches number of numbers user wished for in the pwd
            if l < nr_numbers:
                position_number = random.randint(0,9)
                pwd = pwd + numbers[position_number]
            # Keep checking and adding a symbol to the pwd string
            # till it reaches number of symbols user wished for in the pwd
            if l < nr_symbols:
                position_symbols = random.randint(0,10)
                pwd = pwd + symbols[position_symbols]
        # Jumbling the created pwd string.
        # Then converting the string to a list and
        # shuffling using shuffle() function before converting the list back to a string using join()
        pwd_l = list(pwd)
        random.shuffle(pwd_l)
        final_pwd = ''.join(pwd_l)
        print(f"Your password is: {final_pwd}")

        answer = "no"
