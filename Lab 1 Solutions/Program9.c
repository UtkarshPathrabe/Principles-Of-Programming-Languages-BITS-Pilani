#include <stdio.h>

void swap(int *m, int *n){
	int temp = *m;
	*m = *n;
	*n = temp;
}

int main(){
	int a, b;
	printf("Enter any two integers: ");
	scanf("%d %d", &a, &b);
	swap(&a, &b);
	printf("The numbers after swapping are : %d & %d.", a, b);
	return 0;
}
