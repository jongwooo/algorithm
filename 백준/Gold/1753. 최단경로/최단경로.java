import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	static int V, E;
	static int K;
	static List<Node>[] graph;
	static int[] distance;

	public static void main(final String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		V = Integer.parseInt(st.nextToken());
		E = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(br.readLine());
		graph = new List[V + 1];
		for (int i = 0; i <= V; i++) {
			graph[i] = new ArrayList<>();
		}
		distance = new int[V + 1];
		Arrays.fill(distance, Integer.MAX_VALUE);
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			final int u = Integer.parseInt(st.nextToken());
			final int v = Integer.parseInt(st.nextToken());
			final int w = Integer.parseInt(st.nextToken());
			graph[u].add(new Node(v, w));
		}
		dijkstra(K);
		for (int i = 1; i <= V; i++) {
			final int dist = distance[i];
			if (dist == Integer.MAX_VALUE) {
				sb.append("INF");
			} else {
				sb.append(dist);
			}
			sb.append("\n");
		}
		System.out.print(sb);
	}

	private static void dijkstra(final int start) {
		final PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.add(new Node(start, 0));
		distance[start] = 0;
		while (!pq.isEmpty()) {
			final Node node = pq.poll();
			if (distance[node.index] < node.cost) {
				continue;
			}
			for (final Node next : graph[node.index]) {
				final int newCost = node.cost + next.cost;
				if (newCost < distance[next.index]) {
					distance[next.index] = newCost;
					pq.add(new Node(next.index, newCost));
				}
			}
		}
	}
}

class Node implements Comparable<Node> {

	final int index;
	final int cost;

	public Node(final int index, final int cost) {
		super();
		this.index = index;
		this.cost = cost;
	}

	@Override
	public int compareTo(final Node other) {
		return this.cost - other.cost;
	}
}