### Assignment Four - Dice Roller
### Author: Raiden Borunda

#!/usr/bin/env python3
import random


def displayTitle():
    while True:
        cont = print("Welcome to Dice Roller!\nRoll the dice? (y/n:):")
        if cont != 'y':
            print("Thanks for playing!")
            break


def roll():
    return random.randint(1,6)

def rollDice(): 
    die1 = roll()
    die2 = roll()
    totalDice = die1 + die2
    print(f'Die 1: {die1}')
    print(f'Die 2: {die2}')
    print(f'Total: {totalDice}')
    if totalDice == 2 :
        print('Snake eyes!')
    elif totalDice == 12 :
        print('Boxcars!')

def main():
    displayTitle
    rollDice





if __name__ == "__main__":
    main()