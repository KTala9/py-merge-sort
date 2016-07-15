#!/usr/bin/env python3
"""
A module which implements the MergeSort algorithm.
"""

import sys


def parseInput(input):
    """
    Converts an input string of integers into an array of integers.
    """
    return [int(num) for num in input.split(',')]


def mergeSort(a):
    """
    Sorts and array of numbers into ascending order.
    """

    if len(a) == 1:
        return a;
    else:
        nArrayMid = int(len(a) / 2)
        a1 = a[0:nArrayMid]
        a2 = a[nArrayMid: len(a)]
        return merge(mergeSort(a1), mergeSort(a2));


def merge(a1, a2):
    """
    Merges two arrays of numbers (both of which are expected to be pre-sorted into ascending order),
    into a new array, sorted in ascending order.
    """

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