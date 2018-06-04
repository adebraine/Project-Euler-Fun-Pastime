# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:36:16 2018

@author: Adebraine
"""

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. 

Find the sum of all the primes below two million.
"""

n = 2000000

def is_prime(n):
    if n % 2 == 0: return False
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True

def all_prime(n):
    result = 2
    if n < result:
        return []
    if n == result:
        return [result]
    for i in range(result+1,n+1):
        if is_prime(i):
            result = result + i
    
    return result

print(all_prime(n))
        