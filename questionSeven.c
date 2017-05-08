/*
*Author: Matthew Zheng
*Purpose: Project Euler Solution Question Seven: 10001st Prime
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//Definitions
#define TRUE 1
#define FALSE 0

//initialize functions
int primeCheckS(int);
int increment(int);

int main(void){
   //Given info
   int counter = 6;
   int currentPrime = 13;

   while(counter < 10001){
      currentPrime += increment(currentPrime);
      counter++;
      printf("%d\n", currentPrime);
   }

   //Print final result
   printf("The current prime is %d with a counter of %d.\n", currentPrime, counter);

   system("PAUSE");
   return 0;
}

//Checks for prime numbers
int primeCheckS(int numCheck){
   int isPrime = FALSE;
   for(int i = 1; i <= ceil(sqrt(numCheck)); i++){
      if(numCheck % i == 0){
         if(i == 1 || i == numCheck){
            isPrime = TRUE;
         } else{
            isPrime = FALSE;
         }
      }
   }
   return(isPrime);
}

//Determines how much to increment by to get to next prime
int increment(int num){
   for(int i = 1; i < num; i++){
      if (primeCheckS(num+i) == TRUE){
         return(i);
      }
   }
}
