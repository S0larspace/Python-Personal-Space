'''practice for OOP'''
import random


class Coin:
    # child data is packed in the dictionary called kwargs
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
        # kwargs = KeyWord ARGuments

        for key, value in kwargs.items():
            # what this does: create and set an attribute of self.key(parameter) = value, similar to a constructor
            setattr(self, key, value)

        self.is_rare = rare  # assignment of default parameters
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def flip(self):
        heads_options = [True, False]  # list
        choice = random.choice(heads_options)
        self.heads = choice

     # Destructor method, note the __del__ naming method
    def __del__(self):
        # Will be automatically called upon del method execution of the coin object type
        print("Coin Spent!")

    def __str__(self):  # Formatting the output when printing out the coin objects themselves, because otherwise there would be a bunch of weird lines
        if self.original_value >= 1.00:
            return "£{} Coin".format(int(self.original_value))
        else:
            return "{}p Coin".format(int(self.original_value*100))


class One_Pence(Coin):  # inheriting the Coin class
    def __init__(self):
        data = {
            "original_value": 0.01,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
        }

        # calling the parent constructor using super() and unpacking the child information stored in the dictionary "data"
        super().__init__(**data)


class Two_Pence(Coin):  # inheriting the Coin class
    def __init__(self):
        data = {
            "original_value": 0.02,
            "clean_colour": "bronze",
            "rusty_colour": "brownish",
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
        }

        # calling the parent constructor using super() and unpacking the child information stored in the dictionary "data"
        super().__init__(**data)


class Five_Pence(Coin):  # inheriting the Coin class
    def __init__(self):
        data = {
            "original_value": 0.05,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.25
        }

        # calling the parent constructor using super() and unpacking the child information stored in the dictionary "data"
        super().__init__(**data)

        # Override the parent function (Polymorphism: When a function has multiple versions within a class)
        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour


class Ten_Pence(Coin):  # inheriting the Coin class
    def __init__(self):
        data = {
            "original_value": 0.10,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 24.5,
            "thickness": 1.85,
            "mass": 6.50
        }

        # calling the parent constructor using super() and unpacking the child information stored in the dictionary "data"
        super().__init__(**data)

        # Override the parent function (Polymorphism: When a function has multiple versions within a class)
        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour


class Twenty_Pence(Coin):  # inheriting the Coin class
    def __init__(self):
        data = {
            "original_value": 0.20,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 21.4,
            "thickness": 1.7,
            "mass": 5.00
        }

        # calling the parent constructor using super() and unpacking the child information stored in the dictionary "data"
        super().__init__(**data)

        # Override the parent function (Polymorphism: When a function has multiple versions within a class, due to overriding from a child class)
        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour


class Fifty_Pence(Coin):  # inheriting the Coin class
    def __init__(self):
        data = {
            "original_value": 0.50,
            "clean_colour": "silver",
            "rusty_colour": None,
            "num_edges": 7,
            "diameter": 27.3,
            "thickness": 1.78,
            "mass": 8.00
        }

        # calling the parent constructor using super() and unpacking the child information stored in the dictionary "data"
        super().__init__(**data)

        # Override the parent function (Polymorphism: When a function has multiple versions within a class)
        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour


class One_Pound(Coin):  # inheriting the Coin class
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        }

        # calling the parent constructor using super() and unpacking the child information stored in the dictionary "data"
        super().__init__(**data)


class Two_Pound(Coin):  # inheriting the Coin class
    def __init__(self):
        data = {
            "original_value": 2.00,
            "clean_colour": "gold & silver",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 28.4,
            "thickness": 2.50,
            "mass": 12.00
        }

        # calling the parent constructor using super() and unpacking the child information stored in the dictionary "data"
        super().__init__(**data)


# ------------------------------------------------------Test Area-----------------------------------------------------------------
coins = [One_Pence(), Two_Pence(), Five_Pence(), Ten_Pence(),
         Twenty_Pence(), Fifty_Pence(), One_Pound(), Two_Pound()]
for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness,
                 coin.num_edges, coin.mass]  # packing the properties into a list

    # unpacking arguments into format
    string = "{} - Colour: {}, value: {}, diameter(mm): {}, thickness(mm): {}, number of edges: {}, mass(g): {}".format(
        *arguments)
    print(string)

# Note that we will see the deconstructor message carried out because the object is deleted prior to the program closing
