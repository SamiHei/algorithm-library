# bin/bash/python3

def main():
    print("*** You can test all functions here ***")

def pop(array):
    try:
        arrays_first_value = array.pop(0)
        return arrays_first_value
    except:
        return None

def push(new_value, array):
    array.insert(0, new_value)

def is_empty(array):
    if(size(array) == 0):
        return True
    else:
        return False

def size(array):
    return len(array)

def top(array):
    try:
        return array[0]
    except:
        return None

if __name__ == '__main__':
    main()
