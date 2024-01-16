#!/usr/bin/env python3

### Assignment Seven - Birthday Calculator
### Author: Raiden Borunda

## Programs should have a shebang and correctly called main() function.  Functions, iterations and conditionals should be used as needed. 
# The program should print the title of the program - "Birthday Calculator."
# Import the datetime module.  
# The program should accept as input a name and a birth date.  Allow the user to enter a date in the MM/DD/YY format. Adjust the date so that it is correct even if the birth year is later than the current year.
# The program should then display the person’s birthday, the current day, the person’s age, and the number of days until the person’s next birthday. 
# When you calculate the person’s age, don’t take leap year into account. 
# When you display the message that indicates the number of days to the person’s
# birthday, you can use the following format for a person with a name of John:
#     today - John's birthday is today!
#     tomorrow - John's birthday is tomorrow!
#     yesterday - John's birthday was yesterday!
#     other days - John's birthday is in X days.
# If the user does not continue, print an exit message (e.g. "Bye")  
# Example Program:

# Birthday Calculator

# Enter name: Joel
# Enter birthday (MM/DD/YY): 2/4/68

# Birthday: Sunday, February 04, 1968
# Today:    Tuesday, January 12, 2021
# Joel is 52 years old.
# Joel's birthday is in 23 days.

# Continue? (y/n): y

# Enter name: Barbra
# Enter birthday (MM/DD/YY): 12/1/07

# Birthday: Saturday, December 01, 2007
# Today:    Tuesday, January 12, 2021
# Barbra is 13 years old.
# Barbra's birthday is in 323 days.

# Continue? (y/n): y

# Enter name: Mike
# Enter birthday (MM/DD/YY): 1/12/86

# Birthday: Sunday, January 12, 1986
# Today:    Tuesday, January 12, 2021
# Mike is 35 years old.
# Mike's birthday is today!

# Continue? (y/n): n

# Bye!

## https://www.w3schools.com/python/python_datetime.asp

import datetime
from datetime import date
from datetime import datetime as dt

def displayTitle():
    print("Birthday Calculator\n")

def birthdayCalc():
    name = 'Raiden'
    # name = input("Enter name: ")
    # birthday = input("Enter birthday (MM/DD/YY): ")
    birthday = '10/06/93'
    # x = birthday.strftime("%A, %B %d, %Y")
    # print(x)

    todayDate = date.today()
    print(todayDate)
    birthday = birthday.split('/')
    if(int(birthday[2]) >= 00 and int(birthday[2]) <= 24): 
        birthday[2] = '20' + str(birthday[2])

    else: birthday[2] = '19' + birthday[2]
    print(birthday[2])

    month = birthday[0]
    day = birthday[1]
    year = birthday[2]
    formatted_birthday = f"{year}-{month}-{day}"
    print(formatted_birthday)
    # x = datetime.date(int(year), int(month), int(day))
    # x = formatted_birthday.strftime("%A, %B %D %Y")
    x = dt.now()
    formatted_birthday = x.strftime("%B %d, %Y")
    print(formatted_birthday)
    print(x)
    y = 0
    print("Birthday: ")
    print("Today: ")
    print(f'{name} is {x} years old ')
    print(f"{name}'s birthday is in {y} days")


def main():
    displayTitle()
    birthdayCalc()
    cont = input("Continue? (y/n): ")
    while cont.lower() == 'y':
        birthdayCalc()
        cont = input("Continue? (y/n:): ")
    # Exit program if user input is n
    print('Bye!')

if __name__ == "__main__":
    main()


