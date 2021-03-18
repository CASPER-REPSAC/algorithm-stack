#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void push(char* str, int push_cnt, int* stack_ptr)
{
	str = &str[1];
	int num = atoi(str);

	stack_ptr[push_cnt] = num;
}

void pop(int push_cnt, int* pop_ptr, int* stack_ptr)
{
	if (push_cnt - *pop_ptr == 0)
	{
		printf("-1\n");
		return;
	}

	printf("%d\n", stack_ptr[(*pop_ptr)++]);
}

void size(int push_cnt, int pop_cnt)
{
	printf("%d\n", push_cnt - pop_cnt);
}

void empty(int push_cnt, int pop_cnt)
{
	if (push_cnt - pop_cnt == 0)
		printf("1\n");
	else
		printf("0\n");
}

void back(int push_cnt, int pop_cnt, int* stack_ptr)
{
	if (push_cnt - pop_cnt == 0)
	{
		printf("-1\n");
		return;
	}

	printf("%d\n", stack_ptr[(push_cnt - 1)]);
}

void front(int push_cnt, int pop_cnt, int* stack_ptr)
{
	if (push_cnt - pop_cnt == 0)
	{
		printf("-1\n");
		return;
	}

	printf("%d\n", stack_ptr[pop_cnt]);
}

void clearreadbuffer(void)
{
	while (getchar() != '\n');
}

int main(void) {
	int* stack;
	int N;
	int push_cnt = 0;
	int pop_cnt = 0;
	int* pop_ptr = &pop_cnt;
	char cmd[50];

	stack = malloc(sizeof(int) * 10000);

	scanf("%d", &N);
	clearreadbuffer();

	for (int i = 0; i < N; i++) {
		fgets(cmd, sizeof(cmd), stdin);
		cmd[strlen(cmd) - 1] = '\0';

		if (strstr(cmd, "push") == cmd)
			push(strstr(cmd, " "), push_cnt++, stack);
		else if (!strcmp(cmd, "pop"))
			pop(push_cnt, pop_ptr, stack);
		else if (!strcmp(cmd, "size"))
			size(push_cnt, pop_cnt);
		else if (!strcmp(cmd, "empty"))
			empty(push_cnt, pop_cnt);
		else if (!strcmp(cmd, "front"))
			front(push_cnt, pop_cnt, stack);
		else if (!strcmp(cmd, "back"))
			back(push_cnt, pop_cnt, stack);
		else
			printf("ERROR\n");
	}

	free(stack);
}
