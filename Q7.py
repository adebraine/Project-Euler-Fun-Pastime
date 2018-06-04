# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:31:07 2018

@author: Adebraine
"""

"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

import numpy as np

n = 10001
def nth_prime_number(n):
    prime_list = [2]
    num = 3
    while len(prime_list) < n:
        for p in prime_list:
            if num % p == 0:
                break
        else:
            prime_list.append(num)
        num += 2

    return prime_list[-1]

result = nth_prime_number(n)
print(result)