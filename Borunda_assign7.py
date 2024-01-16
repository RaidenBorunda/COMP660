#!/usr/bin/env python3

### Assignment Seven - Birthday Calculator
### Author: Raiden Borunda

import datetime

def displayTitle():
    print("Birthday Calculator\n")

def birthdayCalc():
    name = input("Enter name: ")
    birthday = input("Enter birthday (MM/DD/YY): ")
    x = 0
    y = 0
    print("Birthday: ")
    print("Today: ")
    print(f'{name} is {x} years old ')
    print(f"{name}'s birthday is in {y} days")


def main():
    displayTitle()
    cont = input("Continue? (y/n): ")
    while cont.lower() == 'y':
        birthdayCalc()
        cont = input("Continue? (y/n:): ")
    # Exit program if user input is n
    print('Bye!')

if __name__ == "__main__":
    main()


