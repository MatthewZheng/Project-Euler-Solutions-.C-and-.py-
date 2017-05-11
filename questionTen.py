#! usr/bin/env python
_author_ = "Matthew Zheng"
_purpose_ = "Solution to Project Euler Question 10: Summation of Primes"

import sys
import math

def main():
    #counter for sum
    sumOfPrimes = 0
    currPrime = 2
    while currPrime < 2000000:
        print(currPrime)
        sumOfPrimes += currPrime
        currPrime += increment(currPrime)

    print("The sum of primes is", sumOfPrimes)



#determines how much to increment value by to get to next prime
def increment(num):
    for i in range (1, num):
        if primeCheckS(num + i) == True:
            return i

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

if __name__ == "__main__":
    main()
