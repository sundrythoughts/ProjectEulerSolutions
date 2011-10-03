#!/bin/bash/env python

#SOLVED

#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?

def method1():
    sm = sum(int(i) for i in str(2**1000))
    print("Method 1: ", sm)

if __name__ == '__main__':
    method1()