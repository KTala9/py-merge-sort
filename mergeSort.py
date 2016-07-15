#!/usr/bin/env python3
"""
A module which implements the MergeSort algorithm.
"""

# conda execute
# env:
#  - python >=3
#  - numpy

import sys
import re # regular expressions
from numpy import * # scientific math library

def parseInput(input):
    """
    Converts an input string of integers into an array of integers.
    """
    return [int(num) for num in input.split(',')]


def mergeSort(a):
    if len(a) == 1:
        return a;
    else:
        nArrayMid = int(len(a) / 2)
        a1 = a[0:nArrayMid]
        a2 = a[nArrayMid: len(a)]
        return merge(mergeSort(a1), mergeSort(a2));


def merge(a1, a2):
    nTotalLength = len(a1) + len(a2)
    aMerged = []
    i = 0
    j = 0

    while len(aMerged) < nTotalLength:
        if i == len(a1):
            aMerged.append(a2[j])
            j = j + 1
        elif j == len(a2):
            aMerged.append(a1[i])
            i = i + 1
        elif a1[i] <= a2[j]:
            aMerged.append(a1[i])
            i = i + 1
        else:
            aMerged.append(a2[j])
            j = j + 1

    return aMerged


def main(sInput):
    aInput = parseInput(sInput)
    result = mergeSort(aInput);
    print(result)

if __name__ == '__main__':
    main(sys.argv[1]) # The 0th argument is the module filename