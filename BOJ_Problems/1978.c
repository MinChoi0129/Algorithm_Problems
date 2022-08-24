#include <stdio.h>

int is_prime(int num) {
	if (num == 1) {
		return 0;
	}
	else if (num == 2) {
		return 1;
	}
	else {
		for (int i = 2; i <= num - 1; i++) {
			if (num % i == 0) {
				return 0;
			}
		}
		return 1;
	}
}

int main() {

	int n;
	int count = 0;
	scanf("%d", &n);
	int* num = (int*)malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &num[i]);
		
	}
	for (int i = 0; i < n; i++) {
		int value = is_prime(num[i]);
		if (value == 1) {
			count++;
		}
	}
	printf("%d\n", count);


	return 0;
}