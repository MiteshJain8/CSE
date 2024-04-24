#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 10

int heap[MAX_SIZE];
void insert(int item, int *n)
{
    int i;
    if ((*n) == MAX_SIZE - 1)
    {
        printf("Heap Full\n");
        return;
    }
    i = ++(*n);
    while (i != 1 && item > heap[i / 2])
    {
        heap[i] = heap[i / 2];
        i /= 2;
    }
    heap[i] = item;
}
int deleteHeap(int *n)
{
    int parent=1, child=2;
    int temp, item;
    if (*n == 0)
    {
        printf("Heap Empty\n");
        item = -1;
        return item;
    }
    item = heap[1];
    temp = heap[(*n)--];
    while (child <= *n)
    {
        if (child < *n && heap[child] < heap[child + 1])
            child++;
        if (temp >= heap[child])
            break;
        heap[parent] = heap[child];
        parent = child;
        child = child * 2;
    }
    heap[parent] = temp;
    return item;
}
void display(int n)
{
    int i;
    for (i = 1; i <= n; i++)
    {
        printf("%d\n", heap[i]);
    }
}
int main()
{
    int choice, n = 0;
    int item;
    while (1)
    {
        printf("Enter\t1.Insert\t2.Display\t3.Delete\t4.Exit: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter element to insert: ");
            scanf("%d", &item);
            insert(item, &n);
            break;
        case 2:
            display(n);
            break;
        case 3:
            item = deleteHeap(&n);
            if (item != -1)
                printf("Element Deleted: %d\n", item);
            break;
        case 4:
            exit(0);
        }
    }
}