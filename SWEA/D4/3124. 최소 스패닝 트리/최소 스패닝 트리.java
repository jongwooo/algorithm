import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {

	static int V, E;
	static List<Edge>[] edges;
	static long result;

	public static void main(final String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			edges = new List[V + 1];
			for (int i = 0; i <= V; i++) {
				edges[i] = new ArrayList<>();
			}
			for (int i = 0; i < E; i++) {
				st = new StringTokenizer(br.readLine());
				final int A = Integer.parseInt(st.nextToken());
				final int B = Integer.parseInt(st.nextToken());
				final int C = Integer.parseInt(st.nextToken());
				edges[A].add(new Edge(B, C));
				edges[B].add(new Edge(A, C));
			}
			result = 0;
			prim();
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(result)
					.append("\n");
		}
		System.out.print(sb);
	}

	private static void prim() {
		final PriorityQueue<Edge> pq = new PriorityQueue<>();
		final boolean[] visited = new boolean[V + 1];
		int count = 0;
		pq.add(new Edge(1, 0));
		while (!pq.isEmpty()) {
			final Edge edge = pq.poll();
			if (visited[edge.v]) {
				continue;
			}
			result += edge.weight;
			visited[edge.v] = true;
			if (++count == V) {
				break;
			}
			for (final Edge next : edges[edge.v]) {
				if (!visited[next.v]) {
					pq.add(next);
				}
			}
		}
	}
}

class Edge implements Comparable<Edge> {

	final int v;
	final int weight;

	public Edge(final int v, final int weight) {
		this.v = v;
		this.weight = weight;
	}

	@Override
	public int compareTo(final Edge other) {
		return weight - other.weight;
	}
}