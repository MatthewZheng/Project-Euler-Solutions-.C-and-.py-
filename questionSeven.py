#! usr/bin/env python
_author_ = "Matthew Zheng"
_purpose_= "Project Euler Solution Question Seven: 10001st Prime"

import sys
import math

def main():
    #given info
    counter = 6
    currentPrime = 13

    #count up by primes
    while counter < 10001:
        currentPrime += increment(currentPrime)
        counter += 1
        print(currentPrime)
        print(counter)

    #prints final result
    print("The current prime is", currentPrime)
    print("The counter is", counter)

#Checks for prime numbers
def primeCheckS(numCheck):
    isPrime = False
    for i in range (1, math.ceil(math.sqrt(numCheck))+1):
        if numCheck % i == 0:
            if i == 1 or i == numCheck:
                isPrime = True
            else:
                isPrime = False
    return isPrime

#determines how much to increment value by to get to next prime
def increment(num):
    for i in range (1, num):
        if primeCheckS(num + i) == True:
            return i


if __name__ == "__main__":
    main()
