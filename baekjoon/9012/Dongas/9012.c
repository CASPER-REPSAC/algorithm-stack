#include <stdio.h>
#include <string.h>

int main() {
    int num = 0, i = 0, j=0;
    scanf("%d", &num);

    for (i = 0;i < num;i++) {
        char string[50];
        scanf("%s", string);
        int count = 0;

        int len = strlen(string);

        for (j = 0;j < len;j++) {
            if (string[j] == '(') {
                count++;
            }
            else if (string[j] == ')') {
                if (count <= 0) {
                    count -= 100;
                }
                else count--;
            }
        }
        if (count == 0) {
            printf("YES\n");
        }
        else {
            printf("NO\n");
        }
    }
}