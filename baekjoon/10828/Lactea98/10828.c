#include <stdio.h>
#include <string.h>

#define MAX_SIZE 10000

typedef struct Stack{
    int arr[MAX_SIZE];
    int size;
} Stack;

int main(){
    int num;
    Stack stack = {0,};

    scanf("%d", &num);
    for(int i=0; i<num; i++){
        char command[6];
        scanf("%s", command);

        if(!strcmp(command, "push")){
            int data;
            scanf("%d", &data);

            stack.arr[stack.size] = data;
            stack.size++;
        }
        else if(!strcmp(command, "pop")){
            printf("%d\n", (stack.size != 0 ? stack.arr[stack.size - 1] : -1));
            stack.size = (stack.size == 0 ? stack.size : --stack.size);
        }
        else if(!strcmp(command, "size")) printf("%d\n", stack.size);
        else if(!strcmp(command, "empty")) printf("%d\n", (stack.size != 0 ? 0 : 1));
        else if(!strcmp(command, "top")) printf("%d\n", (stack.size != 0 ? stack.arr[stack.size - 1] : -1));
    }
}