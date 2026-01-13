films = {
    "Finding Nemo": [3, 1],
    "Lord Of The Rings": [12, 5],
    "Avatar: Ash And Fire": [15, 5]
}

while True:
    choice = input(
        "Hello, welcome to XY Cinemas. What film do you wish to watch today?: ").strip().title()
    if choice in films:
        # input converts user input into a string so typecasting to integer is necessary

        # Check user age
        age = int(input("How old are you?: ").strip())

        if age >= films[choice][0]:

            # Checking availability of tickets
            if films[choice][1] > 0:
                print("Your ticket has been printed, enjoy your film!")
                films[choice][1] -= 1
            else:
                print("Sorry, but that film is fully sold out.")

        else:
            print("You are too young for that film.")

    else:
        print("That film is not in our theaters currently.")
