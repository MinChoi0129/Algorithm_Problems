#include <stdio.h>
int main() {
	int h, m, new_alarm;
	scanf("%d %d", &h, &m);
	new_alarm = 60 * h + m - 45;
	h = new_alarm / 60;
	m = new_alarm - 60 * h;
	if (!(h<0 || m<0)) {
		printf("%d %d", h, m);
	}
	else if (m < 0) {
		h += 23;
		m += 60;
		printf("%d %d", h, m);
	}
	else {
	}
	return 0;
}