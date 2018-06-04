# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 19:14:43 2018

@author: Adebraine
"""

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


import numpy as np

x = 600851475143
i = 2
result = []

run = True
while run:
    i += 1
    if x % i == 0:
        x = x / i
        result.append(i)
    
    if x <= 1:
        run = False
        

print(np.max(result))
