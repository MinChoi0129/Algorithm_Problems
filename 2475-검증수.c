#include <stdio.h>
#include <math.h>

int main() {

    int arr[5];
    scanf("%d %d %d %d %d", &arr[0], &arr[1], &arr[2], &arr[3], &arr[4]);
    
    int result = 0;
    for (int i = 0; i < 5; i++) {
        result += pow(arr[i], 2);
    }

    printf("%d", result % 10);

    return 0;
}