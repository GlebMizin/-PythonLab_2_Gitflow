#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__ == "__main__":

    # Entering the coordinates of the first and second points
    a1, a2 = map(int, input("Enter first point coordinates: ").split())
    b1, b2 = map(int, input("Enter second point coordinates: ").split())

    # Calculating the distance to a point from the origin
    A_point = math.sqrt(a1 ** 2 + a2 ** 2)
    B_point = math.sqrt(b1 ** 2 + b2 ** 2)

    # Comparison of the obtained values and conclusion
    if A_point > B_point:
        print("Point A is farther than B")
    elif A_point < B_point:
        print("Point B is farther than A")
    else:
        print("Points are on the same distance")
