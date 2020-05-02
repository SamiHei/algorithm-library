#! /usr/bin/python3

import random
import math


# Test program
def main():
    approx = calculate_pi_approximation(50)
    difference = math.pi - approx
    print("Pi approximate value using 50 random points:\t\t" + str(approx) + "\t\tdifference to Python3 math.pi value:\t" + str(difference))

    approx = calculate_pi_approximation(100)
    difference = math.pi - approx
    print("Pi approximate value using 100 random points:\t\t" + str(approx) + "\t\tdifference to Python3 math.pi value:\t" + str(difference))

    approx = calculate_pi_approximation(1000)
    difference = math.pi - approx
    print("Pi approximate value using 1000 random points:\t\t" + str(approx) + "\t\tdifference to Python3 math.pi value:\t" + str(difference))

    approx = calculate_pi_approximation(10000)
    difference = math.pi - approx
    print("Pi approximate value using 10000 random points:\t\t" + str(approx) + "\t\tdifference to Python3 math.pi value:\t" + str(difference))

    approx = calculate_pi_approximation(50000)
    difference = math.pi - approx
    print("Pi approximate value using 50000 random points:\t\t" + str(approx) + "\t\tdifference to Python3 math.pi value:\t" + str(difference))

    approx = calculate_pi_approximation(100000)
    difference = math.pi - approx
    print("Pi approximate value using 100000 random points:\t" + str(approx) + "\t\tdifference to Python3 math.pi value:\t" + str(difference))


'''
Calculates the approximate value of pi by adding points inside square which contains max size circle and calculates
which points are inside the circle and which are not. For those points we use formula 4k/n where k is the points
inside the circle and n is the overall amount of the points
     amount_of_points = points set to the coordinate system (more points increases the accuracy)
'''
def calculate_pi_approximation(amount_of_points):
    
    rand_generated_points = []

    # 100 is the radius of the circle and the center is point (0, 0)
    for p in range(amount_of_points):
       x = random.uniform(-100.0, 100.0)
       y = random.uniform(-100.0, 100.0)
       point = (x, y)
       rand_generated_points.append(point)

    points_inside_circle = 0

    # Check if point is inside the circle
    for p in rand_generated_points:
        if ((p[0]**2 + p[1]**2) <= 100.0**2):
            points_inside_circle += 1

    # Calculate the pi using the formula 4k/n
    result = (4 * points_inside_circle) / len(rand_generated_points)
    return result
    

if __name__ == "__main__":
    main()
