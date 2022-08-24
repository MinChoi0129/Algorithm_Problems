#include <stdio.h>
#include <stdlib.h>

void show(int num) {
	int* count = (int*)calloc((num + 1), sizeof(int));
	int temp = num;
	for (int i = 2; i <= num; i++) {
		while (temp % i == 0) {
			count[i]++;
			temp /= i;
		}
	}

	for (int i = 2; i <= num; i++) {
		if (count[i] > 0) {
			printf("%d %d\n", i, count[i]);
		}
	}
	free(count);
}

int main(void) {

	int n = 0;
	scanf("%d", &n);
	while (n--) {
		int num = 0;
		scanf("%d", &num);
		show(num);
	}

	return 0;
}