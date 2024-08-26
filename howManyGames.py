"""
Function Description

Complete the howManyGames function in the editor below.

howManyGames has the following parameters:

int p: the price of the first game
int d: the discount from the previous game price
int m: the minimum cost of a game
int s: the starting budget
https://www.hackerrank.com/challenges/halloween-sale/problem?isFullScreen=true
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    sumPrice = 0
    count = 0
    while(sumPrice <= s):
        
        if p <= m:
            p = m
        sumPrice += p
        p = p-d
        count += 1
    return count-1
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
