#include <stdio.h>
#include <stdlib.h>

#define MAX_QUEUES 10

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

typedef struct queue *queuePointer;
typedef struct queue {
    element data;
    queuePointer link;
}queue;

queuePointer front[MAX_QUEUES], rear[MAX_QUEUES];

void enqueue(int i, element item) {
    queuePointer newNode;
    MALLOC(newNode, sizeof(*newNode));
    newNode->data = item;
    newNode->link = NULL;
    if (front[i])
        rear[i]->link = newNode;
    else
        front[i] = newNode;
    rear[i] = newNode;
    printf("%d and %c enqueued to queue number %d\n", newNode->data.key, newNode->data.c, i+1);
}

element queueEmpty(element item)
{
    item.key = -1;
    item.c = ' ';
    return item;
}

element dequeue(int i) {
    element item;
    queuePointer temp = front[i];
    if (!temp)
        return queueEmpty(item);
    item = temp->data;
    front[i] = temp->link;
    free(temp);
    return item;
}

void displayItem(int i, element item) {
    if (item.key == -1 && item.c == ' ')
        printf("Queue number %d is empty\n", i+1);
    else
        printf("%d and %c dequeued from the queue number %d\n", item.key, item.c, i+1);
}

int main() {
    element item;

    item.key = 10;
    item.c = '$';
    enqueue(8, item);

    item.key = 20;
    item.c = 'b';
    enqueue(8, item);

    item = dequeue(8);
    displayItem(8, item);

    item = dequeue(8);
    displayItem(8, item);
    
    item = dequeue(8);
    displayItem(8, item);

    item.key = 30;
    item.c = 'c';
    enqueue(8, item);

    return 0;
}