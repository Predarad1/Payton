from methods import *
from time import sleep
import os
 
if __name__ == "__main__":
    list_crops = ["Carrot", "Tomato", "Potato", "Corn", "Wheat", "Pumpkin", "Cucumber", "Strawberry", "Blueberry",
                  "Lettuce"]
    money = 100
    day = 1
    nr_crops = 5
    banner()
    stats(day, nr_crops, money)
    mainMenu()
    while True:
 
        user_choice = get_user_choice()
        perform_action(user_choice)
        sleep(4)
 

