#include <stdio.h>
#include <iostream>

class ParenthesisString
{
public:
	int count;
	char ps[50];
	bool IsRight();
};


bool ParenthesisString::IsRight()
{
	count = 0;
	for (int i = 0; i < 50; i++)
	{
		if (ps[i] == '(') count++;
		else if (ps[i] == ')')count--;
		
		if (count < 0) return false;
	}

	if (count > 0) return false;

	return true;
}


int main(void)
{
	int t, i;
	ParenthesisString* PS;

	scanf("%d", &t);

	PS = (ParenthesisString*)malloc(sizeof(ParenthesisString) * t);

	for (i = 0; i < t; i++) 
	{
		scanf("%s", PS[i].ps);
	}

	for (i = 0; i < t; i++)
	{
		if (PS[i].IsRight() == true) printf("YES");
		else printf("NO");

		if (i < t - 1) printf("\n");
	}

	return 0;
}

