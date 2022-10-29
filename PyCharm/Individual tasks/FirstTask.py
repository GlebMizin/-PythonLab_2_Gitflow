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
    C_number = int(input("Enter number (|C|<9): "))

    # Number range check
    if C_number <= -9 or C_number >= 9:
        print("Your number is out of range")

    # Displaying a number with a sign
    else:
        if C_number < 0:
            print('Your number is: minus ' + NumList[(C_number*-1)-1])
        elif C_number > 0:
            print('Your number is: ' + NumList[C_number-1])
        else:
            print('Your number is: zero')
