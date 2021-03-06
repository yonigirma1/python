# coding=utf-8

import random

# R-1.1
# Write a short Python function, is multiple(n, m), that takes two integer values and returns
# True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.

def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False

# R-1.2
# Write a short Python function, is even(k), that takes an integer value and returns True if k is even,
# and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.

def is_even(n):
    if n & 1:
        return False
    else:
        return True

# R-1.3
#Write a short Python function, minmax(data), that takes a sequence of one or more numbers,
# and returns the smallest and largest numbers, in the form of a tuple of length two.
# Do not use the built-in functions min or max in implementing your solution.

def minmax(data):
    smallest = data[0]
    largest = data[0]
    for item in data:
        if item < smallest:
            smallest = item
        elif item > largest:
            largest = item
        return smallest, largest

# R-1.4
# Write a short Python function that takes a positive integer n and returns the sum of the squares
#  of all the positive integers smaller than n.

def sum_of_squares(n):
    n -= 1
    total = 0
    while n > 0:
        total += n * n
        n -= 1
    return total

# R-1.5
# give a single command that computes the sum from exercise r-1.4, relying on python's comprehension syntax and built in sum function

def sum_of_squares2(n):
    return sum([k * k for k in range(0,n)])

# R-1.6
#Write a short Python function that takes a positive integer n and returns the sum of the squares
# of all the odd positive integers smaller than n.

def sum_of_odd_squares(n):
    n -= 1
    total = 0
    while n > 0:
        if n % 2 != 0:
            total += n * n
            n -= 1
    return total

# R-1.7

# give a single command that computes the sum from r-1.6, relying on python's comprehension syntax and built in sum function

def sum_of_odd_squares2(n):
    return sum([k * k for k in range (0,n) if k % 2 != 0])

# R-1.8
# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used
# for index -n <= k < 0, what is the equivalent index j >= 0 such that s[j]
# references the same element?

s = "string"
n = len(s)

for k in range(-n, 0):
    print (s[k])

for j in range(-n, 0):
    print (s[j + n])

# R-1.9
# What parameters should be sent to the range constructor, to produce a range with values 50, 60, 70, 80?

print(range(50,90, 10))

# R-1.10
# what parameters should be sent to the range constructor to produce a range with values
# 8, 6, 4, 2, 0, -2, -4, -6, -8

print (range(8,-10,-2))

# R-1.11
# Demonstrate how to use Python's list comprehension syntax to produce the list
# [1, 2, 4, 8, 16, 32, 64, 128, 256].

print (pow(2, k) for k in range (0, 9, 1))

# R-1.12

# Python's random module includes a function choice(data) that returns a random element
# from a non-empty sequence. The random module in- cludes a more basic function randrange,
# with parameterization similar to the built-in range function, that return a random choice
# from the given range. Using only the randrange function, implement your own version of the choice function.

def my_choice(data):
    return data[random.randrange(1, len(Data))]

# C-1.13

# Write a pseudo-code description of a function that reverses a list of n integers,
# so that the numbers are listed in the opposite order than they were before, and compare
# this method to an equivalent Python function for doing the same thing.

list = [1,2,3,4,5,6,7,8,9,10]
print(list[-1])

# C-1.14
# Write a short Python function that takes a sequence of integer values and determines
# if there is a distinct pair of numbers in the sequence whose product is odd.

def odd_product(data):
    count = 0
    for k in range(0, len(data) - 1):
        if k % 2 != 0:
            count += 1
        return True if count >= 2 else False


# C-1.15
# Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

def are_identical(data):
    count = 0
    for k in data:
        for k in range(0, len(data) -1):
            if k == j:
                count += 1
                if count >= 2:
                    return False
    return True

# C-1.18
# Demo list comprehension to create the following
# list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

print ([k * (k-1) for k in range(1,11)])

# C-1.19
# Demonstrate how to use python's
# list comprehension syntax to produce
# the list [ a , b , c ,..., z ],without typing  characters literally.

print ([chr(k) for k in range(97,123)])

# C-1.23
# Give an example of a Python code fragment that attempts
# to write an ele- ment to a list based on an index that may be out of bounds.
# If that index is out of bounds, the program should
# catch the exception that results, and print the following error message:
# “Don’t try buffer overflow attacks in Python!”

listoch = [1,2,3,4,5]

try:
    listoch[5]
except IndexError:
    print("bad index")

# C-1.24
# Write a short Python function that counts the number of vowels in a given
# character string.

sentence = "The Quick brown Fox jumps over the lazy dog."
count = 0

for c in sentence:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        count += 1
print count





