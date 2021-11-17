#include <stdio.h>

int main() {

	int num[10];
	for (int i = 0; i < 10; i++) {
		scanf("%d", &num[i]);
	}
	int mod[42] = { 0 };
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 42; j++) {
			if (num[i] % 42 == j) {
				mod[j]++;
			}
		}
	}
	int count = 0;
	for (int i = 0; i < 42; i++) {
		if (mod[i] != 0) {
			count++;
		}
	}

	printf("%d", count);

	return 0;
}