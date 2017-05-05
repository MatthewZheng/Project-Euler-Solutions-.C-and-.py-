#! usr/bin/env python
_author_ = "Matthew Zheng"
_purpose_ = "Solution to Project Euler Q4: Largest Palindrome"

import sys
import math

def main():
    #Largest value of 3digit (3d) x 3d is 999x999
    startM = 999
    startM2 = 999
    #Empty array for unknown length of all the palindromes possible
    paliArr = []

    #An array of intgers (of a product)
    prodArr = [int(i) for i in str(startM*startM2)]

    #Loop through all possible values computed by a 3dx3d
    for j in range (999, 1, -1):
        startM = j
        startM2 = j
        while(startM2 >= 1):
            print(prodArr)
            startM2 -= 1
            prodArr = [int(i) for i in str(startM*startM2)]
            if paliCheck(prodArr) == True:
                #The below were used for checking purposes
                # print(startM)
                # print(startM2)
                # print(prodArr)

                #Add value of prodArr to array of palindromes
                paliArr.append(startM*startM2)

    #For testing purposes
    #print(paliArr)

    #Print the largest value
    print(max(paliArr))



def paliCheck(someArr):
    check = False
    if len(someArr) == 1:
        return True
    #Compare index 0 with index -1 and so forth
    for i in range(0, int(len(someArr)/2)):
        if someArr[-(i+1)] == someArr[i]:
            check = True
        else:
            check = False
            #Any false cases immediately != palindrome
            break
    return(check)


if __name__ == "__main__":
    main()
