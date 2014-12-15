#include <stdio.h>

int search(int *a, int n, int ele){
	int found = -1, i;
	for(i=0;i<n;i++){
		if(a[i]==ele){
			found = 1;
			break;
		}
	}
	if(found==-1)
		return -1;
	else
		return i;
}

int main(){
	int n, i, ele;
	printf("Enter the number of elements: ");
	scanf("%d", &n);
	int array[n];
	printf("Enter the individual elements: ");
	for(i=0;i<n;i++){
		scanf("%d", &array[i]);
	}
	printf("Enter the element you want to search: ");
	scanf("%d", &ele);
	i = search(array, n, ele);
	if(i==-1)
		printf("The element is not present.");
	else
		printf("The element is present at position %d.", i);
	return 0;
}
