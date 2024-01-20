#define size 5
#include<stdio.h>
#include<stdlib.h>

typedef struct element {
    int key;
}element;

element *queue;
int rear = -1, front = -1;

void enqueue(element item) {
    if((rear+1)%size == front) {
        printf("Queue is full\n");
        return;
    }
    rear = (rear+1)%size;
    queue[rear] = item;
    printf("%d inserted\n", item.key);
    if(front == -1)
        front = 0;
}

element dequeue() {
    element item;
    if (rear == -1) {
        printf("Queue is empty\n");
        item.key = -1;
        return item;
    } else if (front == rear) {
        item = queue[front];
        front = rear = -1;
        return item;
    }
    item = queue[front];
    front = (front+1)%size;
    return item;
}

void display() {
    int i;
    if(rear == -1) {
        printf("Queue is empty\n");
        return;
    }
    printf("The elements in the queue are: ");
    for(i=front-1;i!=rear;i=(i+1)%size)
        printf("%d ",queue[i+1].key);
    printf("\n");
}

int main() {
    int choice;
    element item;
    queue = (element *)malloc(sizeof(element)*size);
    printf("1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\n");
    do {
        printf("Enter your choice: ");
        scanf("%d",&choice);
        switch(choice) {
            case 1:
                printf("Enter the element to be inserted: ");
                scanf("%d",&item.key);
                enqueue(item);
                break;
            case 2:
                item = dequeue();
                if(!(item.key == -1))
                    printf("The element deleted is %d\n",item.key);
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
                break;
            default:
                printf("Invalid choice\n");
                break;
        }
        printf("\nDo you want to continue? (1=Yes/0=No): ");
        scanf("%d",&choice);
    }while(choice);
    return 0;
}