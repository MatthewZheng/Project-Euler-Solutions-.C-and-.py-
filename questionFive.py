#! usr/bin/env python
_author_ = "Matthew Zheng"
_purpose_ = "Project Euler Question 5: Smallest Multiple"

import sys
import math

#-------------------
# divisible by 20 = 2 and 10
# divisible by 19 prime
# divisible by 18 = 9
# divisible by 17 prime
# divisible by 16 = 4
# divisible by 15 = 3 and 5
# divisible by 14 = 7
# divisible by 13 prime
# divisible by 12 = 6 and 8
# divisible by 11 prime
# every other case < 10 already accounted for
#-------------------

def main():
    #minimum case is 20
    numCheck = 20
    satisfies = False

    while(satisfies == False):
        for i in range (11, 20+1):
            if numCheck % i != 0:
                #has to be a multiple of 20
                numCheck += 20
                print(numCheck)
                break
            if i == 20 and numCheck % 20 == 0:
                satisfies = True

    print(numCheck)

if __name__ == "__main__":
    main()
