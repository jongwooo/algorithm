import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	static int N;
	static long[] X, Y;
	static int[] parent;
	static double E;
	static Edge[] edges;

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("input.txt"));
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			N = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			X = new long[N];
			for (int i = 0; i < N; i++) {
				X[i] = Long.parseLong(st.nextToken());
			}
			st = new StringTokenizer(br.readLine());
			Y = new long[N];
			for (int i = 0; i < N; i++) {
				Y[i] = Long.parseLong(st.nextToken());
			}
			E = Double.parseDouble(br.readLine());
			parent = new int[N];
			for (int i = 0; i < N; i++) {
				parent[i] = i;
			}
			edges = new Edge[N * (N - 1) / 2];
			int index = 0;
			for (int i = 0; i < N - 1; i++) {
				for (int j = i + 1; j < N; j++) {
					final long L = (X[i] - X[j]) * (X[i] - X[j]) + (Y[i] - Y[j]) * (Y[i] - Y[j]);
					edges[index++] = new Edge(i, j, L);
				}
			}
			Arrays.sort(edges);
			double result = 0.0;
			for (final Edge edge : edges) {
				if (find(edge.from) != find(edge.to)) {
					union(edge.from, edge.to);
					result += edge.cost;
				}
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(Math.round(result * E))
					.append("\n");
		}
		System.out.println(sb);
	}

	private static int find(final int x) {
		if (parent[x] == x) {
			return x;
		}
		return parent[x] = find(parent[x]);
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

	final int from, to;
	final long cost;

	public Edge(final int from, final int to, final long cost) {
		super();
		this.from = from;
		this.to = to;
		this.cost = cost;
	}

	@Override
	public int compareTo(final Edge other) {
		return Long.compare(this.cost, other.cost);
	}
}
