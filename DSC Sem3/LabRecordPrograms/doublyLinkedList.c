#include <stdio.h>
#include <stdlib.h>

#define MALLOC(p, s) \
if (!((p) = malloc(s))) \
{ \
    fprintf(stderr, "Insufficient memory"); \
    exit(EXIT_FAILURE); \
}

typedef struct node *nodePtr;
typedef struct node
{
    nodePtr llink;
    int data;
    nodePtr rlink;
}node;

nodePtr head = NULL;

void insertAfter(nodePtr node, int data)
{
    nodePtr newnode;
    MALLOC(newnode, sizeof(*newnode));
    if(node->llink == node)
        node->llink = newnode;
    newnode->llink = node;
    newnode->rlink = node->rlink;
    node->rlink->llink = newnode;
    node->rlink = newnode;
    newnode->data = data;
}

void delete(nodePtr node)
{
    if(node == head) {
        printf("\nHead node cannot be deleted");
    } else {
    node->llink->rlink = node->rlink;
    node->rlink->llink = node->llink;
    printf("\n%d deleted",node->data);
    free(node);
    }
}

void print() {
    nodePtr node = head->rlink;
    printf("\nThe list is: ");
    while (node != head) {
        printf("%d ", node->data);
        node = node->rlink;
    }
}

int main() {
    nodePtr node;
    MALLOC(node, sizeof(*node));
    head = node;
    node->llink = node;
    node->rlink = node;
    insertAfter(node, 10);
    insertAfter(node->rlink, 20);
    insertAfter(node->llink, 30);  
    insertAfter(node->llink, 40);
    print();
    delete(node);
    delete(node->llink);
    delete(node->rlink);
    print();
}