#!/bin/bash/env python

#A palindromic number reads the same both ways. The largest palindrome made from
#the product of two 2-digit numbers is 9009 = 91  99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def method1():
    mx = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            k = i * j
            k_str = str(k)
            if k_str == k_str[::-1]:
                mx = max(mx, k)
    print("Method 1: ", mx)

if (__name__ == '__main__'):
    method1()
