# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 15:10:53 2019

@author: explo
"""

def findPrimeNumber(a):
    for i in range (2,a):
        print(i)
        x = a%i
        print (x)
        if x!=0:
            prime = 0
        else:
            prime = 1
   # print(prime)
            
            
        
a = int(input("Enter number"))

findPrimeNumber(a)

