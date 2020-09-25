* Grades 2 Scores *

#include <stdio.h>
#define SIZE 10
void convert(double grades[], double scores[], int size) {
	for (int i = 0; i < size; i++) {
		scores[i] = grades[i] * 100 / 4.3;
	}
}
void print_grades_scores(double arr[], int size) {
	for (int i = 0; i < size; i++) {
		printf("%.2f\t", arr[i]);
	}
	printf("\n");
}
int main() {
	double grades[SIZE] = { 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.3 };
	double scores[SIZE];
	print_grades_scores(grades, SIZE);
	convert(grades, scores, SIZE);
	print_grades_scores(scores, SIZE);
	return 0;
}
-------------------------------------------------------------------------------------------------------------------------------
* Salary addition *

#include <stdio.h>
#define SIZE 10
void salary_add(int arr_basic[], int arr_plus[], int arr_total[], int size) {
	for (int i = 0; i < size; i++) {
		arr_total[i] = arr_basic[i] + arr_plus[i];
	}
}
void print_salary(int arr[], int size, char alphabet) {
	printf("%c[] = ", alphabet);
	for (int i = 0; i < size; i++) {
		printf("%2d\t", arr[i]);
	}
	printf("\n");
}
int main() {
	int A[SIZE] = { 22,31,53,11,26,23,75,96,50,21 };
	int B[SIZE] = { 20,22,24,26,28,30,32,34,36,38 };
	int C[SIZE];
	salary_add(A, B, C, SIZE);
	print_salary(A, SIZE, 'A');
	print_salary(B, SIZE, 'B');
	print_salary(C, SIZE, 'C');
	return 0;
}