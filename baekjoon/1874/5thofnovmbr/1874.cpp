#include<stdio.h>
#include<iostream>

#define MAXLENGTH 100001

int n;
// result�� ����� ũ�� �����ؾ���.
char result[MAXLENGTH*2];

int storeCommand(int _sequence[]) {
	int i = 0, currentStack = -1, popcount = 0;
	int currentInputNum = 1;

	int temp[MAXLENGTH] = { 0, };

	while (popcount < n) {

		// ������ ������� push
		if (currentStack < 0) {
			currentStack++;
			temp[currentStack] = currentInputNum;
			result[i] = '+';
			currentInputNum++;
		} // ���ϴ� ���ڰ� ���� ���ÿ� ������ pop
		else if (_sequence[popcount] == temp[currentStack]) {
			temp[currentStack] = 0;
			currentStack--;
			result[i] = '-';
			popcount++;
		} // ���ϴ� ���ڰ� ���ÿ� �������� push
		else if (_sequence[popcount] >= currentInputNum) {
			currentStack++;
			temp[currentStack] = currentInputNum;
			result[i] = '+';
			currentInputNum++;
		}
		// ���ϴ� ���ڰ� ������ں��� ������ false��ȯ
		else if (_sequence[popcount] < currentInputNum) {
			return false;
		}
		else {
			printf("something unpredicted happend\n");
		}

		i++;
	}

	return true;
}

int main(void) {
	int i;
	int sequence[MAXLENGTH] = { 0, };

	scanf("%d", &n);

	for (i = 0; i < n; i++) {
		scanf("%d", &sequence[i]);
	}

	if (storeCommand(sequence)) {
		i = 0;
		while (result[i]!=0) {
			printf("%c\n", result[i]);
			i++;
		}
	}
	else {
		printf("NO");
	}

	return 0;
}