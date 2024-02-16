#include <stdio.h>
#include <stdlib.h>
struct node
{
	int vertex;
	struct node *next;
};

struct node *createNode(int v);

struct Graph
{
	int totalVertices;
	int *visited;
	struct node **adjLists;
};

void DFS(struct Graph *graph, int vertex)
{
	struct node *adjList = graph->adjLists[vertex];
	struct node *temp = adjList;
	graph->visited[vertex] = 1;
	printf("%d -> ", vertex);
	while (temp != NULL)
	{
		int connectedVertex = temp->vertex;
		if (graph->visited[connectedVertex] == 0)
		{
			DFS(graph, connectedVertex);
		}
		temp = temp->next;
	}
}

struct node *createNode(int v)
{
	struct node *newNode = malloc(sizeof(struct node));
	newNode->vertex = v;
	newNode->next = NULL;
	return newNode;
}
struct Graph *createGraph(int vertices)
{
	struct Graph *graph = malloc(sizeof(struct Graph));
	graph->totalVertices = vertices;
	graph->adjLists = malloc(vertices * sizeof(struct node *));
	graph->visited = malloc(vertices * sizeof(int));
	int i;
	for (i = 0; i < vertices; i++)
	{
		graph->adjLists[i] = NULL;
		graph->visited[i] = 0;
	}
	return graph;
}
void addEdge(struct Graph *graph, int src, int dest)
{
	struct node *newNode = createNode(dest);
	newNode->next = graph->adjLists[src];
	graph->adjLists[src] = newNode;
	newNode = createNode(src);
	newNode->next = graph->adjLists[dest];
	graph->adjLists[dest] = newNode;
}
void displayGraph(struct Graph *graph)
{
	int v;
	for (v = 1; v < graph->totalVertices; v++)
	{
		struct node *temp = graph->adjLists[v];
		printf("\n%d =>  ", v);
		while (temp)
		{
			printf("%d, ", temp->vertex);
			temp = temp->next;
		}
		printf("\n");
	}
	printf("\n");
}
int main()
{
	struct Graph *graph = createGraph(8);
	addEdge(graph, 1, 2);
	addEdge(graph, 1, 3);
	addEdge(graph, 2, 5);
	addEdge(graph, 2, 4);
	addEdge(graph, 4, 8);
	addEdge(graph, 5, 8);
	addEdge(graph, 3, 6);
	addEdge(graph, 3, 7);
	addEdge(graph, 6, 8);
	addEdge(graph, 7, 8);
	printf("\nThe Adjacency List of the Graph is:");
	displayGraph(graph);
	printf("\nDFS traversal of the graph: \n");
	DFS(graph, 1);
	return 0;
}
