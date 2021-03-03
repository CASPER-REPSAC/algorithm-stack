#include <stdio.h>
#include <string.h>

int main() {
    int num;
    scanf("%d", &num);

    for(int i=0; i<num; i++){
        char input[50];
        scanf("%s", input);

        int length = strlen(input);
        int stack = 0;
        int check = 0;
        for(int i=0; i<length; i++){
            if(input[i] == '('){
                stack++;
            }
            else{
                if(stack == 0){
                    check = 1;
                    break;
                }
                else stack--;
            }
        }

        if(!check && stack == 0) printf("YES\n");
        else printf("NO\n");
    }
}