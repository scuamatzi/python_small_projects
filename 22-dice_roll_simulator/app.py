import random
import time

MIN_VAL = 1
MAX_VAL = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dices...")
    time.sleep(1)
    print("The value is:  ")

    print(random.randint(MIN_VAL, MAX_VAL))

    roll_again = input("Roll the dices Again (y/n)?  ")

print("\nByeee!")
