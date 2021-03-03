#include <stdio.h>
#include <string.h>
int Is_This_VPS(char* str);

int main(void)
{
	int T;
	char str[51];

	scanf("%d", &T);
	while (getchar() != '\n');


	for (int i = 0; i < T; i++)
	{
		scanf("%s", str);
		while (getchar() != '\n');

		if (Is_This_VPS(str))
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}


int Is_This_VPS(char* str)
{
	if (str[0] == '(' || str[strlen(str) - 1] == ')')
	{
		int stack1 = 0, stack2 = 0, i = 0;

		for (i = 0; i < (int)strlen(str); i++)
		{
			if (str[i] == '(')
				stack1++;
			else if (str[i] == ')')
				stack2++;
			else
				stack1;

			if (stack1 < stack2)
				return 0;
		}

		if (stack1 == stack2)
			return 1;
		else
			return 0;
	}
	else
		return 0;
}