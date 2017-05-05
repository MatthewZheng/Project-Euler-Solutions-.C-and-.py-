/*
 *Author: Matthew Zheng
 *Purpose: Solution to Project Euler Q4: Largest Palindrome
 */

 #include <stdio.h>
 #include <stdlib.h>

 #define TRUE 1
 #define FALSE 0

 /*Initialize functions*/
 int paliCheck(int[]);

 int main(void){

    system("PAUSE");
    return 0;
}

int paliCheck(int someArr[]){
   int check = FALSE;
   if(sizeof(someArr) == 1){
      return TRUE;
   } else {
      for(int i = 0; i < ((int) sizeof(someArr)/2); i++){
         if(someArr[-(i+1)] == someArr[i]){
            check = TRUE;
         } else{
            check = FALSE;
            break;
         }
      }
   }
   return(check);
}
