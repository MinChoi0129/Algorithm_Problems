#include <stdio.h>
int main() {
	int tree;
	int up;
	int down;
	scanf("%d %d %d", &up, &down, &tree);
	int day = 0;
	int total_move = 0;

	while (total_move < tree) {
		day++;
		total_move += up;
		if (total_move >= tree) {
			break;
		}
		else {
			total_move -= down;
		}
	}
	printf("%d", day);
	return 0;
}