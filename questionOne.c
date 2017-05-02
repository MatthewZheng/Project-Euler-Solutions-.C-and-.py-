/*
 *Project Euler multiples of 3 and 5
 *Author: Matthew Zheng
 */

#include <stdlib.h>
#include <stdio.h>

int main(void){
	int mySum = 0;

	for (int i = 0; i < 1000; i++){
		if (i % 5 == 0 || i % 3 == 0){
			mySum += i;
			printf("%d\n", i);
		}
	}

	printf("The sum is %d\n", mySum);

	system("PAUSE");
	return 0;

}
