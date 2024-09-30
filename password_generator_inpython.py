# Import the random module to use its functions for generating random elements
import random

# Create a list of lowercase and uppercase letters for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Create a list of numeric characters for the password
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Create a list of special characters (symbols) to be used in the password
symbols = ['#', '$', '%', '&', '*', '_']

# Shuffle the lists of letters, numbers, and symbols to randomize their order
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

# Display a welcome message for the user
print("Welcome to the Python Password Generator!")

# Ask the user how many letters, symbols, and numbers they want in their password
nr_letters = int(input("How many letters would you like in your password: "))
nr_symbols = int(input("How many symbols would you like: "))
nr_numbers = int(input("How many numbers would you like: "))

# Initialize an empty list to store the password characters
password = []

# Randomly select 'nr_letters' letters from the shuffled letters list and add to password list
for i in range(0, nr_letters):
    password.append(random.choice(letters))

# Randomly select 'nr_symbols' symbols from the shuffled symbols list and add to password list
for i in range(0, nr_symbols):
    password.append(random.choice(symbols))

# Randomly select 'nr_numbers' numbers from the shuffled numbers list and add to password list
for i in range(0, nr_numbers):
    password.append(random.choice(numbers))

# Shuffle the characters in the password list to ensure randomness
random.shuffle(password)

# Initialize an empty string to store the final password
password_result = ""

# Variable 'i' is used to iterate through the list elements
i = 0

# Loop through each character in the password list and concatenate it to the password_result string
for letter in password:
    password_result = password_result + password[i]
    i += 1

# Print the newly generated password for the user
print("\n\nNewly generated password: " + password_result)

# Creator and date information
print("\n\nCREATOR/DEVELOPER = Aishik Mukherjee")
print("DATE: 01-10-2024")

input("\nPress ENTER to exit")
