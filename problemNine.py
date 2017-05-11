#! usr/bin/env python
_author_="Matthew Zheng"
_purpose_ = "Project Euler Solution Question Nine: Special pythagoran triplet"

import sys
import math

def main():
    defaultCheck()
    secondaryCheck()

def checkOtherCases(currentA, currentB, currentC):
    for a in range(1, currentC):
        for b in range (1, currentC):
            if(isSquarable(a+b)):
                currentA = a
                currentB = b

def defaultCheck():
    #Starting values
    a=3
    b=4
    c=5
    counter = 1

    #find next pythagoran triplet based on pattern of keeping 3:4:5 ratio
    while (a+b+c <= 1000):
        a=3
        b=4
        c=5
        a *= counter
        b *= counter
        c *= counter
        print("Default counter:", a, b, c)
        if(a+b+c == 1000):
            print("Gotchu.")
            break
        counter += 1

    print("The product is:", a*b*c)

def secondaryCheck():
    #Starting values
    a=3
    b=4
    c=5
    counter = 1

    #find next pythagoran triplet based on pattern of keeping 5:12:13 ratio
    while (a+b+c <= 1000):
        a=5
        b=12
        c=13
        a *= counter
        b *= counter
        c *= counter
        print("Secondary counter:", a, b, c)
        if(a+b+c == 1000):
            print("Gotchu.")
            break
        counter += 1
    print("The product is:", a*b*c)


#Returns true if number is square root
def isSquarable(num):
    if float.is_integer(math.sqrt(num)):
        return(math.sqrt(num))
    else:
        return(False)

if __name__ == "__main__":
    main()
