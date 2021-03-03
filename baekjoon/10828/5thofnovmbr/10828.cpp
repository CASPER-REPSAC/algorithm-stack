#include<stdio.h>
#include<string>
#include<iostream>

struct Stack
{
	int data;
	Stack* prev;
	Stack* next;
};

// 포인터 선언시 malloc으로 초기화하지 않으면 NULL값을 가진다.
Stack* currentStack;

void Push(int _data) {
	Stack* newStack = (Stack*)malloc(sizeof(Stack));
	newStack->data = _data;
	newStack->next = NULL;

	if (currentStack == NULL) {
		newStack->prev = NULL;
		currentStack = newStack;
	}
	else {
		newStack->prev = currentStack;
		currentStack->next = newStack;
		currentStack = newStack;
	}
}

int Pop() {
	int ans = 0;
	if (currentStack == NULL) return -1;
	else {
		ans = currentStack->data;
		Stack* temp = currentStack;

		currentStack = currentStack->prev;

		free(temp);

		if (currentStack) currentStack->next = NULL;

		return ans;
	}
}

int Size() {
	int count = 0;
	Stack* temp = currentStack;
	while (temp) {
		count++;
		temp = temp->prev;
	}
	return count;
}

int Empty() {
	if (currentStack == NULL) return 1;
	else return 0;
}

int Top() {
	if (currentStack == NULL) return -1;
	else return currentStack->data;
}

void stackProcessor(std::string _command) {
	int ans = 0;
	bool isprint = true;

	if (_command.substr(0, 4) == "push") {
		Push(atoi(_command.substr(5).c_str()));
		isprint = false;
	}
	else if (_command == "pop") {
		ans = Pop();
	}
	else if (_command == "size") {
		ans = Size();
	}
	else if (_command == "empty") {
		ans = Empty();
	}
	else if (_command == "top") {
		ans = Top();
	}
	else {
		isprint = false;
		printf("오류\n");
	}

	if (isprint) printf("%d\n", ans);
}

int main(void) {
	int t = 0, i = 0;
	char temp;
	std::string command;

	scanf("%d", &t);
	temp = getchar();

	for (i = 0; i < t; i++) {
		std::getline(std::cin, command);
		stackProcessor(command);
	}

	return 0;
}