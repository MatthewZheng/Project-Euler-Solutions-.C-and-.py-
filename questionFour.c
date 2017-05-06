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
void int2Arr(int intIn, int[], int size);

int main(void){
	/*int startM = 999;
	int startM2 = 999;
	int prod = startM*startM2;
	int size = sizeof(prod) / sizeof(int);
	int prodArr[size];



	for (int i = 0; i < sizeof(myArr)/sizeof(int); i++){
		printf("%d ", myArr[i]);
	}*/

	system("PAUSE");
	return 0;
}

int paliCheck(int someArr[]){
	int check = FALSE;
	if (sizeof(someArr) == 1){
		return TRUE;
	}
	else {
		for (int i = 0; i < ((int) sizeof(someArr) / 2); i++){
			if (someArr[-(i + 1)] == someArr[i]){
				check = TRUE;
			}
			else{
				check = FALSE;
				break;
			}
		}
	}
	return(check);
}

void int2Arr(int inNum, int outArr[], int size){
	while (inNum > 0){
		outArr[size-1] = inNum % 10;
		size--;
		inNum /= 10;
	}
}
