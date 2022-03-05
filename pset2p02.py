array = [1, 2, 3, 4, 5]
# print(len(array))


def sumArray(input):
    last_place = len(input)
    sum = 0
    i = 0
    while i < last_place:
        if not input[i] == None:
            sum += input[i]
        i += 1
    return sum

print(sumArray(array))
