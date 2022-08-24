#include <stdio.h>

int main() {

	int n;
	scanf("%d", &n);
	int count = 0;
	for (int i = 1; i <= n; i++) {
		if (i % 5 == 0) {
			count++;
		}
		if (i % 25 == 0) {
			count++;
		}
		if (i % 125 == 0) {
			count++;
		}
	}

	printf("%d", count);

	return 0;
}