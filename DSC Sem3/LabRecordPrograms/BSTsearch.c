#include <stdio.h>
#include <stdlib.h>

#define MALLOC(p, s) \
if (!((p) = malloc(s))) \
{ \
    fprintf(stderr, "Insufficient memory"); \
    exit(EXIT_FAILURE); \
}

typedef struct node *tree_pointer;
typedef struct node
{
    int data;
    tree_pointer left_child, right_child;
} node;

tree_pointer search(tree_pointer root, int key)
{
    /* return a pointer to the node that contains key. If there is no such
    node, return NULL */
    if (!root)
        return NULL;
    if (key == root->data)
        return root;
    if (key < root->data)
        return search(root->left_child,key);
    return search(root->right_child, key);
}

void insert_node(tree_pointer *node, int num)
{
    tree_pointer ptr, temp = search(*node, num);
    if (temp || !(*node))
    {
        MALLOC(ptr,sizeof(node))
        // ptr = (tree_pointer)malloc(sizeof(node));
        // if (IS_FULL(ptr))
        // {
        //     fprintf(stderr, "The memory is full\n");
        //     exit(1);
        // }
        ptr->data = num;
        ptr->left_child = ptr->right_child = NULL;
        if (*node)
            if (num < temp->data)
                temp->left_child = ptr;
            else
                temp->right_child = ptr;
        else
            *node = ptr;
    }
}

int main()
{
    tree_pointer root = NULL;
    insert_node(&root, 10);
    insert_node(&root, 5);
    insert_node(&root, 15);

    tree_pointer result1 = search(root, 10);
    if (result1) {
        printf("Found node with data: %d\n", result1->data);
    } else {
        printf("Node not found\n");
    }

    tree_pointer result2 = search(root, 15);
    if (result2) {
        printf("Found node with data: %d\n", result2->data);
    } else {
        printf("Node not found\n");
    }

    return 0;
}
