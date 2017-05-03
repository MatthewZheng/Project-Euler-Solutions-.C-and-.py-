#!/usr/bin/env python
_author_ = "Matthew Zheng"
_purpose_ = "Euler question 1, multiples of 3 and 5"

import sys

def main():
    mySum = 0
    for num in range (0, 1000):
        if num % 5 == 0 or num % 3 == 0:
            mySum += num
            print(num)

    #print final result
    print("The sum is", mySum)

if __name__ == "__main__":
    main()
