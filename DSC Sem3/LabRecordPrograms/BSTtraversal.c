#include <stdio.h>
#include <stdlib.h>

typedef struct node *tree_pointer; 
typedef struct node { 
 int data; 
 tree_pointer left_child, right_child; 
}node;

void inorder(tree_pointer ptr) 
/* inorder tree traversal */ 
{ 
    if (ptr) { 
        inorder(ptr->left_child); 
        printf("%d ", ptr->data); 
        inorder(ptr->right_child); 
    } 
}

void preorder(tree_pointer ptr) 
/* preorder tree traversal */ 
{ 
    if (ptr) { 
        printf("%d ", ptr->data); 
        preorder(ptr->left_child); 
        preorder(ptr->right_child); 
    } 
}

void postorder(tree_pointer ptr) 
/* postorder tree traversal */ 
{ 
    if (ptr) { 
        postorder(ptr->left_child); 
        postorder(ptr->right_child); 
        printf("%d ", ptr->data); 
    } 
}

int main() {
    struct node root, left, right;

    root.data = 1;
    left.data = 2;
    right.data = 3;

    root.left_child = &left;
    root.right_child = &right;

    left.left_child = NULL;
    left.right_child = NULL;

    right.left_child = NULL;
    right.right_child = NULL;

    printf("Inorder traversal: ");
    inorder(&root);
    printf("\n");

    printf("Preorder traversal: ");
    preorder(&root);
    printf("\n");

    printf("Postorder traversal: ");
    postorder(&root);
    printf("\n");

    return 0;
}
