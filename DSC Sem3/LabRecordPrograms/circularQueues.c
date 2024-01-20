#include<stdio.h>
#include<stdlib.h>

int size=5;

#define MALLOC(p, s) \
if (!((p) = malloc(s))) \
{ \
    fprintf(stderr, "Insufficient memory"); \
    exit(EXIT_FAILURE); \
}

typedef struct element {
    int key;
} element;

element *queue;
int rear = -1, front = -1;

void copy(element *src, element *dest, int count) {
    for (int i = 0; i < count; i++) {
        dest[i] = src[i];
    }
}

void queueFull() {
    element *newQueue;
    MALLOC(newQueue, 2 * sizeof(element) * size);

    int start = (front + 1) % size;
    if (start < 2) {
        copy(queue + start, newQueue, size - 1);
    } else {
        copy(queue + start, newQueue, size - start);
        copy(queue, newQueue + size - start, rear + 1);
    }

    front = 2 * size - 1;
    rear = size - 2;
    size *= 2;
    free(queue);
    queue = newQueue;
}

void enqueue(element item) {
    rear = (rear + 1) % size;
    if (rear == size) {
        queueFull();
    }
    (queue + rear)->key = item.key;
    printf("%d inserted\n", item.key);
}

element dequeue() {
    element item;
    if (rear == front) {
        printf("Queue is empty\n");
        exit(0);
    }
    front = (front + 1) % size;
    item.key = (queue + front)->key;
    printf("%d deleted\n", item.key);
    return item;
}

void display() {
    int i;
    if (rear == front) {
        printf("Queue is empty\n");
        return;
    }
    printf("The elements in the queue are: ");
    for (i = front; i != rear; i = (i + 1) % size)
        printf("%d ", queue[i + 1].key);
    printf("\n");
}

int main() {
    element item;
    MALLOC(queue, sizeof(element) * size);
    item.key = 10;
    enqueue(item);
    item.key = 20;
    enqueue(item);
    item.key = 30;
    enqueue(item);
    item.key = 40;
    enqueue(item);
    item.key = 50;
    enqueue(item);
    item.key = 10;
    enqueue(item);
    item.key = 20;
    enqueue(item);
    item.key = 30;
    enqueue(item);
    item.key = 40;
    enqueue(item);
    item.key = 50;
    enqueue(item);
    printf("Dequeuing element %d\n", dequeue().key);
    printf("Dequeuing element %d\n", dequeue().key);
    printf("Dequeuing element %d\n", dequeue().key);
    item.key = 40;
    enqueue(item);
    return 0;
}
