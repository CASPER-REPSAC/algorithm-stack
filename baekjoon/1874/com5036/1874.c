#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int MaxNum_Index(int* arr, int arr_size); //배열에서 가장 큰 수의 인덱스 값 반환
int Is_this_possible(int* stack, int arr_size); //수열을 만들 수 있는지 판단 (가능: 1, 불가능 : 0 반환)
void push_or_pop(int* arr, int* stack, int arr_size); //push 할지 pop 할지 계산해서 + - 출력

int main(void)
{
	static int arr[100000];
	static int stack[100000];

	int n;
	scanf_s("%d", &n);

	for (int i = 0; i < n; i++)
		scanf_s("%d", &arr[i]);
	

	if (Is_this_possible(arr, n) == 1)
	{
		push_or_pop(arr, stack, n);
		return 0;
	}
	else if (Is_this_possible(arr, n) == -1)
	{
		printf("ERROR\n");
	}
	else
	{
		printf("NO");
		return 0;
	}
	return 0;
}


void push_or_pop(int* arr, int* stack, int arr_size)
{
	int num = 1, s = 0, a =0, r=0;

	for (num = 1; num <= arr_size ; num++)
	{
		stack[s] = num;
		printf("+\n");
		
		while (stack[s] == arr[a])
		{
			printf("-\n");
			s--;
			a++;
			if (s < 0 || a >= arr_size)
				return;
		}
		s++;
	}
}

int MaxNum_Index(int* arr, int arr_size)
{
	int max = arr[0];
	int i = 0, j = 0;

	for (i = 0; i < arr_size; i++)
		max = (max < arr[i + 1]) ? arr[i + 1] : max;

	while (arr[j] != max)
		j++;

	return j;
}

int Is_this_possible(int* arr, int arr_size)
{
	for (int j = 0; MaxNum_Index(arr, arr_size) + 2 + j < arr_size; j++)
	{
		if (arr[MaxNum_Index(arr, arr_size) + 1 + j] > arr[MaxNum_Index(arr, arr_size) + 2 + j])
			return 1;
		else
			return 0;
	}

	return -1;
}
