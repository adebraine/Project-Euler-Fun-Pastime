# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 19:46:16 2018

@author: Adebraine
"""

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


import numpy as np
result = []
run = True
x = 999
xold = x


vt = [i for i in range(x,1,-1)]

while run:
    v = vt[0:10]
    for i in v:
        for j in v:
            r = i*j
            rstr = str(r)
            l = len(rstr)
            rrev = ''
    
            while l > 0:
                l -= 1
                rrev = rrev + str(rstr[l])
            
            if rrev == rstr:
                result.append(int(rstr))
    
    if len(result) >= 1:
        run = False
    else:
        for i in range(0,10):
            vt.remove(vt[0])


print(np.max(result))
print(len(result))