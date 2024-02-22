#include <stdio.h>
#include <stdlib.h>
#define MAX 200
typedef struct node
{
    struct node *next;
    int vertex;
} node;

int visited[MAX];
node *G[20]; // heads of the linked list
int n;

void insert(int vi, int vj)
{
    node *p, *q;
    // acquire memory for the new node
    q = (node *)malloc(sizeof(node));
    q->vertex = vj;
    q->next = NULL;
    // insert the node in the linked list for the vertex no. vi
    if (G[vi] == NULL)
        G[vi] = q;
    else
    {
        // go to the end of linked list
        p = G[vi];
        while (p->next != NULL)
            p = p->next;
        p->next = q;
    }
}

void readgraph()
{
    int i, vi, vj, no_of_edges;
    printf("\nEnter no. of vertices :");
    scanf("%d", &n);
    // initialize G[] with NULL
    for (i = 0; i < n; i++)
        G[i] = NULL;
    // read edges and insert them in G[]
    printf("\nEnter no of edges :");
    scanf("%d", &no_of_edges);
    for (i = 0; i < no_of_edges; i++)
    {
        printf("\nEnter an edge (u,v) :");
        scanf("%d%d", &vi, &vj);
        insert(vi, vj);
        insert(vj, vi);
    }
}

void DFS(int i)
{
    node *p;
    visited[i] = 1;
    printf("\n%d", i);
    for (p = G[i]; p; p = p->next)
        if (!visited[p->vertex])
            DFS(p->vertex);
}

void BFS(int i)
{
    int queue[MAX], front = -1, rear = -1, vertex;
    node *p;

    visited[i] = 1;
    printf("\n%d", i);
    queue[++rear] = i;

    while (front != rear)
    {
        vertex = queue[++front];
        for (p = G[vertex]; p; p = p->next)
        {
            if (!visited[p->vertex])
            {
                visited[p->vertex] = 1;
                printf("\n%d", p->vertex);
                queue[++rear] = p->vertex;
            }
        }
    }
}

int main()
{
    int i, op;
    do
    {
        printf("\n1)Create\t2)DFS\t3)BFS\t4)Quit: ");
        scanf("%d", &op);
        switch (op)
        {
        case 1:
            readgraph();
            break;
        case 2:
            for (i = 0; i < n; i++)
                visited[i] = 0;
            printf("\nStarting Node No. : ");
            scanf("%d", &i);
            DFS(i);
            break;
        case 3:
            for (i = 0; i < n; i++)
                visited[i] = 0;
            printf("\nStarting Node No. : ");
            scanf("%d", &i);
            BFS(i);
            break;
        }
    } while (op != 4);
}