import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int[][] W;
	static boolean[] visited;
	static int result;

	public static void main(final String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		N = Integer.parseInt(br.readLine());
		W = new int[N + 1][N + 1];
		StringTokenizer st;
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				W[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		visited = new boolean[N + 1];
		result = Integer.MAX_VALUE;
		tsp(1, 1, 0);
		System.out.print(result);
	}

	private static void tsp(final int depth, final int start, final int cost) {
		if (depth == N && W[start][1] != 0) {
			if (cost + W[start][1] < result) {
				result = cost + W[start][1];
			}
			return;
		}
		for (int i = 2; i <= N; i++) {
			if (!visited[i] && W[start][i] != 0) {
				visited[i] = true;
				tsp(depth + 1, i, cost + W[start][i]);
				visited[i] = false;
			}
		}
	}
}