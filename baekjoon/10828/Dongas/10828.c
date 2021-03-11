#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
    int data;
    struct node* link;
}Stack;

Stack* getnode() {
    Stack* newnode = (Stack*)malloc(sizeof(Stack));
    newnode->link = NULL;
    return newnode;
}

void Push(Stack** top, int data) {
    Stack* tmp = *top;
    *top = getnode();
    (*top)->data = data;
    (*top)->link = tmp;
}

int Pop(Stack** top) {
    if (*top == NULL) {
        return -1;
    }
    Stack* tmp = *top;
    int num = (*top)->data;
    *top = (*top)->link;
    free(tmp);
    return num;
}

int Empty(Stack* top) {
    if (top == NULL) {
        return 1;
    }
    else return 0;
}

int Size(Stack* top) {
    int size = 0;
    while (top != NULL) {
        size++;
        top = top->link;
    }
    return size;
}

int Top(Stack* top) {
    if (top == NULL) {
        return -1;
    }
    else {
        return top->data;
    }
}

int main() {
    int maxsize = 10000;
    int num;
    Stack* top = NULL;
    int data = 0, i = 0;

    scanf("%d", &num);

    for (i = 0;i < num;i++) {
        char cmd[10];
        scanf("%s", cmd);

        if (!strcmp(cmd, "push")) {
            scanf("%d", &data);
            Push(&top, data);
        }
        else if (!strcmp(cmd, "pop")) {
            printf("%d", Pop(&top));
        }
        else if (!strcmp(cmd, "size")) {
            printf("%d", Size(top));
        }
        else if (!strcmp(cmd, "empty")) {
            printf("%d", Empty(top));
        }
        else if (!strcmp(cmd, "top")) {
            printf("%d", Top(top));
        }
        else {
            printf("Error");
        }
    }
}