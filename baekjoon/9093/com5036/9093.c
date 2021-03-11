#include <stdio.h>
#include <string.h>

void Reverse_str(char* str);

int main(void)
{

	int T;
	char* devide;
	char str[1000];

	scanf("%d", &T);
	while (getchar() != '\n');

	for (int i = 0; i < T; i++)
	{
		int cnt = 0;

		fgets(str, sizeof(str), stdin);
		str[strlen(str) - 1] = '\0';

		devide = strtok(str, " ");
		while (devide != NULL)
		{
			Reverse_str(devide);
			devide = strtok(NULL, " ");
		}
		printf("\n");
	}
	return 0;
}

void Reverse_str(char* str)
{
	char tmp;

	if ((int)strlen(str) > 1)
	{
		for (int i = 0; i < (int)strlen(str) / 2; i++)
		{
			tmp = str[strlen(str) - i - 1];
			str[strlen(str) - i - 1] = str[i];
			str[i] = tmp;
		}
		printf("%s ", str);
	}
	else
	{
		printf("%s ", str);
	}
}