#include <stdio.h>

int clap(int user, int n) {

	if (n < 10) { // 1 ~ 9

		if (n == 3 || n == 6 || n == 9) { // n == 3, 6, 9

			if (user == 1) { // clap == 1
				return 0;
			}

			else { // clap != 1
				return -1;
			}

		}

		else { // n != 3, 6, 9

			if (user == 0) { // clap == 0
				return 0;
			}

			else { // clap != 0
				return -1;
			}

		}

	}

	else if (n < 100) { // 10 ~ 99

		int digit_10 = n / 10;
		int digit_1 = n % 10;

		if (digit_10 == 3 || digit_10 == 6 || digit_10 == 9) { // n == 30대, 60대, 90대

			if (digit_1 == 3 || digit_1 == 6 || digit_1 == 9) { // n == 33, 36, 39

				if (user == 2) { // clap == 2
					return 0;
				}

				else { // clap != 2
					return -1;
				}

			}

			else { // n == 30대, 60대 90대이면서 33, 36, 39는 아닌 수

				if (user == 1) { // clap == 1
					return 0;
				}

				else {
					return -1; // clap != 1
				}

			}

		}

		else { // n != 30대, 60대, 90대

			if (digit_1 == 3 || digit_1 == 6 || digit_1 == 9) { // 1의자리만 3, 6, 9 인경우

				if (user == 1) { // clap == 1
					return 0;
				}

				else { // clap != 1
					return -1;
				}

			}

			else {

				if (user == 0) { // clap == 0
					return 0;
				}

				else {
					return -1; // clap != 0
				}

			}

		}

	}

	//else if (n < 1000) { // 100 ~ 999

	//	int digit_100 = n / 100;
	//	int digit_10 = (n / 10) % 10;
	//	int digit_1 = n % 100;

	//	if (digit_100 == 3 || digit_100 == 6 || digit_100 == 9) {

	//		if (digit_10 == 3 || digit_10 == 6 || digit_10 == 9) {

	//			if (digit_1 == 3 || digit_1 == 6 || digit_1 == 9) {

	//				if (user == 3) {
	//					return 0;
	//				}

	//				else {
	//					return -1;
	//				}

	//			}

	//			else {

	//				if (user == 2) {
	//					return 0;
	//				}

	//				else {
	//					return -1;
	//				}

	//			}

	//		}

	//		else {

	//			if (digit_1 == 3 || digit_1 == 6 || digit_1 == 9) {

	//				if (user == 2) {
	//					return 0;
	//				}

	//				else {
	//					return -1;
	//				}

	//			}

	//			else {
	//				if (user == 1) {
	//					return 0;
	//				}

	//				else {
	//					return -1;
	//				}

	//			}

	//		}

	//	}

	//	else {

	//		if (digit_10 == 3 || digit_10 == 6 || digit_10 == 9) {

	//			if (digit_1 == 3 || digit_1 == 6 || digit_1 == 9) {

	//				if (user == 2) {
	//					return 0;
	//				}

	//				else {
	//					return -1;
	//				}

	//			}

	//			else {

	//				if (user == 1) {
	//					return 0;
	//				}

	//				else {
	//					return -1;
	//				}

	//			}

	//		}

	//		else {

	//			if (digit_1 == 3 || digit_1 == 6 || digit_1 == 9) {

	//				if (user == 1) {
	//					return 0;
	//				}

	//				else {
	//					return -1;
	//				}

	//			}

	//			else {

	//				if (user == 0) {
	//					return 0;
	//				}

	//				else {
	//					return -1;
	//				}

	//			}

	//		}

	//	}

	//}

	else {

		printf("\n\n%d 통과!!\n\a", n);
		return 1;

	}
}

int game_369(int n) {

	int user;
	scanf_s("%d", &user, sizeof(user));

	int value = clap(user, n);
	if (value == 0) {
		return 0;
	}

	else if (value == 1) {
		printf("\n축하합니다. 게임을 통과하셨습니다!!\n\n");
		return -1;
	}
	else {
		printf("\n\n틀렸습니다!\n\a이번 차례의 숫자 = %d\n\n", n);
		return -1;
	}

}


int main() {

	int n = 1;

	while (game_369(n) != -1) {
		n++;
	}

	return 0;
}