#include <stdio.h>
#include <math.h>

int count_ryu_pos(int x1, int y1, int r1, int x2, int y2, int r2) {
	double d = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2));

	if (d > r1 + r2) {
		return 0;
	}
	else if (d < abs(r1 - r2)) {
		return 0;
	}
	else if (d == 0 && r1 == r2) {
		return -1;
	}
	else if (d == r1 + r2) {
		return 1;
	}
	else if (d == abs(r1 - r2)) {
		return 1;
	}
	else {
		return 2;
	}
}
int main() {

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int x1, y1, r1, x2, y2, r2;
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
		
		printf("%d\n", count_ryu_pos(x1, y1, r1, x2, y2, r2));
	}

	return 0;
}