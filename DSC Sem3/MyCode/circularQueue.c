#include<stdio.h>
#include<stdlib.h>

int size=3;

#define MALLOC(p, s) \
if (!((p) = malloc(s))) \
{ \
    fprintf(stderr, "Insufficient memory"); \
    exit(EXIT_FAILURE); \
}

int *queue;
int rear = 0, front = 0;

void copy(int *src, int *dest, int count) {
    for (int i = 0; i < count; i++) {
        dest[i] = src[i];
    }
}

void queueFull() {
    int *newQueue;
    MALLOC(newQueue, 2 * sizeof(int) * size);
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

void enqueue(int item) {
    rear = (rear + 1) % size;
    if (rear == front) {
        queueFull();
    }
    queue[rear] = item;
    printf("%d inserted\n", item);
}

int dequeue() {
    int item;
    if (rear == front) {
        printf("Queue is empty\n");
        item=-1;
        return item;
    }
    front = (front + 1) % size;
    item = queue[front];
    printf("%d deleted\n", item);
    return item;
}

void display() {
    int i;
    if (rear == front) {
        printf("Queue is empty\n");
        return;
    }
    printf("The ints in the queue are: ");
    for (i = (front+1)%size; i != (rear+1)%size; i = (i + 1) % size)
        printf("%d ", queue[i]);
    printf("\n");
}

int main() {
    int item;
    int choice;
    MALLOC(queue, sizeof(int) * size);
    while (1)
    {
        printf("1.Add\t2.Delete\t3.Display\t4.Exit: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter item to add");
            scanf("%d", &item);
            enqueue(item);
            break;
        case 2:
            item = dequeue();
            if (item == -1)
                printf("Queue Empty");
            else
                printf("Item deleted: %d", item);
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
