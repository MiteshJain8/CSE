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

tree_pointer newNode(int item){
        tree_pointer temp = (tree_pointer) malloc(sizeof(node));
        temp->data = item;
        temp->left_child = temp->right_child = NULL;
        return temp;
}

tree_pointer insert(tree_pointer node , int key){
        if(node==NULL){
                return newNode(key);
        }
        else if(key<node->data)
                node->left_child = insert(node->left_child, key);
        else if(key<node->data)
                node->left_child = insert(node->left_child, key);
        else if(key>node->data)
                node->right_child = insert(node->right_child , key);
}
int main(){
        tree_pointer root = NULL;
        root= insert(root,50);
        insert(root,20);
        insert(root,40);
        insert(root,3000);
        insert(root, 1);
        insert(root,25);
        printf("pre:");

        preorder(root);
        printf("\npost: ");

        postorder(root);
        printf("\nin: ");

        inorder(root);
        return 0;
}