#include<stdio.h>
#include<iostream>

int main(void) {
	int n, k;

	scanf("%d %d", &n, &k);

	int* circle = (int*)malloc(sizeof(int) * n);
	int* output = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++) {
		*(circle + i) = i + 1;
	}

	int currentPoint = 0;

	for (int i = 0; i < n; i++) {
		int count = 0;
		while (count < k) {
			if (*(circle + currentPoint) > 0) {
				count++;
			}
			if (count == k) {
				*(output + i) = *(circle + currentPoint);
				*(circle + currentPoint) = 0;
			}
			currentPoint = (currentPoint + 1) % n;
		}
	}

	printf("<");
	for (int i = 0; i < n-1; i++) {
		printf("%d, ", *(output + i));
	}
	printf("%d>\n", *(output + n - 1));
}