#include <stdio.h>
#include <string.h>

int main(){
	char name[5] = "BITS", place[7] = "Pilani";
	strcat(name, " ");
	strcat(name, place);
	printf("%s", name);
	return 0;
}
