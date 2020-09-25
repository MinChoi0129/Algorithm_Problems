#include <stdio.h>
int main() {
	int a = 1;
	int b = 1;
	int c = 1;
	while (!(a == 0 && b == 0 && c == 0)) {
		scanf("%d %d %d", &a, &b, &c);
		if (a == 0 && b == 0 && c == 0) {
			break;
		}
		else if (a == 0 || b == 0 || c == 0) {
			if (a == 0) {
				printf("wrong\n");
			}
			else if (b == 0) {
				printf("wrong\n");
			}
			else {
				printf("wrong\n");
			}
		}
		else {
			if ((a * a + b * b == c * c) || (a * a + c * c == b * b) || (c * c + b * b == a * a)) {
				printf("right\n");
			}
			else {
				printf("wrong\n");
			}
		}
	}
	return 0;
}