#!/usr/bin/env python3
"""This program test different conditional tests"""

"""Testing equality and inequality in numbers"""
var1 = 21
var2 = 22

print('var1 = {}, var2 = {}'.format(var1, var2))
print('Is var1 == var2')
print(var1 == var2)

print("\n")
var2 = 21
print('var1 = {}, var2 = {}'.format(var1, var2))
print("Is var1 == var2")
print(var1 == var2)

"""Testing equality with lower function"""
print("\n")
motorcycle = 'Ducati'
motorcycle.lower() == "ducati"
print("Is my motorcycle still a Ducati?")
print(motorcycle == motorcycle.lower())

print("\n")
motorcycle = 'ducati'
motorcycle.lower() == "ducati"
print("Is my motorcycle still a Ducati?")
print(motorcycle == motorcycle.lower())

"""Testing equality and inequality in strings"""
print("\n")
big_cat = "Tiger"
big_cat2 = "tiger"
print("big_cat = {}, big_cat2 = {}".format(big_cat, big_cat2))
print("Are this big cats the same?")
print(big_cat == big_cat2)

print("\n")
big_cat2 = "Tiger"
print("big_cat = {}, big_cat2 = {}".format(big_cat, big_cat2))
print("Are these two big cats the same?")
print(big_cat == big_cat2)

print("\n")

"""Testing less than or greater than"""
var3 = 50
var4 = 52
print("var3 = {}, var4 = {}".format(var3, var4))
print("Is var3 greater than var4?")
print(var3 > var4)

print("\n")
print("var3 = {}, var4 = {}".format(var3, var4))
print("Is var3 less than var4?")
print(var3 < var4)

print("\n")

"""Test the 'or' keyword"""
age1 = 29
age2 = 30
print("age1 = {}, age2 = {}".format(age1, age2))
print("Are the ages age1 and ag2 greater than or equal to other numbers?")
print(age1 >= 28 or age2 >= 32)

print("\n")

print("age1 = {}, age2 = {}".format(age1, age2))
print("Are the ages age1 and ag2 less than or equal to other numbers?")
print(age1 <= 28 or age2 <= 29)

print("\n")

"""Testing the 'and' keyword"""
age3 = 50
age4 = 51

print("age3 = {}, age4 = {}".format(age3, age4))
print("Are the ages age3 and age4 less than and equal to other numbers?")
print(age3 <= 50 and age4 <= 45)

print("\n")
print("age3 = {}, age4 = {}".format(age3, age4))
print("Are the ages age3 and age4 less than and equal to other numbers?")
print(age3 <= 51 and age4 <= 55)

print("\n")

"""Test whether an item is in a list"""
cars = ['hilux', 'd-max', 'corolla', 'vitz']
car = 'hilux'
if car not in cars:
    print(car)
else:
    print(cars)

print("\n")

"""Tests is an item is'nt in a list"""

cars = ['amg', 'g-wagon', 'compressor', 'm3']
car = 'compressor'
if car in cars:
    print(cars)
else:
    print(car)