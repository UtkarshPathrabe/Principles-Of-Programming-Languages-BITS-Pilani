#include <stdio.h>

int * bubble_sort(int *a, int num){
	int i, j, temp;
	for(i = 0; i < num; i++){
		for(j = i+1; j < num; j++){
			if(a[i] > a[j]){
				temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}
	}
	return a;
}

int main(){
	int array[6] = {12, 5, 8, 16, 65, 10}, i, *a = NULL;
	a = bubble_sort(array, 6);
	printf("The sorted array is: \n");
	for(i = 0; i < 6; i++){
		printf("%d ", a[i]);
	}
	return 0;
}
