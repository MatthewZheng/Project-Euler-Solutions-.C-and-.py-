#! usr/bin/env python
_author_ = "Matthew Zheng"
_purpose_ = "Python solution Euler Q2: Even fibonacci numbers"

import sys

def main():
    #printFib(33)
    printFibSum(32)

def printFib(length):
    fibNum1 = 1
    fibNum2 = 2
    if length <= 0:
        print("There's nothing to show!")
    elif length >= 1:
        print(1)
    for num in range(1, length):
        if num == 1:
            print(2)
        else:
            sumNum = fibNum1+fibNum2
            print(sumNum)
            if sumNum > 4000000:
                print("This is over 4 mill")
            elif sumNum == 4000000:
                print("This is 4 mill")
            else:
                print("This is under 4 mill")
            fibNum1 = fibNum2
            fibNum2 = sumNum

def printFibSum(length):
    fibNum1 = 1
    fibNum2 = 2
    sum = 0
    #Cases for when length is smaller than or equal to 1 removed because either it does not contribute to the sum or is 1, an odd number
    for num in range(1, length):
        if num == 1:
            #first even
            sum += 2
        else:
            sumNum = fibNum1+fibNum2
            if sumNum % 2 == 0:
                sum += sumNum
            fibNum1 = fibNum2
            fibNum2 = sumNum
    print(sum)

if __name__ == '__main__':
    main()
