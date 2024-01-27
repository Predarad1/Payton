from methods import *
from time import sleep

if __name__ == "__main__":
    list_crops = ["Carrot", "Tomato", "Potato", "Corn", "Wheat", "Pumpkin", "Cucumber", "Strawberry", "Blueberry", "Lettuce"]

    money = 100
    nr_crops = 5
    day = 1

    banner()
    sleep(2)

    stats(day, nr_crops, money)
    sleep(2)

    mainMenu()
    sleep(2)




