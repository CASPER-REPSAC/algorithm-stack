#include <stdio.h>
#include <string.h>

typedef struct Queue{
    int start;
    int end;
    int size;
    int data[10000];
} Queue;

void init(Queue *q){
    q->start = 0;
    q->end = 0;
    q->size = 0;
}

int main(){
    int num;
    Queue queue;
    
    init(&queue);

    scanf("%d", &num);
    while(num--){
        char command[6];
        int data;

        scanf("%s", command);
        if(!strcmp(command, "push")){
            scanf("%d", &data);
            queue.data[queue.end] = data;
            queue.end++;
            queue.size++;
        }
        else if(!strcmp(command, "pop")){
            if(queue.size == 0) printf("-1\n");
            else{ 
                printf("%d\n", queue.data[queue.start]);
                queue.start++;
                queue.size--;
            }
        }
        else if(!strcmp(command, "size")) printf("%d\n", queue.size);
        else if(!strcmp(command, "empty")) printf("%d\n", (queue.size == 0 ? 1 : 0));
        else if(!strcmp(command, "front")) printf("%d\n", (queue.size == 0 ? -1 : queue.data[queue.start]));
        else if(!strcmp(command, "back")) printf("%d\n", (queue.size == 0 ? -1 : queue.data[queue.end-1]));
    }
}