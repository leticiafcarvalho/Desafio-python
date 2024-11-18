#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    valorInicial = 3
    tempoInicio = 1
    
    while t > tempoInicio + valorInicial - 1:
        tempoInicio += valorInicial
        valorInicial *= 2
    
    return valorInicial - (t - tempoInicio)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
