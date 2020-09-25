#include <stdio.h>

int find_max_score(int* score, int size) {
	int max = -1;
	for (int i = 0; i < size; i++) {
		if (score[i] > max) {
			max = score[i];
		}
	}
	return max;
}

int main() {

	int subj_num;
	scanf("%d", &subj_num);
	int* old_score = (int*)malloc(sizeof(int) * subj_num);
	double* new_score = (double*)malloc(sizeof(double) * subj_num);
	for (int i = 0; i < subj_num; i++) {
		scanf("%d", &old_score[i]);
	}
	int max_score = find_max_score(old_score, subj_num);
	for (int i = 0; i < subj_num; i++) {
		new_score[i] = old_score[i] / (double)max_score * 100;
	}
	double sum = 0;
	for (int i = 0; i < subj_num; i++) {
		sum += new_score[i];
	}
	printf("%.50lf", sum / subj_num);

	return 0;
}