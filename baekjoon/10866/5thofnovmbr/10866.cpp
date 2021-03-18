#include<stdio.h>
#include<string>
#include<iostream>

#define MAX_N 10000

struct Deque {
	int data;
	Deque* next;
};

Deque deque[MAX_N];
Deque* curr_front;
Deque* curr_back;
int deque_count;

void init(void) {
	curr_front = curr_back = deque;
	curr_front->data = curr_back->data = NULL;
	curr_front->next = curr_back->next = NULL;
	deque_count = 0;
}


void push_front(int _x) {
	if (curr_front->data) {
		deque_count++;
		(deque[deque_count]).next = curr_front;
		curr_front = &(deque[deque_count]);
	}
	curr_front->data = _x;
}
void push_back(int _x) {
	if (curr_back->data) {
		deque_count++;
		curr_back->next = &(deque[deque_count]);
		curr_back = curr_back->next;
	}
	curr_back->data = _x;
}
int pop_front(void) {
	int _ans = -1;
	if (curr_front->data) {
		_ans = curr_front->data;
		curr_front->data = NULL;
		if (curr_front->next) {
			Deque *temp = curr_front;
			curr_front = curr_front->next;
			temp->next = NULL;
		}
	}
	return _ans;
}
int pop_back(void) {
	int _ans = -1;
	if (curr_back->data) {
		_ans = curr_back->data;
		if (curr_back == curr_front) {
			curr_back->data = NULL;
			curr_back->next = NULL;
			curr_front->data = NULL;
			curr_front->next = NULL;
		}
		else {
			for (int i = 0; i < MAX_N; i++) {
				if (deque[i].next == curr_back) {
					curr_back = &(deque[i]);
					curr_back->next->data = NULL;
					curr_back->next->next = NULL;
					break;
				}
			}
		}
	}
	return _ans;
}
int size(void) {
	if (curr_back->data == NULL) {
		return 0;
	}
	else if (curr_back == curr_front) {
		return 1;
	}
	else {
		Deque* temp = curr_front;
		int i;
		for (i = 0; i < MAX_N; i++) {
			if (temp->next) {
				temp = temp->next;
			}
			else {
				return i + 1;
			}
		}
	}
}
int empty(void) {
	if (curr_front->data == NULL) {
		return 1;
	}
	return 0;
}
int front(void) {
	if (curr_front->data) {
		return curr_front->data;
	}
	return -1;
}
int back(void) {
	if (curr_back->data) {
		return curr_back->data;
	}
	return -1;
}

int main(void) {
	int n = 0;

	scanf("%d", &n);
	getchar();

	init();

	std::string command;

	for (int i = 0; i < n; i++) {
		int ans = 0;
		bool isPrint = true;

		std::getline(std::cin, command);
		if (command.substr(0, 6) == "push_f") {
			push_front(stoi(command.substr(11, command.length() - 11)));
			isPrint = false;
		}
		else if (command.substr(0, 6) == "push_b") {
			push_back(stoi(command.substr(10, command.length() - 10)));
			isPrint = false;
		}
		else if (command == "pop_front") {
			ans = pop_front();
		}
		else if (command == "pop_back") {
			ans = pop_back();
		}
		else if (command == "size") {
			ans = size();
		}
		else if (command == "empty") {
			ans = empty();
		}
		else if (command == "front") {
			ans = front();
		}
		else if (command == "back") {
			ans = back();
		}

		if (isPrint) {
			printf("%d\n", ans);
		}
	}
}