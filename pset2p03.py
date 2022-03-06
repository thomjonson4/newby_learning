# #3
# Write a function avgArray(nums) that computes and returns the average of a list of numbers.
# avgArray([5,6,7])		# 6
# avgArray([10,10,15])	# 11.666666666

array = [5,6,7]
def avgArray(array):
    i = 0
    sum = 0
    while i < len(array):
        if not array[i] == None:
            sum += array[i]
        i += 1
    return sum / len(array)

print(avgArray([5,6,7]))
print(avgArray([10,10,15]))