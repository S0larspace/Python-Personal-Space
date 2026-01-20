'''Translating words or sentences into an imaginary nonsense language that would make it unintelligible'''

# Welcome statement
print("Welcome to the Pig Latin translator.\n")

# Obtain user input
original = input(
    "Please enter the word or sentence to be converted: ").strip().lower()

# Split sentence into individual words
words = original.split()  # split() function creates a list from separating a sentence
# print(words)

# Loop through words and convert to Pig Latin
new_words = []

for word in words:

    # if starts with vowel, add "yay" to the end
    if word[0] in "aeiou":
        new_word = word + "yay"
    else:  # otherwise, move first consonant cluster to the end and add "ay"
        vowel_pos = 0
        consonant_cluster = ""
        for letter in word:
            if word[vowel_pos] not in "aeiou":
                # increment vowel_pos
                vowel_pos += 1
            else:
                # moving the consonant cluster into another variable
                consonant_cluster = word[:vowel_pos]
                # upon reaching the vowel, amend the original word
                new_word = word[vowel_pos:] + consonant_cluster + "ay"

                # no increment needed since this is the exit condition
                # exit the loop
                break

    # add to new_words list regardless of which case
    new_words.append(new_word)
    # print(new_words)

# Stick words back together
# .join() allows combining of the elements of a list with the spacing of whatever is before the .join statement
output = " ".join(new_words)

# Output final string
print(output)

# End of Program
print("\nEnd of Program.")
