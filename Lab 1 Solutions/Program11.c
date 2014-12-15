#include <stdio.h>

void add(int a, int b, int c, int d){
	int e = a + c, f = b + d;
	printf("The sum is %d + %dj.\n", e, f);
}

void sub(int a, int b, int c, int d){
	int e = a - c, f = b - d;
	printf("The difference is %d + %dj.\n", e, f);
}

void mul(int a, int b, int c, int d){
	int e = a*c - b*d, f = a*d + b*c;
	printf("The product is %d + %dj.\n", e, f);
}

void conju(int a, int b, int *c, int *d){
	*c = a;
	*d = -b;
}

void mulp(int a, int b, int c, int d, int *e, int *f){
	*e = a*c - b*d;
	*f = a*d + b*c;
}

void div(int a, int b, int c, int d){
	int e, f;
	float g, h;
	conju(c, d, &e, &f);
	mulp(c, d, e, f, &c, &d);
	mulp(a, b, e, f, &a, &b);
	g = (float)a/c;
	h = (float)b/c;
	printf("The quotient is %f + %fj.\n", g, h);
}

int main(){
	int a, b, c, d;
	printf("Enter any two complex numbers with separated real and imaginary parts of each(Eg. 4+2j should be written as 4 2): ");
	scanf("%d %d %d %d", &a, &b, &c, &d);
	add(a, b, c, d);
	sub(a, b, c, d);
	mul(a, b, c, d);
	div(a, b, c, d);
	return 0;
}
