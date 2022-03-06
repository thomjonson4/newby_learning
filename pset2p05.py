# #5
# Write a function printStars(N) that prints a pattern of stars, with N being the number of rows. Example:


# printStars(3) prints:

# *
# **
# ***


# printStars(5):

# *
# **
# ***
# ****
# *****

def multiStar(input):
    if input != 0:
        count = 0
        output = ""
        while count != input:
            output += "*"
            count += 1
        return output
    else:
        print("")
# print(multiStar(5))

def printStars(num):
    if num > 0:
        numStars = 1
        while numStars <= num:
            print(multiStar(numStars))
            numStars += 1
printStars(5)
printStars(3)
