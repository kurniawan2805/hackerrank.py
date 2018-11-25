#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hh12=int(s[0:2])
    dy12=s[-2:len(s)]
    if dy12=='PM':
        hh12+=12
    hh12s=str(hh12)
    return hh12s + s[2:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
