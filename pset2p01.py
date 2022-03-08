# #1
# Given an expression of the form ax^2 + bx + c
# Write a function roots(a,b,c) that returns the roots (as a tuple) of the quadratic equation (values of x for which the expression is equal to 0).
# Use the quadratic formula to do this (can look it up if you don't remember it).

import math

def root(a, b, c):
    if (b ** 2 - 4 * a * c) < 0:
        print("Error")
    else:
        root_1 = (((-1 * b) + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
        root_2 = (((-1 * b) - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a))
        return (root_1, root_2)
print(root(2, 5, 3))
print(root(2, 3, 5))