known_users = ["Alex", "Brenda", "Carlos", "Damien",
               "Ella", "Fred", "George"]  # This is case sensitive

print(len(known_users))

while True:
    print("\nHi! My name is Travis.")

    # Using title to eliminate generating dupes from user inconsistency in capitalising first letter of their name
    # capitalize() does similar, except title does it to every word in the string
    user_name = input('What is your name?: ').strip().title()
    if user_name in known_users:
        print("Welcome back, {}\n".format(user_name))
        remove = input(
            "Would you like to be removed from the system (Y/N)?:").lower()

        # print(known_users)
        if remove == "y":
            # remove removes first instance of the data, so problematic if there are duplicates
            known_users.remove(user_name)
            # use del list[indexnumber]
            # print(known_users)
        elif remove == 'n':
            print("No problem, I didn't want you to leave anyways!")

    else:
        print(
            "Hmm, you seem to be a new user.\n")
        add_user = input(
            'Would you like to be added to the system (Y/N)?: \n').strip().lower()

        # print(known_users)
        if add_user == 'y':
            known_users.append(user_name)
            # IMPT be careful when assigning a variable to an outcome of an append command as it overrides the existing data type to NONE, essentially deleting it
            # print(known_users)
        elif add_user == 'n':
            print("No worries, see you around!")


# tuples are iterable like list, except immutable (meaning data CANNOT BE CHANGED after initial creation), but they can be sliced etc
# useful for protecting existing data
# can be used on existing variables like A = tuple (A)
