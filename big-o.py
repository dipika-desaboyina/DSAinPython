import time
import os,sys,argparse

nemo = ["nemo"]
everyone = ["dory","bruce","marlin","ray","gill","nigel","squirt","darla","hank","nemo"]
lotsanemos = ["nemo" for _ in range(100)]

def findNemo(ocean: list):
    t0 = time.time()
    for i in range(0,len(ocean)):
        if ocean[i]=="nemo":
            exectime = time.time() - t0
            print("Found Nemo in %0.10f seconds!" % exectime)

findNemo(nemo) # Found Nemo in 0.0000023842 seconds!
findNemo(everyone) # Found Nemo in 0.0000038147 seconds!
findNemo(lotsanemos) # Found Nemo in 0.0007047653 seconds!

# execution time increases as size of input increases
# big o is the notation that plots input size against number of operations needed

# here the growth is linear, which means the big O is O(n)