#!/bin/python3

"""
Given a range of numbered days[i...j],  and a number k , determine the number of days in the range that are beautiful. 
Beautiful numbers are defined as numbers where |i -rev(i)|  is evenly divisible by k .
If a day's value is a beautiful number, it is a beautiful day. Return the number of beautiful days in the range
"""

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # Write your code here
    count = 0
    def rev(num):
        rev = 0
        while (num>0):
            n = num % 10
            rev = rev*10 + n
            num = num // 10
        return rev
        
        
    for num in range(i,j+1):
        absDiff = abs(num- rev(num))
        if(absDiff%k==0):
            count +=1
    return count
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
