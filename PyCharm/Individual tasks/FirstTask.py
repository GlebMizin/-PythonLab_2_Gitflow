#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":

    # List of numbers
    NumList = [
    'one',
    'two',
    'three',
    'four',
    'five', 
    'six', 
    'seven', 
    'eight'
    ]

    # Number input
    number = int(input("Enter number (|C|<9): "))

    # Number range check
    if number <= -9 or number >= 9:
        print("Your number is out of range")

    # Displaying a number with a sign
    else:
        if number < 0:
            print('Your number is: minus ' + NumList[(number*-1)-1])
        elif number > 0:
            print('Your number is: ' + NumList[number-1])
        else:
            print('Your number is: zero')
