#! /usr/bin/python3

import random

def main():
    # Test function here
    test_array = []
    for i in range(50):
        test_array.append(random.randrange(0, 10000))
    print(test_array)
    print("==========================")
    print(selection_sort(test_array))


def selection_sort(array):
    array_length = len(array)
    for i in range(array_length):
        smallest_value = array[i]
        smallest_value_index = i
        
        for j in range(i+1, array_length):
            if(array[j] < smallest_value):
                smallest_value = array[j]
                smallest_value_index = j
               
        array[i], array[smallest_value_index] = array[smallest_value_index], array[i]

    return array


if __name__ == "__main__":
    main()
