'''This program aims to receive an input from the user and counts the number of vowels and consonants in it.'''
import math
import string

loop = True


def is_punctuation(char):
    '''Checks if the character is a punctuation mark'''
    return char in string.punctuation  # returns boolean if char is a punctuation


# Welcome statement
print("Welcome to the Vowel/Consonant counter.\n")

while loop == True:
    # Resetting the vowel and consonants counts if program loop is not terminated
    vowels = 0
    consonants = 0
    input_validity = True

    # obtain inputs
    og_string = input(
        "Please enter the word or sentence that needs counting: ")
    user_string = og_string.strip().lower()

    # Input processing
    for letter in user_string:
        if letter in "aeiou":
            vowels += 1
        elif letter not in "aeiou":
            if letter.isnumeric():  # checking for numbers
                continue
            # calls the function is_punctuation to check if the char is in the list of valid punctuations and returns a boolean
            elif is_punctuation(letter):
                continue
            elif letter.isspace():  # checking for whitespaces
                continue
            else:
                consonants += 1
        else:
            input_validity = False
            print("Invalid input.")
            break

    # Ensure that if input is invalid, don't even bother with the results.
    if input_validity == True:
        print("For the input \'{}\':\n The number of vowels are {}.\n The number of consonants are {}.\n".format(
            og_string, vowels, consonants))

    # Check for user input to repeat the program
    check_loop = input(
        "Do you wish to check a new input? (Y/N): ").strip().lower()
    if check_loop != 'y':  # consider invalid inputs as program termination
        loop = False
    if check_loop != 'n':
        print("\nInvalid input enterred, program will be terminating.")


print("End of program. Bye.\n")
