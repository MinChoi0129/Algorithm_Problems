#include <stdio.h>

int is_hansu(int put) {
	int hund = put / 100;
	int ten = put / 10 % 10;
	int one = put % 10;
	if (2 * ten == hund + one) {
		return 1;
	}
	else {
		return 0;
	}
}

int main() {

	int n, count = 99;
	scanf("%d", &n);

	if (n < 100) {
		printf("%d", n);
	} // n이 1에서 99까지면
	else { //n이 100이상이면
		for (int i = 100; i <= n; i++) {
			if (is_hansu(i) == 1) {
				count++;
			}
			else {
			}
		}
		printf("%d", count);
	}
	

	return 0;
}