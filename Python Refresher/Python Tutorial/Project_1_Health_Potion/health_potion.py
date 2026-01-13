# Project #1: Code a health potion that gives a certain amount of health to a player.
import random
import math

START_HEALTH = 50  # player's starting health
MAX_HEALTH = 100  # Maximum possible player health
MIN_HEALTH = 0  # Minimum possible player health
difficulty = 1  # Difficulty setting, 1 for easy, 2 for medium and 3 for hard

health = START_HEALTH  # setting the player's current health
print("The player's starting health was " + str(health) + ".\n")

# utilising the randint function under the random module that was imported
# floor function from the math module rounds down the float number to the nearest integer
potion_health = math.floor(random.randint(25, 50) / difficulty)
print("Using potion now....\nThe amount of health restored is " +
      str(potion_health) + ".\n")

health += potion_health
print("The player's current health has been restored to " + str(health) + ".")
