# array = [1, 2, 3, 4, 5]
# print(len(array))

array = [30, 50, 20, 100]


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
print(sumArray([1,1,2]))	# 4
print(sumArray([10,-2]))	# 8
print(sumArray([]))         # 0