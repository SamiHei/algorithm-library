#! /usr/bin/python3

import random

# NOTE: Tested typing python function parameters

def main():

    random_numbers: [int] = []

    random_numbers = generate_random_numbers(1000)

    print(is_divisible_for_given_amount_numbers(random_numbers, 2, 3, 5))

def is_divisible_for_given_amount_numbers(random_numbers_array: [int], *argv: int):
    """
    Args:
        random_numbers_array (int[]): Array of random numbers
        *argv (int): Values that the random numbers needs to divisible

    Returns:
        Amount of numbers that were divisible for all the given *argv numbers
    """
    
    is_divisble_amount: int = 0

    for random_number in random_numbers_array:
        for arg in argv:
            if(random_number % arg == 0):
                is_still_divisible = True
                continue
            else:
                is_still_divisible = False
                break

        if(is_still_divisible):
            is_divisble_amount += 1

    return is_divisble_amount


def generate_random_numbers(amount: int):
    """
    Args:
        amount (int): Amount of numbers to be generated between 0 to 1000 to array

    Returns:
        Array of generated random numbers
    """
    random_numbers: [int] = []

    while(len(random_numbers) < amount):
        random_numbers.append(random.randrange(0, 1000))

    return random_numbers

if __name__ == "__main__":
    main()
