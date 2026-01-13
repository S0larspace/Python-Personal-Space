'''Playground for functions'''


def reverse(str):
    flipped = str[::-1]
    return flipped

# user_input = input("Enter what you wish to be reversed: ").strip()
# print(reverse(user_input))


# IMPT note that parameters with a default have to be POSITIONED LAST OR it would give an ERROR
def about(name, age=20, likes="Python"):
    output = ("Meet {}, they are {} years old and they like {}".format(
        name, age, likes))
    return output


# print(about("Jack"))
dictionary = {"name": "Brendan", "age": 30, "likes": "gaming"}
# utilising a dictionary to unpack data into a formatted string
# print(about(**dictionary))  # note the double **


def add(*numbers):  # the input gets added into a tuple called "numbers", involves a concept called packing
    # packing is useful when the number of inputs are uncertain
    total = 0
    for number in numbers:
        total += number
    return total


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))

def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))


foo(Username="User1423", PW="ILoveMyPW", Value=9999)
