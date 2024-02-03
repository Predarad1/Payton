import os
from time import sleep

def plantCrop():
    os.system('cls')
    print("Crop Planted")

def waterCrop():
    os.system('cls')
    print("Crop Watered")

def harvestCrop():
    os.system('cls')
    print("Crop Harvested")

def goToMarket():
    os.system('cls')
    print("Welcome To The Market")

def quitGame():
    print("Game Over! Have a very save day!")
    exit(1)

def banner():
    print("+--------------------------------+")
    print("|     Welcome to FarmVille       |")
    print("+--------------------------------+")
    print("                                  ")

def stats(day, nr_crops, money):
    print("----------------------------------")
    print(f"Day {day}")
    print(f"Total crops = {nr_crops}")
    print(f"Money = ${money}")
    print("----------------------------------")
    print("                                  ")

def mainMenu():
    print("----------------------------------")
    print("What Do You Want to Do?")
    print("1. Plant a Crop")
    print("2. Water All Plants")
    print("3. Harvest Crop")
    print("4. Go To Market")
    print("5. Quit")
    print("----------------------------------")
    print("                                  ")


def userChoice():
    print("----------------------------------")
    while True:
        try:
            choice = int(input("What Is Your Choise? "))
            if 1 <= choice <= 5:
                break
            else:
                print("!INVALID INPUT! Please enter a number from 1-5.")
        except ValueError:
            print("!INVALID INPUT! Please DO NOT input a letter")
    print("----------------------------------")
    print("                                  ")

def perform_action(choice):
    match choice:
        case 1:
            plantCrop()
        case 2:
            waterCrop()
        case 3:
            harvestCrop()
        case 4:
            goToMarket()
        case 5:
            quitGame()
        case _:
            print("Invalid action!")

def get_user_choice():
    print("----------------------------------")
    while True:
        try:
            choice = int(input("Choise: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("!INVALID INPUT! Please enter a number from 1-5.")
        except ValueError:
            print("!INVALID INPUT! Please DO NOT input a letter")
    print("----------------------------------")
    print("                                  ")
