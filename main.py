# Password Generator Project
import random
from string import ascii_letters
from string import digits
from string import punctuation

if __name__ == '__main__':
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    # Assuming that nr_letters, symbols and numbers are valid
    random_letters = random.sample(ascii_letters, nr_letters)
    random_symbols = random.sample(punctuation, nr_symbols)
    random_numbers = random.sample(digits, nr_numbers)

    # Combine and shuffle the random characters
    combined_characters = random_letters + random_symbols + random_numbers
    random.shuffle(combined_characters)

    # print(random_letters)
    # print(random_symbols)
    # print(random_numbers)

    # Join a list of random characters into a string
    random_password = ''.join(combined_characters)
    print(random_password)
