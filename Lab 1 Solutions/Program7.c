#include <stdio.h>

int main(){
	char fruits[4][7] = {"Banana", "Apple", "Grapes", "Orange"}, i;
	for(i = 0; i < 4; i++){
		printf("Current Fruit: %s\n", fruits[i]);
	}
	return 0;
}
