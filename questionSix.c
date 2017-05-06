/*
*Author: Matthew Zheng
*Purpose: Solution to Project Euler Q6: Sum square difference
*/

#include <stdio.h>
#include <stdlib.h>

int main(void){
   int squareS = 0;
   int sqNumS = 0;

   for (int i = 1; i < 101; i++){
      squareS += i;
      sqNumS += i*i;
   }
   squareS = squareS * squareS;

   printf("The difference is %d\n", (squareS - sqNumS));

   system("PAUSE");
   return 0;
}
