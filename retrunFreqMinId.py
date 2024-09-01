#!/bin/python3
"""
Given an array of bird sightings where 
every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
"""
import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    digitFreq = {}
    for bird in arr:
        if bird in digitFreq:
            digitFreq[bird] += 1
        else:
            digitFreq[bird] = 1
    
    maxfreq = max(digitFreq.values())
    
    mostFreqBird = []
    for bird, freq in digitFreq.items():
        if freq == maxfreq:
            mostFreqBird.append(bird)
    return min(mostFreqBird)
            
    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
