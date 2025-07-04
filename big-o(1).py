import time 
import random
import os, sys, argparse


# no matter how many elements are there, we do the same number of operations 

# one simple example is a function that fetches the first element of any non-empty array

def simplefunc(input_array):
    return input_array[0]

print(simplefunc([random.choice(range(100)) for _ in range(10)]))

# no matter the size of the array to simplefunc(), the program runs only once, returning the very first element of a non-empty array