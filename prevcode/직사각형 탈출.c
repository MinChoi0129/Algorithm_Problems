#include <stdio.h>

int find_min(a, b, c, d) {
	int min = a;
	if (min > b) {
		min = b;
	}
	if (min > c) {
		min = c;
	}
	if (min > d) {
		min = d;
	}
	return min;
}

int main() {

	int left, right, up, down, x, y, w, h;

	scanf("%d %d %d %d", &x, &y, &w, &h);
	left = x;
	right = w - x;
	up = h - y;
	down = y;

	int min = find_min(left, right, up, down);
	printf("%d", min);

	return 0;
}