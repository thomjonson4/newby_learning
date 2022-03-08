# #6
# Write a function printPyramid(N) that prints a pyramid of height N:

# printPyramid(3):

#   *
#  ***
# *****

# printPyramid(4):

#    *
#   ***
#  *****
# *******

def printPyramid(x):
    for i in range (0, x):
        print((" " * (x-1-i)) + ("*" * (i * 2 + 1)))

printPyramid(5)