'''Playground for functions'''


def reverse(str):
    flipped = str[::-1]
    return flipped


user_input = input("Enter what you wish to be reversed: ").strip()
print(reverse(user_input))
