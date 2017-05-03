/*
*Author: Matthew Zheng
*Purpose: Solution to Project Euler Q3: Largest Prime Factor
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define TRUE 1
#define FALSE 0

unsigned long long int ceilingUp(float);
unsigned long long int prime(unsigned long long int);

int main(void){
	unsigned long long int numTest = 600851475143;
	unsigned long long int biggest;
	for (int i = 1; i <= numTest; i++){
		/*Look for the largest multiple*/
		if (numTest % i == 0){
			//printf("%llu ", i);
			/*Check if prime by comparing it to the ceiling value of root*/
			if (prime(i)){
				biggest = i;
			}
			else{
				//puts("There is no prime.");
			}
		}
	}

	printf("The largest prime is: %llu\n", biggest);

	system("PAUSE");
	return 0;
}

unsigned long long int ceilingUp(float num){
	float difference;
	/*Get absolute value difference*/
	if ((((int)num) - num) < 0){
		difference = -(((int)num) - num);
	}
	else{
		difference = ((int)num) - num;
	}
	/*Comparison test to see if round up or down*/
	if (difference < 0.5){
		return(((int)num));
	}
	else if (difference >= 0.5){
		return(((int)num) + 1);
	}
}

unsigned long long int prime(unsigned long long int numCheck){
	/*Declare new variable to act as a switch*/
	int primeNum = FALSE;

	if (numCheck <= 2){
		/*Numbers 2 or under are prime*/
		primeNum = TRUE;
	}
	else{
		for (int i = 2; i < ceilingUp(sqrt(numCheck)); i++){
			if (numCheck % i == 0){
				primeNum = FALSE;
				break;
			}
			else {
				primeNum = TRUE;
			}
		}
	}
	return(primeNum);
}
