#include <stdio.h>
#include <stdlib.h>

// Structure for a node
typedef struct Node {
    int data;
    struct Node* link;
}Node;

Node* head = NULL; // Global variable

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed!");
        exit(1);
    }
    newNode->data = data;
    newNode->link = NULL;
    return newNode;
}

// Function to add an element at the front of the linked list
void addFront(int data) {
    Node* newNode = createNode(data);
    newNode->link = head;
    head = newNode;
    printf("%d added at the front.\n", data);
}

// Function to remove an element from the rear of the linked list
void removeRear() {
    if (head == NULL) {
        printf("List is empty!\n");
        exit(1);
    }
    Node* temp = head;
    Node* prev = NULL;
    while (temp->link != NULL) {
        prev = temp;
        temp = temp->link;
    }
    if (prev != NULL) {
        prev->link = NULL;
    } else {
        head = NULL;
    }
    printf("%d removed from the rear.\n", temp->data);
    free(temp);
}

// Function to print the linked list
void printList() {
    if (head == NULL) {
        printf("List is empty!\n");
        return;
    }
    Node* temp = head;
    printf("List: ");
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->link;
    }
    printf("\n");
}

int main() {
    addFront(10);
    addFront(20);
    addFront(30);
    addFront(40);

    printList();

    removeRear();
    removeRear();

    printList();

    return 0;
}
