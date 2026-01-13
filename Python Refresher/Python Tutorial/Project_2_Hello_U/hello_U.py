# Program to ask user input for details
detail_validation = False

# Ask user for name
name = input("Hello user, what is your name? ").strip()

# Ask user for age
age = int(input("Hello " + name + ", how old are you? "))

# Ask user for city
city = input("What city do you live in, " + name + "? ").strip()

# Ask user what they enjoy
hobbies = input("Name one thing that you enjoy doing: ").lower().strip()

output = "{}, let me confirm your details. You are {} years old, living in {} and you love {}.".format(
    name, age, city, hobbies)
# Convenient tip: using .format() allows non-string variables to be formatted into a string without an explicit type-cast.
# .strip() removes either char or if left blank, all white space characters like tab and spaces and new lines and carriage returns, only from the beginning or trailing, not in between

# Print output to console
print(output)

# Space for playing around
print("\n\n---Following space is for experimentation---")

print(output)
# variable[start_index:end_index_not_inclusive:step] slices a string into the specified details, steps refer to pattern of characters to skip if any)
print(output[0::2])
# Setting step to -1 essentially inverts the whole string. Index of the final character in a string is also -1, so indexing can be done from the end if it's closer.
print(output[::-1])
