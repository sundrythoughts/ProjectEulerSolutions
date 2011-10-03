#!/bin/bash/env python

#SOLVED

#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def method1():
    (sum_of_sqrs, sqr_of_sums) = 0, 0
    for i in range(1, 100 + 1):
        sum_of_sqrs += (i**2)
        sqr_of_sums += i
    sqr_of_sums = sqr_of_sums**2

    print("Method 1: ", sqr_of_sums - sum_of_sqrs)

if __name__ == '__main__':
    method1()