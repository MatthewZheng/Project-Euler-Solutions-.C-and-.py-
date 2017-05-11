/*
*Author: Matthew Zheng
*Purpose: Project Euler Solution Question Ten: Summation of primes
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//Definitions
#define TRUE 1
#define FALSE 0

int main(void){

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
