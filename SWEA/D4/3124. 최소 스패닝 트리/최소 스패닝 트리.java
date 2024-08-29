import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	static int V, E;
	static Edge[] edges;
	static int[] parent;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			edges = new Edge[E];
			for (int i = 0; i < E; i++) {
				st = new StringTokenizer(br.readLine());
				final int A = Integer.parseInt(st.nextToken());
				final int B = Integer.parseInt(st.nextToken());
				final int C = Integer.parseInt(st.nextToken());
				edges[i] = new Edge(A, B, C);
			}
			parent = new int[V + 1];
			for (int i = 1; i <= V; i++) {
				parent[i] = i;
			}
			Arrays.sort(edges);
			int count = 0;
			long result = 0;
			for (final Edge edge : edges) {
				if (find(edge.from) != find(edge.to)) {
					union(edge.from, edge.to);
					result += edge.weight;
					count++;
					if (count == V - 1) {
						break;
					}
				}
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(result)
					.append("\n");
		}
		System.out.print(sb);
	}

	private static int find(final int x) {
		if (parent[x] != x) {
			parent[x] = find(parent[x]);
		}
		return parent[x];
	}

	private static void union(int a, int b) {
		a = find(a);
		b = find(b);
		if (a < b) {
			parent[b] = a;
		} else {
			parent[a] = b;
		}
	}
}

class Edge implements Comparable<Edge> {

	final int from;
	final int to;
	final int weight;

	public Edge(final int from, final int to, final int weight) {
		this.from = from;
		this.to = to;
		this.weight = weight;
	}

	@Override
	public int compareTo(final Edge other) {
		return this.weight - other.weight;
	}
}