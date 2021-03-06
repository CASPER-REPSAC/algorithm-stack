#include <stdio.h>
#include <stdlib.h>

int main() {
	int n, result_n = 0;
	int top = -1, t = 1;
	scanf("%d", &n);

	int* input = (int*)malloc(sizeof(int) * n);
	int* stack = (int*)malloc(sizeof(int) * n);
	char* result = (char*)malloc(sizeof(char) * n * 2);

	for (int i = 0; i < n; i++)
		scanf("%d", &input[i]);

	for (int i = 0; i < n; i++) {
		while (result_n < n * 2) {
			if (stack[top] == input[i]) {
				stack[top--] = 0;
				result[result_n++] = '-';
				break;
			}
			stack[++top] = t++;
			result[result_n++] = '+';
		}
	}

	if (top != -1) {
		printf("NO");
	}
	else {
		for (int i = 0; i < n * 2; i++)
			printf("%c\n", result[i]);
	}
	return 0;
}
