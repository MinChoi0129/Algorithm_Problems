#include <stdio.h>
#define PI 3.14159265358979

int main() {

	int r;
	scanf("%d", &r);
	printf("%.6f\n%.6f\n", PI * r * r, 2.0 * r * r);

	return 0;
}