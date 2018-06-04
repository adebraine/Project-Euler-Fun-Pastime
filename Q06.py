# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 19:06:36 2018

@author: Adebraine
"""

"""


The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

alist = [i for i in range(1,101)]
r1 = 0
for i in alist:
    r1 += i*i

v2 = sum(alist)
r2 = v2*v2

print(r2-r1)
