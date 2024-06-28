import java.util.Scanner;

public class BellmanFord {
    private int[] distances;
    private int numVertices;
    public static final int MAX_VALUE = 999;

    public BellmanFord(int numVertices) {
        this.numVertices = numVertices;
        distances = new int[numVertices + 1];
    }

    public void evaluate(int source, int[][] graph) {
        // Initialize distances
        for (int i = 1; i <= numVertices; i++) {
            distances[i] = MAX_VALUE;
        }
        distances[source] = 0;

        // Relax edges |V| - 1 times
        for (int i = 1; i <= numVertices - 1; i++) {
            for (int u = 1; u <= numVertices; u++) {
                for (int v = 1; v <= numVertices; v++) {
                    if (graph[u][v] != MAX_VALUE && distances[u] != MAX_VALUE && distances[u] + graph[u][v] < distances[v]) {
                        distances[v] = distances[u] + graph[u][v];
                    }
                }
            }
        }

        // Check for negative-weight cycles
        for (int u = 1; u <= numVertices; u++) {
            for (int v = 1; v <= numVertices; v++) {
                if (graph[u][v] != MAX_VALUE && distances[u] != MAX_VALUE && distances[u] + graph[u][v] < distances[v]) {
                    System.out.println("The Graph contains a negative edge cycle");
                    return;
                }
            }
        }

        // Print distances
        for (int i = 1; i <= numVertices; i++) {
            System.out.println("Distance from source " + source + " to " + i + " is " + distances[i]);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of vertices");
        int numVertices = scanner.nextInt();

        int[][] graph = new int[numVertices + 1][numVertices + 1];
        System.out.println("Enter the adjacency matrix");
        for (int i = 1; i <= numVertices; i++) {
            for (int j = 1; j <= numVertices; j++) {
                graph[i][j] = scanner.nextInt();
                if (i == j) {
                    graph[i][j] = 0;
                } else if (graph[i][j] == 0) {
                    graph[i][j] = MAX_VALUE;
                }
            }
        }

        System.out.println("Enter the source vertex");
        int source = scanner.nextInt();
        
        BellmanFord bellmanFord = new BellmanFord(numVertices);
        bellmanFord.evaluate(source, graph);
        
        scanner.close();
    }
}