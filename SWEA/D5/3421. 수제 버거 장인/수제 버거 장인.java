import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int N, M;
	static boolean[][] impossible;
	static boolean[] visited;
	static int[] selected;
	static int result;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			impossible = new boolean[N + 1][N + 1];
			visited = new boolean[N + 1];
			selected = new int[N + 1];
			result = 0;
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				final int a = Integer.parseInt(st.nextToken());
				final int b = Integer.parseInt(st.nextToken());
				impossible[a][b] = true;
				impossible[b][a] = true;
			}
			dfs(0, 0);
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(result)
					.append("\n");
		}
		System.out.println(sb);
	}

	private static boolean isPossible(final int depth, final int target) {
		for (int i = 0; i <= depth; i++) {
			if (impossible[target][selected[i]])
				return false;
		}
		return true;
	}

	private static void dfs(final int depth, final int index) {
		result++;
		for (int i = index; i < N; i++) {
			if (visited[i]) {
				continue;
			}
			if (!isPossible(depth, i + 1)) {
				continue;
			}
			visited[i] = true;
			selected[depth] = i + 1;
			dfs(depth + 1, i);
			visited[i] = false;
			selected[depth] = 0;
		}
	}
}
