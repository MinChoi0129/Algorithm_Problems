#include <stdio.h>
#include <string.h>

int find(int arr[], char* str, int n){
	if(strcmp(str, "min")){
		int min = 1;
		for(int i=0; i<n; i++){
			if(arr[i]>=1){
				if(min>arr[i]){
					min = arr[i];
				}
			}
		}
		return min;
	}
	else{
		int max = 0;
		for(int i=0; i<n; i++){
			if(arr[i]>=1){
				if(max<arr[i]){
					max = arr[i];
				}
			}
		}
		return max;
	}
}

int acid_1_to_1000[1001]; // 모든 원소 = 0

int main() {

	int n;
	scanf("%d", &n);
	int* acid = (int*)malloc(sizeof(int)*n);

	for(int i=0; i<n; i++){
		scanf("%d", &acid[i]);
	}

	for(int i=0; i<n; i++){
		for(int j=1; j<=1000; j++){
			if(acid[i]==j){
				acid_1_to_1000[j]++;
				break;
			}
		}
	} // count 끝.

	int min_times = find(acid_1_to_1000, "min", n);
	int max_times = find(acid_1_to_1000, "max", n);




	return 0;
}