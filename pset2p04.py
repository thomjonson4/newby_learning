# #4
# Write a function medianArray(nums) that computes and returns the median of a list of numbers.
# medianArray([4,2,7,5,5])	# 5
# medianArray([2,1,88,3])		# 2.5 (average of 2 and 3 since they are both in the middle)

import math
# print(int(math.ceil(4.2)))
def medianArray(nums):
    sortedArray = sorted(nums)
    if len(nums) % 2 == 0:
        middle_2 = sortedArray[int((len(nums) / 2))]
        middle_1 = sortedArray[int((len(nums) / 2 - 1))]
        return ((middle_1 + middle_2) / 2)
    else:
        median_num = int(math.ceil(len(nums) / 2))
        return sortedArray[median_num]

print(medianArray([4,2,7,5,5]))
print(medianArray([2,1,88,3]))