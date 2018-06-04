# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:16:55 2018

@author: Adebraine
"""

"""
A Pythagorean triplet is a set of three natural numbers, a<b<c, for which

a^2+b^2=c^2

For example, 3^2+4^2=9+16=25=5^2.

There exists exactly one Pythagorean triplet for which a+b+c=1000.
Find the product abc.

"""

n = 1000
def trip(n):
    for i in range(1,n+1):
        for j in range(i,n):
            k = n - i - j
            if i**2 + j**2 == k**2:
                r1 = i
                r2 = j
                r3 = k
                return r1,r2,r3

r1,r2,r3 = trip(n)
print(r1,r2,r3)
print(r1*r2*r3)
