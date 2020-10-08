#include <stdio.h>

struct point {
	int x;
	int y;
};

int main(void) {
	struct point p1, p2, p3, p4;
	scanf("%d %d", &p1.x, &p1.y);
	scanf("%d %d", &p2.x, &p2.y);
	scanf("%d %d", &p3.x, &p3.y);

	if (p1.x == p2.x) {
		p4.x = p3.x;
	}
	else if (p1.x == p3.x) {
		p4.x = p2.x;
	}
	else {
		p4.x = p1.x;
	}

	if (p1.y == p2.y) {
		p4.y = p3.y;
	}
	else if (p1.y == p3.y) {
		p4.y = p2.y;
	}
	else {
		p4.y = p1.y;
	}
	printf("%d %d", p4.x, p4.y);
	return 0;
}