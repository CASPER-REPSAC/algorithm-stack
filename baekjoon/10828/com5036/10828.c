#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int stack[10000];


void push(char* str, int stack_cnt)
{
	str = &str[1];
	int num = atoi(str);

	stack[stack_cnt] = num;
}

int pop(int stack_cnt)
{
	if (stack_cnt == 0)
	{
		printf("-1\n");
		return stack_cnt;
	}
	printf("%d\n", stack[stack_cnt - 1]);
	return stack_cnt - 1;

}

void size(int stack_cnt)
{
	printf("%d\n", stack_cnt);
}

void empty(int stack_cnt)
{
	if (stack_cnt == 0)
		printf("1\n");
	else
		printf("0\n");
}

void top(int stack_cnt)
{
	if (stack_cnt == 0)
	{
		printf("-1\n");
		return;
	}

	printf("%d\n", stack[(stack_cnt - 1)]);

}

void clearreadbuffer(void)
{
	while (getchar() != '\n');
}



int main(void)
{
	int N;
	int stack_cnt = 0;

	char cmd[50];

	scanf("%d", &N);
	clearreadbuffer();


	for (int i = 0; i < N; i++) {

		fgets(cmd, sizeof(cmd), stdin);
		cmd[strlen(cmd) - 1] = '\0';

		if (strstr(cmd, "push") == cmd)
		{
			push(strstr(cmd, " "), stack_cnt++);

		}
		else if (!strcmp(cmd, "pop"))
		{
			stack_cnt = pop(stack_cnt);
		}
		else if (!strcmp(cmd, "size"))
		{
			size(stack_cnt);

		}
		else if (!strcmp(cmd, "empty"))
		{
			empty(stack_cnt);

		}
		else if (!strcmp(cmd, "top"))
		{
			top(stack_cnt);

		}
		else
		{
			printf("ERROR\n");
		}
	}

}
