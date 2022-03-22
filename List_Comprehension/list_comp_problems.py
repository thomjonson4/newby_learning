##############
# PROBLEMS
##
# Implement each problem
# A) without comprehensions
# B) with comprehensions
#
# !! You can write helper functions if you think they will be helpful !!
#
# When using comprehensions, you might be able to do some of these in one line!
# It's not necessary (and not always good to do that), so don't focus on that.
##############

# 1)    Write a function that returns the first N odd numbers, starting from 1.
def first_n_odd_numbers_A(N):
    nums = []
    while len(nums) < N:
        for num in range (N * 2):
            if num % 2 == 1:
                nums.append(num)
    print(nums)




def first_n_odd_numbers_B(N) -> list[int]:
    return [num for num in range (N * 2) if num % 2 == 1]


# assert(first_n_odd_numbers_A(10) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
# assert(first_n_odd_numbers_B(10) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])

# # 2)   Write a function, that when given a list of words, returns only a list of only those
# # words that are of odd length.


# def odd_length_words_A(words):
#     pass


# def odd_length_words_B(words):
#     pass


# # We could compare the lists directly (instead of their length), but then we'd need
# # the words to be in the exact same order too.
# # To keep things simple we'll just comapre the length, even though it's not as good of a test
# assert(len(odd_length_words_A(english_words)) ==
#        len(odd_length_words_B(english_words)))
# odd_length_words = odd_length_words_A(english_words)

# assert('those' in odd_length_words)
# assert('smith' in odd_length_words)
# assert('abate' in odd_length_words)
# assert('ventriloque' in odd_length_words)
# assert('unsuitability' in odd_length_words)
# assert('undisplayed' in odd_length_words)
# assert('polyhedroid' in odd_length_words)


# # 3)   Write a function that returns a list of the sums of the
# # digits of the squares of all the prime numbers below N (first prime number is 2).

# # example:
# # prime numbers below 12               -> [2,  3,  5,  7,  11]
# # their squares                        -> [4,  9, 25, 49, 121]
# # sum of digits                        -> [4,  9,  7, 13,   4]

# def sum_digits_squares_primes_A(N):
#     pass


# def sum_digits_squares_primes_B(N):
#     pass


# assert(sum_digits_squares_primes_A(50) == sum_digits_squares_primes_B(50))
# assert(sum_digits_squares_primes_A(50)[:10] == [
#        4, 9, 7, 13, 4, 16, 19, 10, 16, 13])

# # 4)    Write a function that returns an ASCII (string) representation of a picket fence.
# # The function takes in two parameters: section_length, num_pickets
# # The section length is the distance between pickets, and num_pickets is
# # the amount of pickets in the fence.
# # Example:
# # picket_fence(3,4) returns "|---|---|---|"
# # picket_fence(2,4) returns "|--|--|--|"
# # picket_fence(2,2) returns "|--|"
# # picket_fence(2,1) returns "|"
# # picket_fence(9,1) returns "|"
# # picket_fence(0,3) returns "|||"
# # picket_fence(0,0) returns ""

# # Use the '|' character for pickets, and the '-' character for the sections


# def picket_fence_A(section_length, num_pickets):
#     pass


# def picket_fence_B(section_length, num_pickets):
#     pass


# # 5)     Write a function, that given a list of locations,
# # returns only those locations where the temperature degrees in Celcius in that location,
# # truncated to an integer, is even.

# # Example: locations = ["new york city", "dubai", "stockholm", "sydney"]
# # Let's say the temperatures were 6.2, 25.3, 12.6, and 17.8, respectively.
# # The result would be ["new york city", "stockholm"].

# # Also, some locations might not return a populated response from the weather api. 
# # You should handle this case.


# def get_locations_where_temperature_is_even(locations):
#     pass


# test_locations = [
#     'new york city','dubai','tokyo','stockholm','sydney','nurburg',
#     'st.petersburg','kansas city','daytona','mexico city', 'tijuana', 'cozumel',
#     'san francisco', 'mountain view','vilnius','kyoto', 'barcelona','madrid',
#     'liverpool','london', 'nottingham','outer fucking space man'
#     ]