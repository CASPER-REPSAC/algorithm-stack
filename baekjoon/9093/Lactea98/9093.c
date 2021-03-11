#include <stdio.h>
#include <string.h>

#define MAX 1001

int main(){
    int num;
    scanf("%d", &num);
    while ((getchar()) != '\n');

    for(int i=0; i<num; i++){
        char input[MAX];
        fgets(input, MAX, stdin);
        
        int length = strlen(input);
        input[length - 1] = '\0';

        int char_length = 0;
        for(int index = 0; index < length; index++){
            if(input[index] == ' '){
                for(int i=0; i<char_length; i++){
                    printf("%c", input[index - 1 - i]);
                }
                printf(" ");
                char_length = 0;
            }
            else char_length++;
        }
        for(int i=0; i<char_length; i++){
            printf("%c", input[length - 1 - i]);
        }

        printf("\n");
    }
}