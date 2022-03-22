# List = [character for character in "Geeks 4 Geeks!"]
# print(List)

# import time
 
 
# # define function to implement for loop
# def for_loop(n):
#     result = []
#     for i in range(n):
#         result.append(i**2)
#     return result
 
 
# # define function to implement list comprehension
# def list_comprehension(n):
#     return [i**2 for i in range(n)]
 
 
# # Driver Code 
 
# # Calculate time takens by for_loop()
# begin = time.time()
# for_loop(10**6)
# end = time.time()
 
# # Display time taken by for_loop()
# print('Time taken for_loop:',round(end-begin,2))
 
# # Calculate time takens by list_comprehension()
# begin = time.time()
# list_comprehension(10**6)
# end = time.time()
 
# # Display time taken by for_loop()
# print('Time taken for list_comprehension:',round(end-begin,2))


import requests
import string
import random
import typing
import math


# Comprehensions

# Generate a list of numbers from A up to B
#############################################
def generate_nums_loop(a: int, b: int) -> list[int]:
    nums = []
    for num in range(a, b):
        nums.append(num)
    return nums


def generate_nums_comprehension(a: int, b: int) -> list[int]:
    # General syntax of a list comprehension is:
    # [value for element in collection]

    # Could also have a condition for the comprehension, and the value is added
    # to the resultant list only if the condition is true
    # [value for element in collection if condition]

    return [num for num in range(a, b)]


def generate_nums_list_function(a: int, b: int) -> list[int]:
    return list(range(a, b))


# Compute list of even numbers from A up to B
#############################################

def generate_even_nums_loop(a: int, b: int) -> list[int]:
    # Remember python's ternary syntax:
    # (value if condition else other_value)
    # The above expression evaluates to value if the condition is true,
    # and evaluates to other_value otherwise

    # start with a if it's even, otherwise start with a + 1
    num = a if (a % 2 == 0) else a + 1
    nums = []
    while (num < b):
        nums.append(num)
        num += 2
    return nums


def generate_even_nums_comprehension_01(a: int, b: int) -> list[int]:
    return [num for num in range(a, b) if num % 2 == 0]


def generate_even_nums_comprehension_02(a: int, b: int) -> list[int]:
    return [num for num in range(a if a % 2 == 0 else a + 1, b, 2)]


# quick test
for a in range(0, 10):
    for b in range(0, 10):
        r1 = generate_even_nums_loop(a, b)
        r2 = generate_even_nums_comprehension_01(a, b)
        r3 = generate_even_nums_comprehension_02(a, b)
        assert(r1 == r2)
        assert(r2 == r3)


# how to repeat the above process if we had many more functions?
def test_functions(functions: list[typing.Callable], a_range: range, b_range: range):
    for a in a_range:
        for b in b_range:

            # get results using loop
            results = []
            for function in functions:
                results.append(function(a, b))

            # or using comprehension
            results = [function(a, b) for function in functions]

            # iterate over indeces in results list excluding the last index
            # so that we don't go out of bounds when checking [index + 1]
            for index in range(len(results) - 1):
                assert(results[index] == results[index + 1])

# Now we can test like this:


test_functions([
    generate_nums_loop,
    generate_nums_comprehension,
    generate_nums_list_function
], range(0, 10), range(0, 10))

test_functions([
    generate_even_nums_loop,
    generate_even_nums_comprehension_01,
    generate_even_nums_comprehension_02
], range(0, 10), range(0, 10))


# Some more examples of comprehensions


# Let's look at a few ways we could randomly
# generate usernames.
#############################################

# Get a random character
# from 'a' to 'z' (inclusive)
#############################################


def random_character_01():
    # Generates a random number from [0, 1)      [inclusive, exclusive)
    # Could be something like 0.235234, or 0.1887, or 0.00001234, or 0.999999222
    random_number = random.random()

    # Multiply the random number by 26, such that
    # we have a random number from [0, 26)
    # now could be something like 6.116084, or 4.9062, or 0.00032084 or 25.999979772
    # (BTW, string.ascii_lowercase is just the string 'abcdefghijklmnopqrstuvwxyz'.)
    random_number *= len(string.ascii_lowercase)

    # truncate any decimals using the int function
    # now could be something like 6, or 4, or 0, or 25
    random_index = int(random_number)

    # Use that index to pick a character from the alphabet
    return string.ascii_lowercase[random_index]


def random_character_01_oneliner():
    return string.ascii_lowercase[int(random.random() * len(string.ascii_lowercase))]


def random_character_02():
    # use random.sample function which randomly picks elements from a collection
    # number of elements to pick is the second argument to the function (in this its 1)
    # random.sample returns a list (the picked elements), so thats why we need [0] at the end,
    # to take the first item from the picked items (since we only need one in this case)
    return random.sample(string.ascii_lowercase, 1)[0]

# Very similar to random character_02


def random_digit():
    # (BTW, string.digits is just the string '0123456789'.)
    return random.sample(string.digits, 1)[0]


# Generate usernames like abcdef94
# consisting of 6 characters and two numbers
def generate_random_username_loop():
    username = ''
    for i in range(0, 6):
        # we could use any of the random_character functions we wrote here, they do the same thing
        username += random_character_01()

    for i in range(0, 2):
        username += random_digit()

    return username


# Using a comprehension
def generate_random_username_comprehension_01():
    # generate the letters part
    username_letters = [random_character_01() for _ in range(0, 6)]
    # generate the digits
    username_digits = [random_digit() for _ in range(0, 2)]

    # combine them
    username = username_letters + username_digits

    # username is currently a list of strings.
    # We can turn it into a string using the str.join method.
    # str.join(list) effectively connects each element of the list using the string
    # For example '-'.join('word1','word2','word3') would give you 'word1-word2-word3'
    # For example ' '.join('this','is','a','sentence') would give you 'this is a sentence'
    # For example ''.join( 'this','is','a','sentence') would give you 'thisisasentence'
    return ''.join(username)


def generate_random_username_comprehension_02():
    return ''.join(random.sample(string.ascii_lowercase, 6) + random.sample(string.digits, 2))

# generalize it with parameters so we can control length


def generate_random_username(characters_length, digits_length):
    return ''.join(
        random.sample(string.ascii_lowercase, characters_length) +
        random.sample(string.digits, digits_length)
    )


# Some more examples of simple comprehensions
###############################################
# exponentiating numbers
first_ten_squares = [num*num for num in range(10)]
first_ten_cubes = [num*num*num for num in range(10)]
first_ten_fourth_power = [num**4 for num in range(10)]

# lets make a general function


def first_n_to_power_of_x(n, x):
    return [num**x for num in range(n)]


assert(first_n_to_power_of_x(10, 2) == first_ten_squares)
assert(first_n_to_power_of_x(10, 3) == first_ten_cubes)
assert(first_n_to_power_of_x(10, 4) == first_ten_fourth_power)


def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for divisor in range(2, int(math.sqrt(n) + 1)):
        if n % divisor == 0:
            return False
    return True


# Generate prime numbers below 100
prime_nums = [num for num in range(100) if is_prime(num)]

# Squares of prime numbers below 100
square_prime_nums = [num**2 for num in prime_nums]
# same thing but from scratch (without using prime_nums we generated earlier)
square_prime_nums = [num**2 for num in range(100) if is_prime(num)]

# String representation of squares of prime numbers below 100
str_square_prime_nums = [str(num) for num in square_prime_nums]
# same thing but from scratch
str_square_prime_nums = [str(num**2) for num in range(100) if is_prime(num)]

# string representation of squares of prime numbers below 100, with "ZZZ" on either side
zzz_str_square_prime_nums = ["ZZZ" + str_num +
                             "ZZZ" for str_num in str_square_prime_nums]
# same thing but from scratch
zzz_str_square_prime_nums = [
    "ZZZ" + str(num**2) + "ZZZ" for num in range(100) if is_prime(num)]


# Read words from /usr/share/dict/words
with open('/usr/share/dict/words', 'r') as f:
    # str.strip() returns the same string but without leading or trailing whitespace
    # words contains every line (stripped) in the file (the file has one word per line).
    english_words = [line.strip() for line in f.readlines()]


short_words = [word for word in english_words if len(word) < 5]
uppercase_short_words = [word.upper() for word in short_words]

# could have done the above in one line
uppercase_short_words = [word.upper()
                         for word in english_words if len(word) < 5]

# self-explanatory
words_that_start_with_a = [word for word in english_words if word[0] == 'a']
words_that_dont_start_with_a = [
    word for word in english_words if word[0] != 'a']

# Sanity check: these two lists are mutually exclusive and if you combine them,
# we should have the same amount of words we started with
assert(len(words_that_start_with_a) +
       len(words_that_dont_start_with_a) == len(english_words))


words_that_start_with_ent = [
    word for word in english_words if word.startswith('ent')]
# another way to do it, using slicing
words_that_start_with_ent = [
    word for word in english_words if word[0:3] == 'ent']

# generalize it into a function


def words_that_start_with_prefix(words, prefix):
    return [word for word in words if word.startswith(prefix)]


assert(words_that_start_with_prefix(
    english_words, 'ent') == words_that_start_with_ent)


some_words = ['tree', 'asdfasdf', 'poopiesoppe',
              'derderder', 'shirt', 'jacket']

fake_words = [word for word in some_words if word not in english_words]
real_words = [word for word in some_words if word in english_words]