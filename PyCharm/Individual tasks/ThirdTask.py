#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    print("All distribution options for rabbits and ducks:")

    # The loop is taken up to 16 because the maximum of rabbits in the absence of ducks will be equal to 64/4=16
    for rabbits in range(16):

        # The cycle is taken up to 32 because the maximum ducks in the absence of rabbits will be 64/2=32
        for ducks in range(32):

            # Checking the number of paws
            if rabbits * 4 + (ducks * 2) == 64:

                # Output the numbers of animals
                print("Number of rabbits:", rabbits,
                      "\nNumber of ducks:", ducks, "\n")
