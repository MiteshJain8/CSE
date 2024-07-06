import java.util.Scanner;

public class BellmanFord {
    public static final int maxVal = 999;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("\nEnter number of vertices: ");
        int V = sc.nextInt();
        int[][] graph = new int[V+1][V+1];
        System.out.println("\nEnter edge weights of graph[i][j], 0 if no edge between i,j: ");
        for(int i=1;i<=V;i++){
            for(int j=1;j<=V;j++){
                graph[i][j] = sc.nextInt();
                if (i == j) {
                    graph[i][j] = 0;
                    continue;
                } else if (graph[i][j] == 0) {
                    graph[i][j] = maxVal;
                }
            }
        }
        System.out.print("\nEnter source vertex: ");
        int src = sc.nextInt();
        Evaluate(graph, src, V);
        sc.close();
    }

    public static void Evaluate(int[][] graph, int src, int V) {
        int[] distance = new int[V+1];
        for (int i = 1; i <= V; i++) {
            distance[i] = maxVal;
        }
        distance[src] = 0;
        for (int i = 1; i <= V-1; i++) {
            for (int u = 1; u <= V; u++) {
                for (int v = 1; v <= V; v++) {
                    if (distance[v] > distance[u] + graph[u][v]) {
                        distance[v] = distance[u] + graph[u][v];
                    }
                }
            }
        }
        for (int u = 1; u <= V; u++) {
            for (int v = 1; v <= V; v++) {
                if (distance[v] > distance[u] + graph[u][v]) {
                    System.out.println("Negative cycle found");
                    return;
                }
            }
        }
        for (int i = 1; i <= V; i++) {
            System.out.println("Distance of vertex " + i + " from source " + src + " is " + distance[i]);
        }
    }
}