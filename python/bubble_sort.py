#! /usr/bin/python3

import random


def main():
    # Test function here
    test_array = []
    for i in range(500):
        test_array.append(random.randrange(0, 10000))
    print(test_array)
    print("==========================")
    print(bubble_sort(test_array))


def bubble_sort(array):
    array_length = len(array)
    for i in range(array_length):

        for j in range(array_length-i-1):
            if(array[j] > array[j+1]):
                array[j+1], array[j] = array[j], array[j+1]

    return array


if __name__ == "__main__":
    main()
