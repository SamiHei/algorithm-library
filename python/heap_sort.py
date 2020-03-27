#! /usr/bin/python3

import random


# Test program
def main():
    test = create_test_array(15)
    print("Start:\n", test)
    sorted = heap_sort(test, len(test)-1)
    print("Sorted:\n", sorted)


# Creates array for testing where index 0 is the amount of the values
def create_test_array(size):
    test = [size]
    for i in range(size):
        test.append(random.randrange(0, 100))
    return test


# Creates and sorts heap from array
def heap_sort(array, n):
    array = make_heap(array)
    for x in range(n, 1, -1):
        swap(array, x)
        array[0] -= 1
        fix_heap(array, 1)
    return array


# Swaps arrays value from index 1 with arrays value from index i
def swap(array, i):
    array[1], array[i] = array[i], array[1]
    return array


# Makes heap from given array using fix heap method
def make_heap(array):
    for x in range((int)(len(array) / 2), 0, -1):
        fix_heap(array, x)
    return array


# Fixes heap ordering
def fix_heap(array, i):
    if (2*i > array[0]):
        return array
    j = 2*i
    item = array[i]
    while (j <= array[0]):
        if ((j < array[0]) and (array[j] > array[j+1])):
            j = j+1
        if (item <= array[j]):
            break
        array[(int)(j/2)] = array[j]
        j = 2*j
    array[(int)(j/2)] = item
    return array


if __name__ == "__main__":
    main()

