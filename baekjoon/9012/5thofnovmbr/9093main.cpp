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
	// �����͸� 2���� �迭 ���� �������� Ȱ��

	for (i = 0; i < t; i++)
	{
		scanf("%[^\n]s", st + (LINE * i));
		// ������� �����ؼ� �Է�
		getchar();
		// getchar�� ������ ���͸� ������ �����ϰ� ��� ����Ǳ� ������ �����ֱ� ���� ���

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
			// ���� �� ���� ���ϱ�
			for (int j = space; j > 0; j--)
			{
				temp[i - j] = (st + seq)[preSpace+j-1];
				// ���� ���� ��ġ�� ���� ���� ��ġ�� �̿��� �ܾ� ������
			}
			temp[i] = (st + seq)[i];
			preSpace = i+1;
		}
	}
	return temp;
}

// �����͸� ���ϱ�, ����� ������ �� �ִ°� ó�� �˰� �Ǿ���.