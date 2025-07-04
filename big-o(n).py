import time 
import random
import os, sys, argparse

# linear time growth means that each item in the array is visited once in the worst case scenario

# one example to demonstrate that is finding the largest element in an unsorted array 

choices = range(1000)

array_size = 100

unsorted_array = [random.choice(choices) for _ in range(array_size)]

largest = unsorted_array[0]

t0  = time.time()
for i in unsorted_array:
    if i > largest:
        largest = i

exectime = time.time()-t0

print(unsorted_array)
print("\n")
print("Found largest element %d in %0.10f seconds" %(largest, exectime))

# output : 

# [649, 684, 581, 557, 79, 747, 773, 879, 699, 491, 857, 582, 630, 500, 528, 929, 43, 113, 786, 506, 214, 96, 473, 247, 836, 109, 822, 685, 811, 796, 956, 311, 241, 293, 703, 904, 971, 206, 539, 221, 707, 147, 113, 126, 95, 113, 739, 345, 398, 895, 242, 774, 44, 559, 396, 402, 735, 858, 47, 714, 629, 707, 658, 107, 95, 266, 563, 540, 507, 28, 807, 493, 641, 509, 51, 634, 806, 21, 744, 300, 737, 965, 211, 17, 957, 88, 124, 899, 180, 297, 983, 485, 978, 704, 296, 533, 463, 688, 534, 929]

# Found largest element 983 in 0.0000150204 seconds