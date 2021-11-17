#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int nCr(int n, int r) {
	int value;
	if (n == r) {
		return 1;
	}
	if (r == 0) {
		return 1;
	}
	return nCr(n - 1, r - 1) + nCr(n - 1, r);
}

int main() {

	int n, m;
	int r = 3;
	scanf("%d %d", &n, &m);
	int* cards = (int*)malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &cards[i]);
	}
	int* combi = (int*)malloc(sizeof(int) * nCr(n, r));

	for (int i = 0; i < nCr(n, r); i++) {
		printf("%d ", combi[i]);
	}

	return 0;
}