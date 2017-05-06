#!usr/bin/env python
_author_ = "Matthew Zheng"
_purpose_ = "Solution to Project Euler Q6: Sum square difference."

import sys
import math

def main():
    #square of sum
    squareS = 0
    #sum of the squares
    sqNumS = 0
    for i in range (1,100+1):
        squareS += i
        sqNumS += math.pow(i, 2)
    squareS = math.pow(squareS, 2)

    print("The difference is", squareS - sqNumS)


if __name__ == "__main__":
    main()
