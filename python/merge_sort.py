#! /usr/bin/python3

import random

def main():
    test_array = []
    for i in range(50):
        test_array.append(random.randrange(0, 10000))
    print(test_array)
    print("=" * 150)
    print(merge_sort(test_array))

    
def merge_sort(array):
    if(len(array) <= 1):
        return array

    mid = len(array)//2
    left_array = array[:mid]
    right_array = array[mid:]
    
    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)
    
    return merge(left_array, right_array)


def merge(left_array, right_array):

    new_array = []
    while(left_array and right_array):
        if(left_array[0] <= right_array[0]):
            new_array.append(left_array[0])
            del left_array[0]
        else:
            new_array.append(right_array[0])
            del right_array[0]

    while(left_array):
        new_array.extend(left_array)
        del left_array[:]
    while(right_array):
        new_array.extend(right_array)
        del right_array[:]

    return new_array


if __name__ == "__main__":
    main()

