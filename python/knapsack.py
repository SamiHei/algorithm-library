#! /usr/bin/python3

# NOTE: I am not sure about this solution is it correctly done, more of a googling and trying to understand the problem
# than actually realizing the idea and solution


def main():

    values = [342, 123, 456, 594, 321, 125, 483, 101, 522, 298]
    weights = [10, 43, 23, 12, 59, 32, 21, 12, 95, 10]
    overall_weight = 99

    result = solve_knapsack(values, weights, overall_weight)

    print(result[-1][-1]) # prints the last value in the whole 2 dimensional array (right bottom corner)


def solve_knapsack(v, w, W):
    result_table = [ [0 for i in range(0, W)] for j  in range(0, len(v))] # preps empty 2 dimensional array
    
    for i in range(1, len(v)):
        for j in range(0, W):
            if (w[i] > j):
                result_table[i][j] = result_table[i-1][j]
            else:
                result_table[i][j] = max(result_table[i-1][j], result_table[i-1][j - w[i]] + v[i])
    return result_table


if __name__ == "__main__":
    main()

