#! /usr/bin/python3


"""
Algorithm adds values to given array using hash function
In this case hash function is (k mod m) + i where:
     k is the given value
     m is the array size
     i is value between 0..m-1

Searching the value in the array is done by using linear search

In the array:
    0 presents empty slot
   -1 presents deleted value

main program contains example use of the algorithm
"""
def main():
    t = [0,0,0,0,0,0,0,0,0,0]
    m = 10

    values_to_be_added = [21,55,31,49,52,72,26,19]
    values_to_be_deleted = [72, 21, 109]
    

    for x in values_to_be_added:
        add(t, m, x)
        print("Add {0}: {1}".format(x,t))

    print()
    print("Result array: ", t)
    print()

    for x in values_to_be_deleted:
        delete(t, m, x)
        print("Delete {0}: {1}".format(x,t))

    print()
    print("Result array: ", t)
    print()
    

def hash(k, m, i):
    return (k % m) + i


def add(array, m, value):
    for i in range(0, m-1):
        index = (hash(value, m, i) % m)
        if (array[index] == 0 or array[index] == -1):
            array[index] = value
            return 0 # return 0 if add succeeded
    return -1 # If adding failed returns -1


def delete(array, m, value):
    for i in range(0, m-1):
        index = (hash(value, m, i) % m)
        if (array[index] == value):
            array[index] = -1 # If value found remove it by inserting -1
            return 0 # delete succeeded
        elif (array[index] == 0 or array[index] == -1):
            return -1 # delete failed
        continue


if __name__ == "__main__":
    main()
