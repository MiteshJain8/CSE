import java.util.*;

public class BellmanFord {
    public static final int maxVal = 999;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("\nEnter number of vertices: ");
        int V = sc.nextInt();
        System.out.println("\nEnter edge weights of graph[i][j], 0 if no edge between i,j");
        int[][] graph = new int[V+1][V+1];
        for (int i = 1; i <= V; i++) {
            for (int j = 1; j <= V; j++) {
                graph[i][j] = sc.nextInt();
                if (i == j) {
                    graph[i][j] = 0;
                } else if (graph[i][j] == 0) {
                    graph[i][j] = maxVal;
                }
            }
        }
        System.out.print("\nEnter source vertex:");
        int src = sc.nextInt();
        Evaluate(graph, V, src);
        sc.close();
    }

    public static void Evaluate(int[][] graph,int V,int src) {
        int[] dist = new int[V+1];
        Arrays.fill(dist, maxVal);
        dist[src] = 0;
        for (int i = 1; i <= V-1; i++) {
            for (int u = 1; u <= V; u++) {
                for (int v = 1; v <= V; v++) {
                    if (dist[v] > dist[u] + graph[u][v]) {
                        dist[v] = dist[u] + graph[u][v];
                    }
                }
            }
        }
        for (int u = 1; u <= V; u++) {
            for (int v = 1; v <= V; v++) {
                if (dist[v] > dist[u] + graph[u][v]) {
                    System.out.println("\nGraph contains negative weight cycle");
                    return;
                }
            }
        }
        System.out.println("\nVertex\tDistance from source");
        for (int i = 1; i <= V; i++) {
            System.out.println(i+"\t"+dist[i]);
        }
    }
}