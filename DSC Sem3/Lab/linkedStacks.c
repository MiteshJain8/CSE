#include <stdio.h>
#include <stdlib.h>

#define MAX_STACKS 10

#define MALLOC(p, s) \
if (!((p) = malloc(s))) \
{ \
    fprintf(stderr, "Insufficient memory"); \
    exit(EXIT_FAILURE); \
}

typedef struct element
{
    int key;
    char c;
}element;

typedef struct stack *stackPointer;
typedef struct stack {
    element data;
    stackPointer link;
}stack;

stackPointer top[MAX_STACKS];

void push(int i, element item)
{
    stackPointer newNode;
    MALLOC(newNode, sizeof(*newNode));
    newNode->data = item;
    newNode->link = top[i];
    top[i] = newNode;
    printf("%d and %c pushed to stack number %d\n", newNode->data.key, newNode->data.c, i+1);
}

element stackEmpty(element item) {
    item.key = -1;
    item.c = ' ';
    return item;
}
element pop(int i)
{
    stackPointer temp = top[i];
    element item;
    if (!temp)
        return stackEmpty(item);
    item = temp->data;
    top[i] = temp->link;
    free(temp);
    return item;
}

void displayItem(int i, element item) {
    if (item.key == -1 && item.c == ' ')
        printf("Stack number %d is empty\n", i+1);
    else
        printf("%d and %c popped from the stack number %d\n", item.key, item.c, i+1);
}

int main() {
    element item;

    item.key = 10;
    item.c = '$';
    push(8, item);

    item.key = 20;
    item.c = 'b';
    push(8, item);

    item = pop(8);
    displayItem(8, item);

    item = pop(8);
    displayItem(8, item);
    
    item = pop(8);
    displayItem(8, item);

    item.key = 30;
    item.c = 'c';
    push(8, item);

    return 0;
}