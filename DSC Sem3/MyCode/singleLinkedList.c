#include<stdio.h>
#include<stdlib.h>

typedef struct listnode *lp;
typedef struct listnode
{
    int data;
    lp link;
}Node;

void main()
{
    lp n1,n2;
    n1=(Node*)malloc(sizeof(Node));
    n2=(Node*)malloc(sizeof(Node));
    printf("enter the data of node\n");
    scanf("%d",&(n1->data));
    printf("enter the data of node\n");
    scanf("%d",&(n2->data));
    n1->link = n2;
    n2->link = NULL;
    printf("%d->",n1->data);
    printf("%d",n2->data);
}