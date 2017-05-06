/*
 *Author: Matthew Zheng
 *Purpose: Solution to Project Euler Question 5: Smalles multiple
 */

#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0

int main(void){

   //------------------
   // divisible by 20 = 2 and 10
   // divisible by 19 prime
   // divisible by 18 = 9
   // divisible by 17 prime
   // divisible by 16 = 4
   // divisible by 15 = 3 and 5
   // divisible by 14 = 7
   // divisible by 13 prime
   // divisible by 12 = 6 and 8
   // divisible by 11 prime
   //------------------

   /*Minimum case is 20*/
   int numCheck = 20;
   int satisfies = FALSE;

   while(satisfies == FALSE){
      for(int i = 11; i < 20+1; i++){
         if(numCheck % i != 0){
            numCheck += 20;
            printf("%d\n", numCheck);
            break;
         } if (i == 20 && numCheck % 20 == 0){
            satisfies = TRUE;
         }
      }
   }

   printf("The number is %d.\n", numCheck);


   system("PAUSE");
   return 0;
}
