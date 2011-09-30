#!/usr/bin/env python

#PROBLEM 1 (05 October 2001):
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we
#get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def method1():
    ans = 0
    for n in range(3, 1000):
        if n % 3 == 0 or n % 5 == 0:
            ans += n
    print("Method 1: ", ans)

def method2():
    ans = sum(n for n in range(3, 1000) if (n % 3 == 0 or n % 5 == 0))
    print("Method 2: ", ans)

def method3():
    ans = sum(set(list(range(3, 1000, 3)) + list(range(5, 1000, 5))))
    print("Method 3: ", ans)

def method4():
    ans = sum(range(3, 1000, 3)) + sum(range(5, 1000, 5)) - sum(range(15, 1000, 15))
    print("Method 4: ", ans)

if __name__ == '__main__':
    method1()
    method2()
    method3()
    method4()