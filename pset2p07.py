# #7
# Write a function isPrime(N) that returns whether or not the number N is prime. A number is prime if it is divisible only by itself and 1 (note that the number 1 itself is not prime).

# isPrime(1) 	# False
# isPrime(2)	# True
# isPrime(3)	# True
# isPrime(4)	# False
# isPrime(5)	# True
# isPrime(6)	# False
# isPrime(7)	# True
# isPrime(19)	# True
# isPrime(20)	# False
# isPrime(37)	# True
import math
def isPrime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, (int(math.sqrt(num)) + 1)):
            if num % i == 0:
                return False
        return True


print(isPrime(1))   # False
print(isPrime(2))   # True
print(isPrime(3))   # True
print(isPrime(4))	# False
print(isPrime(5))	# True
print(isPrime(6))	# False
print(isPrime(7))	# True
print(isPrime(19))	# True
print(isPrime(20))	# False
print(isPrime(37))  # True
