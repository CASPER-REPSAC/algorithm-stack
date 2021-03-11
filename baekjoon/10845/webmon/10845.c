#include <stdio.h>
#include <string.h>

int queue[10001];
int first=0, last=0;

int empty()
{
	if(first == last)
		return 1;
	else
		return 0;
}

void push(int data)
{
	queue[last++] = data;
}

int pop()
{
	if(empty())
		return -1;
	else{
		return queue[first++];
	}
}

int size()
{
	return (last-first);
}

int front()
{
	if(empty())
		return -1;
	else{
		return queue[first];
	}
}

int back()
{
	if(empty())
		return -1;
	else{
		return queue[last-1];
	}
}

int main(void)
{
	int n, tmp;
	char cmd[6];

	scanf("%d", &n);

	for(int i=0; i<n; i++){
		scanf("%s", cmd);
		if(!strcmp(cmd, "push")){
			scanf("%d", &tmp);
			push(tmp);
		}else if(!strcmp(cmd, "pop")){
			printf("%d\n", pop());
		}else if(!strcmp(cmd, "size")){
			printf("%d\n", size());
		}else if(!strcmp(cmd, "empty")){
			printf("%d\n", empty());
		}else if(!strcmp(cmd, "front")){
			printf("%d\n", front());
		}else{
			printf("%d\n", back());
		}
	}

	return 0;
}