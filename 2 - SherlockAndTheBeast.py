#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'decentNumber' function below.
# The function accepts INTEGER n as parameter.
def decentNumber(n):
    fives = n - (n % 3)
    
    while fives >= 0:
        if (n - fives) % 5 == 0:
            print('5' * fives + '3' * (n - fives))
            return
        fives -= 3
    
    print(-1)

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        decentNumber(n)
