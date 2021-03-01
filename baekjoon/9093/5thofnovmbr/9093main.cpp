#include <iostream>
#include <stdio.h>

#define LINE 1000

char* reverse(int);

char* st;

int main(void) {
	int t;
	int i; 

	scanf("%d", &t);
	getchar();

	st = (char*)malloc(sizeof(char) * LINE * t);
	// 포인터를 2차원 배열 같은 느낌으로 활용

	for (i = 0; i < t; i++)
	{
		scanf("%[^\n]s", st + (LINE * i));
		// 띄어쓰기까지 포함해서 입력
		getchar();
		// getchar이 없으면 엔터를 눌러도 무시하고 계속 진행되기 때문에 끊어주기 위해 사용

	}

	for (i = 0; i < t; i++)
	{
		if (i == t - 1)
		{
			printf("%s", reverse(i));
			break;
		}
		printf("%s\n", reverse(i));
	}

	return 0;
}

char* reverse(int seq)
{
	int space = 0, preSpace=0;
	char temp[LINE] = {0,};
	seq *= LINE;

	for (int i = 0; i < LINE; i++)
	{
		if((st+ seq)[i] == ' ' || (st + seq)[i] ==0x00)
		{
			space = i - preSpace;
			// 띄어쓰기 간 간격 구하기
			for (int j = space; j > 0; j--)
			{
				temp[i - j] = (st + seq)[preSpace+j-1];
				// 현재 띄어쓰기 위치와 이전 띄어쓰기 위치를 이용해 단어 뒤집기
			}
			temp[i] = (st + seq)[i];
			preSpace = i+1;
		}
	}
	return temp;
}

// 포인터를 더하기, 빼기로 조작할 수 있는걸 처음 알게 되었다.