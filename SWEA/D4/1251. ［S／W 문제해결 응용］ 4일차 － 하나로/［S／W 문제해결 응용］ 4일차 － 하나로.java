import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {

	static int N;
	static long[] X, Y;
	static double E;
	static List<Edge>[] edges;
	static long result;

	public static void main(String[] args) throws Exception {
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
			edges = new List[N];
			int index = 0;
			for (int i = 0; i < N; i++) {
				edges[i] = new ArrayList<>();
				for (int j = 0; j < N; j++) {
					final long L = (X[i] - X[j]) * (X[i] - X[j]) + (Y[i] - Y[j]) * (Y[i] - Y[j]);
					edges[i].add(new Edge(j, L));
				}
			}
			result = 0;
			prim();
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(Math.round(result * E))
					.append("\n");
		}
		System.out.println(sb);
	}

	private static void prim() {
		final PriorityQueue<Edge> pq = new PriorityQueue<>();
		final boolean[] visited = new boolean[N];
		int count = 0;
		pq.add(new Edge(0, 0));
		while (!pq.isEmpty()) {
			final Edge edge = pq.poll();
			if (visited[edge.v]) {
				continue;
			}
			result += edge.weight;
			visited[edge.v] = true;
			if (++count == N) {
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
	final long weight;

	public Edge(final int v, final long weight) {
		super();
		this.v = v;
		this.weight = weight;
	}

	@Override
	public int compareTo(final Edge other) {
		return Long.compare(this.weight, other.weight);
	}
}