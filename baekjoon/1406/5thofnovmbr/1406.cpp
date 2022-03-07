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

// ��� �ʱ�ȭ
int nodeInit() {
	head->next = NULL;
	head->data = NULL;
	curr = head;
	currNum = 0;

	return true;
}

// Ŀ�� ���������� �� ĭ
int commandD() {
	if (curr->next) {
		curr = curr->next;
		currNum++;
		return true;
	}
	return false;
}

// Ŀ�� �������� �� ĭ
int commandL() {
	if (currNum > 0) {
		currNum--;
		curr = head;
		for (int i = 0; i < currNum; i++) {
			// currNum = 0�̸� ���� ù��° Ŀ��
			// 1�̸� ù��° ���� ��
			curr = curr->next;
		}
		return true;
	}
	return false;
}

// Ŀ�� ���� ���� ����
int commandB() {
	if (commandL()) {
		Node* temp = curr->next;
		curr->next = temp->next;
		free(temp);
		return true;
	}
	return false;
}

// Ŀ�� ���ʿ� ���� �߰�
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