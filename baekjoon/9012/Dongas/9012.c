#include <stdio.h>
#include <string.h>

int main(){
    int num = 0, i = 0, count = 0;  
    scanf("%d",&num);

    for(i = 0;i<num;i++){
        char string[50];
        scanf("%s",&string);
        
        int len = strlen(string);
        
        if(len >= 2){
            if(string[i]=='('){
                count++;
            }
            else if(string[i]==')'){
                if(count<=0){
                    printf("NO\n");
                    return 0;
                }
                else count--;
            }
        }
    }

    if(count == 0){
        printf("YES\n");
    }else{
        printf("NO\n");
    }
}