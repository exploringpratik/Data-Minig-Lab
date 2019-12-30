# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:57:14 2019

@author: explo
"""
#string1 = "Peshal"
#print(string1.replace("Peshal","Oli"))
#animals = ["monkey", "giraffe", "shark","animal1","animal2"]
#animals[1] = "tiger"
#animals.append("Leopard")
#print("tiger" in animals)
#print(";".join(animals))
#print(animals)

molecules = {"hair":"keratin","DNA":"nucleotides","protein":"amino acids"}
print(molecules)

print(molecules["DNA"])

molecules["ribosomes"] = "RNA"
print(molecules)

molecules["RNA"] = "nucleotides"

print(molecules)

molecules["ribosomes"] = "rRNA"
print(molecules.keys())
print(molecules.values())

keys_values = list(zip(molecules.keys(),molecules.values()))
print(keys_values)