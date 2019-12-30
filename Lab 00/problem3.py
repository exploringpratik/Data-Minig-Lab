# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:43:50 2019

@author: explo
"""

animalsInZoo = {"lion":3,"tiger":2,"crocodile":5}

print(animalsInZoo)
print(sum(animalsInZoo.values()))
animalsInZoo["monkey"] = 5
print(animalsInZoo)
print(animalsInZoo.values())
print(animalsInZoo.keys())
animalsInZoo["monkey"] = 8
animalsInZoo.pop("lion")
animalsInZoo.pop("crocodile")
print(animalsInZoo)