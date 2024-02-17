#include <stdlib.h>
#define MALLOC(x, size, type) (x = (type *)malloc(size * sizeof(type)))
typedef struct
{
    int n;
} element;
int front = 0, rear = 0, capacity;
element *queue;
void copy(element *start, element *end, element *newQueue)
{
    element *j;
    element *i;
    i = newQueue;
    j = start;
    for (; j < end; j++, i++)
    {
        *i = *j;
    }
}
void queueFull()
{
    element *newQueue;
    MALLOC(newQueue, capacity * 2, element);
    int start = (front + 1) % capacity;
    if (start < 2) // either 1 or 0, 1 when front at 0, 0 when front at capacity - 1
        copy(queue+start, queue+start+capacity-1, newQueue);
    else
    {
        copy(queue+start, queue+capacity, newQueue);
        copy(queue, queue+rear+1, newQueue+capacity-start);
    }
    front = 2 * capacity - 1;
    rear = capacity - 1;
    capacity *= 2;
    free(queue);
    queue = newQueue;
}
void addq(element item)
{
    rear = (rear + 1) % capacity;
    if (front == rear)
        queueFull();
    queue[rear] = item;
}
element deleteq()
{
    element item;
    if (front == rear)
    {
        item.n = -1;
        return item;
    }
    front = (front + 1) % capacity;
    return queue[front];
}

void displayq()
{
    int i;
    if (front == rear)
    {
        printf("Queue Empty\n");
        return;
    }

    for (i = (front + 1) % capacity; i != rear; i = (i + 1) % capacity)
        printf("%d\t", queue[i].n);
    printf("%d", queue[i].n);
    printf("\n");
    // printf("Front: %d Rear: %d\n", front, rear);
}
void main()
{
    int choice;
    element item;
    printf("Enter intial size");
    scanf("%d", &capacity);
    MALLOC(queue, capacity, element);
    while (1)
    {
        printf("1.Add\t2.Delete\t3.Display\t4.Exit");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter item to add");
            scanf("%d", &item.n);
            addq(item);
            break;
        case 2:
            item = deleteq();
            if (item.n == -1)
                printf("Queue Empty");
            else
                printf("Item deleted: %d", item.n);
            break;
        case 3:
            displayq();
            break;
        case 4:
            exit(0);
        }
    }
}