#include <stdio.h>
#include <stdlib.h>

#define MALLOC(p, s) \
if (!((p) = malloc(s))) \
{ \
    fprintf(stderr, "Insufficient memory"); \
    exit(EXIT_FAILURE); \
}

typedef struct listNode *listPointer;
typedef struct listNode {
    int data;
    listPointer link;
}Node;

void insert(listPointer *first, listPointer x)
{//Insert a new node with data 50 after x in the list, *first is the front of the list.
    listPointer temp;
    MALLOC(temp, sizeof(*temp));
    temp->data = 50;
    if (*first)
    {
        temp->link = x->link;
        x->link = temp;
    }
    else
    {
        temp->link = NULL;
        *first = temp;
    }
}

void delete(listPointer *first, listPointer trail, listPointer x)
{ /* delete x from the list, trail is the preceding node and *first is the front of the list */
    if (trail)
        trail->link = x->link;
    else
        *first = (*first)->link;
    free(x);
}

void printList(listPointer first)
{
    printf("The list contains: ");
    for (; first; first=first->link) 
        printf("%4d", first->data);
    printf("\n");
}

int main() {
    listPointer first = NULL;
    listPointer temp = NULL;

    // Insert a node
    insert(&first, temp);
    printList(first);

    // Insert another node
    temp = first;
    insert(&first, temp);
    printList(first);

    // Delete a node
    temp = first;
    delete(&first, NULL, temp);
    printList(first);

    return 0;
}