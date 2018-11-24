#!/bin/python3

def diagonalDifference(arr):
    leftDiag=0
    rightDiag=0
    x=0
    y=0

    lenY=len(arr[x])

    for x in range (0, len(arr)):
        for y in range (0, lenY):
            if x==y:
                leftDiag+=arr[x][y]
                print(leftDiag)
            if x==lenY-1-y:
                rightDiag+=arr[x][y]
                print(rightDiag)

    return abs(leftDiag-rightDiag)
