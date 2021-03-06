#! /usr/bin/python3


def main():
    # Test function here
    test_array = [155, 220, 707, 997, 1013, 1125, 1300, 1346, 1591, 1716, 1864,
                  1873, 1923, 2044, 2432, 2677, 2994, 3085, 4030, 4058, 4172,
                  4378, 4424, 4547, 4598, 4791, 4797, 5961, 6044, 6488, 6640,
                  6703, 6867, 6873, 6989, 7671, 7823, 7850, 7909, 8155, 8248,
                  8437, 8662, 9030, 9454, 9553, 9661, 9760, 9789, 9899]
    print(binary_search(test_array, 4791))


def binary_search(array, search_value):
    """
    Args:
    array (int[]): Sorted array
    search_value (int): Value to be searched

    Returns:
    Index of the searched value in the given array
    (If not found returns -1)
    """
    array_length = len(array)
    index = 0
    while(array_length > 1):
        if(search_value < array[array_length//2] and array_length > 1):
            index += binary_search(array[:(array_length//2)], search_value)
        elif(search_value > array[array_length//2] and array_length > 1):
            index = binary_search(array[((array_length//2)+1):], search_value)
            index += ((array_length//2)+1)
        elif(search_value == array[array_length//2]):
            index += array_length//2
            return index
        break

    if(index > (array_length-1) or search_value != array[index]):
        return -1
    return index


if __name__ == "__main__":
    main()
