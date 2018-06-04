# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 20:37:08 2018

@author: Adebraine
"""

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


import numpy as np

div = [i for i in range(1,21)]
temp = []

count = 0
run = True
while run:
    count += max(div)
    for i in div:
        temp.append(count % i)
    
    if np.sum(temp) == 0:
        result = count
        run = False
        
    temp = []
    

print(result)