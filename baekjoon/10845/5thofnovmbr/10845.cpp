#include<stdio.h>
#include<stdlib.h>


int Qlist[10000];
int* head = Qlist;
int* frontCurr;
int* backCurr;

void init() {
	backCurr = frontCurr = NULL;
}

void push(int _data) {
	if (backCurr) {
		backCurr++;
	}
	else {
		backCurr = head;
		frontCurr = backCurr;
	}

	*backCurr = _data;
}

int pop() {
	if (frontCurr && frontCurr == backCurr) {
		int i = *frontCurr;
		frontCurr = backCurr = NULL;
		return i;
	}
	else if (frontCurr) {
		frontCurr++;
		return *(frontCurr - 1);
	}
	else {
		return -1;
	}
}

int size() {
	if (frontCurr) {
		return backCurr - frontCurr+1;
	}
	else return 0;
}

int empty() {
	if (frontCurr) return 0;
	else return 1;
}

int front() {
	if (frontCurr) return *frontCurr;
	else return -1;
}

int back() {
	if (backCurr) return *backCurr;
	else return -1;
}

int main() {
	int N;
	char command[15];

	init();

	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		int ans = 0;
		bool isprint = true;
		getchar();
		scanf("%[^\n]", &command);

		if (command[0] == 'p' && command[1] == 'u') {
			char numC[10] = "ddddddddd";
			for (int j = 5; j < 15; j++) {
				numC[j-5] = command[j];
			}
			push(atoi(numC));
			isprint = false;
		}
		else if (command[0] == 'p' && command[1] == 'o') {
			ans = pop();
		}
		else if (command[0] == 's') {
			ans = size();
		}
		else if (command[0] == 'e') {
			ans = empty();
		}
		else if (command[0] == 'f') {
			ans = front();
		}
		else if (command[0] == 'b') {
			ans = back();
		}
		if (isprint) {
			printf("%d\n", ans);
		}
	}

	return 0;
}