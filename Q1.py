# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 19:12:16 2018

@author: Adebraine
"""

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import numpy as np

result = []

for i in range(0,1000):
    if i % 3 == 0 or i % 5 == 0:
        result.append(i)

print(np.sum(result))