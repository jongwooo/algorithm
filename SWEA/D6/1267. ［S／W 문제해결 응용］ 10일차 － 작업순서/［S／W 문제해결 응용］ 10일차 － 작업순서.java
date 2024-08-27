import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

	static int V, E;
	static int[] indegree;
	static List<Integer>[] graph;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		for (int testCase = 1; testCase <= 10; testCase++) {
			st = new StringTokenizer(br.readLine());
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			indegree = new int[V + 1];
			graph = new List[V + 1];
			for (int i = 0; i < V + 1; i++) {
				graph[i] = new LinkedList<>();
			}
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < E; i++) {
				final int a = Integer.parseInt(st.nextToken());
				final int b = Integer.parseInt(st.nextToken());
				graph[a].add(b);
				indegree[b]++;
			}
			final List<Integer> result = topologySort();
			sb.append("#")
					.append(testCase);
			for (final int node : result) {
				sb.append(" ")
						.append(node);
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

	private static List<Integer> topologySort() {
		final List<Integer> result = new LinkedList<>();
		final Queue<Integer> queue = new ArrayDeque<>();
		for (int i = 1; i < V + 1; i++) {
			if (indegree[i] == 0) {
				queue.add(i);
			}
		}
		while (!queue.isEmpty()) {
			final int now = queue.poll();
			result.add(now);
			for (final int next : graph[now]) {
				indegree[next]--;
				if (indegree[next] == 0) {
					queue.add(next);
				}
			}
		}
		return result;
	}
}