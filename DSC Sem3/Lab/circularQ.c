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
int rear = 0, front = 0;

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
        copy(queue+start, newQueue, size-1);
    } else {
        copy(queue+start, newQueue, size-start);
        copy(queue, newQueue+size-start, rear+1);
    }
    front = 2 * size - 1;
    rear = size - 1;
    size *= 2;
    free(queue);
    queue = newQueue;
}

void enqueue(element item) {
    rear = (rear + 1) % size;
    if (rear == front) {
        queueFull();
    }
    (queue + rear)->key = item.key;
    printf("%d inserted\n", item.key);
}

element dequeue() {
    element item;
    if (rear == front) {
        printf("Queue is empty\n");
        item.key=-1;
        return item;
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
    for (i = (front+1)%size; i != (rear+1)%size; i = (i + 1) % size)
        printf("%d ", queue[i].key);
    printf("\n");
}

int main() {
    element item;
    int choice;
    MALLOC(queue, sizeof(element) * size);
    while (1)
    {
        printf("1.Add\t2.Delete\t3.Display\t4.Exit: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter item to add");
            scanf("%d", &item.key);
            enqueue(item);
            break;
        case 2:
            item = dequeue();
            if (item.key == -1)
                printf("Queue Empty");
            else
                printf("Item deleted: %d", item.key);
            break;
        case 3:
            display();
            break;
        case 4:
            exit(0);
        }
    }
    return 0;
}
