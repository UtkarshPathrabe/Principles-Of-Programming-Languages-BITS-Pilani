#include <stdio.h>
#include <string.h>

int main(){
	char string[12] = "BITS-Pilani";
	int i;
	for(i = 0; i < strlen(string); i++){
		printf("Current Letter: %c\n", string[i]);
	}
	return 0;
}
