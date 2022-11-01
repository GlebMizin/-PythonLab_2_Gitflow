#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":

    # List of numbers
    num_list = [
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
    c_number = int(input("Enter number (|C|<9): "))

    # Number range check
    if c_number <= -9 or c_number >= 9:
        print("Your number is out of range")

    # Displaying a number with a sign
    else:
        if c_number < 0:
            print('Your number is: minus ' + num_list[(c_number*-1)-1])
        elif c_number > 0:
            print('Your number is: ' + num_list[c_number-1])
        else:
            print('Your number is: zero')
