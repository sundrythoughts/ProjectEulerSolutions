#!/bin/bash/env python

#2520 is the smallest number that can be divided by each of the numbers
#from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the
#numbers from 1 to 20?

def lcm(a, b):
    (mn, mx) = max(a, b), (a * b)
    for i in range(mn, mx + 1):
        if i % a == 0 and i % b == 0:
            return i

def genLcmList(lst):
    lst_outer = lst
    lst_inner = lst
    lcm_lst = []
    for i in lst:
        for j in lst_inner:
            lcm_lst.append(lcm(i, j))
        lst_inner = lst_inner[1:]
    lcm_lst.sort()
    lcm_lst = list(set(lcm_lst))
    return lcm_lst

def method1():
    lcm_lst = list(range(1, 20 + 1))
    while len(lcm_lst) > 1:
        lcm_lst = genLcmList(list(range(1, 20 + 1)))
    print("Method 1: ", lcm_lst)

if (__name__ == '__main__'):
    method1()
