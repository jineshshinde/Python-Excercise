Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and 
last elements of the given list.

import random
def slice(arr):
    return arr[:1] + arr[-1:] if len(arr) > 1 else arr

a = [random.randint(1,100) for x in range(10)]
slice(a)
