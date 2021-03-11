#include<stdio.h>
2
#include<string.h>
3
​
4
int stack[51];
5
int top = -1;
6
​
7
int main() {
8
    int input;
9
    char data[51];
10
    scanf("%d", &input);
11
​
12
    while (input != 0) {
13
        scanf("%s", data);
14
​
15
        for (int i = 0; i < strlen(data); i++) {
16
            if (data[i] == '(')
17
                stack[++top] = 1;
18
            if (data[i] == ')')
19
                stack[top--] = NULL;
20
            if (top < -1)
21
                break;
22
        }
23
        if (top != -1) printf("NO\n");
24
        else printf("YES\n");
25
        top = -1;
26
        input--;
27
    }
28
​
29
    return 0;
30
}
