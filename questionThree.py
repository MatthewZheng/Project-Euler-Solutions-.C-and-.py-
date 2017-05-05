#! usr/bin/env python
_author_ = "Matthew Zheng"
_purpose_ = "Solution to Project Euler Q3: Largest Prime Factor"

import sys
import math

def main():
    numTest = 600851475143
    #look for the largest multiple
    for i in range (1, numTest):
        if(numTest % i == 0):
            #check if number is prime
            if (prime(i)):
                biggestNum = i

    print("The largest prime is", biggestNum)

def ceilingUp(num):
    #We are not going to use the built in ceiling function on line 24
    #return(math.ceil(num))
    if num-int(num) < 0:
        difference = -(num-int(num))
    else:
        difference = num-int(num)
    if difference < 0.5:
        return(int(num))
    else:
        return(int(num)+1)

def prime(numCheck):
    primeNum = False
    if numCheck <= 2:
        #all number up to and including 2 are prime
        primeNum = True
    else:
        for i in range(2, ceilingUp(math.sqrt(numCheck))):
            if numCheck % i == 0:
                primeNum = False
                break
            else:
                primeNum = True
    return(primeNum)


if __name__ == "__main__":
    main()
