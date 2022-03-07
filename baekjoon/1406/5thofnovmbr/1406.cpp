#include<stdio.h>
#include<iostream>

#define N 100000

struct Node {
	Node* next;
	char data;
};

Node* head = (Node*)malloc(sizeof(Node));
Node* curr = (Node*)malloc(sizeof(Node));
int currNum;

// 노드 초기화
int nodeInit() {
	head->next = NULL;
	head->data = NULL;
	curr = head;
	currNum = 0;

	return true;
}

// 커서 오른쪽으로 한 칸
int commandD() {
	if (curr->next) {
		curr = curr->next;
		currNum++;
		return true;
	}
	return false;
}

// 커서 왼쪽으로 한 칸
int commandL() {
	if (currNum > 0) {
		currNum--;
		curr = head;
		for (int i = 0; i < currNum; i++) {
			// currNum = 0이면 제일 첫번째 커서
			// 1이면 첫번째 문자 뒤
			curr = curr->next;
		}
		return true;
	}
	return false;
}

// 커서 왼쪽 문자 삭제
int commandB() {
	if (commandL()) {
		Node* temp = curr->next;
		curr->next = temp->next;
		free(temp);
		return true;
	}
	return false;
}

// 커서 왼쪽에 문자 추가
int commandP(char _data) {
	Node* temp = (Node*)malloc(sizeof(Node));

	temp->data = _data;
	temp->next = curr->next;
	curr->next = temp;
	curr = temp;
	currNum++;

	return true;
}

int printAllNodeData() {
	curr = head;
	while (curr->next) {
		curr = curr->next;
		printf("%c", curr->data);
	}

	return true;
}

int main(void) {
	char st[N] = { 0, };

	char command[4];

	int M;

	nodeInit();

	std::cin >> st;

	for (int i = 0; i < N; i++) {
		if (st[i] == NULL) break;
		commandP(st[i]);
	}

	scanf("%d", &M);
	getchar();



	for (int i = 0; i < M; i++) {
		scanf("%[^\n]", &command);
		if (command[0] == 'L') {
			commandL();
		}
		else if (command[0] == 'D') {
			commandD();
		}
		else if (command[0] == 'B') {
			commandB();
		}
		else if (command[0] == 'P') {
			commandP(command[2]);
		}
		getchar();
	}

	printAllNodeData();

	return 0;
}