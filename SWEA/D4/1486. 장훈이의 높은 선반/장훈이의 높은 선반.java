import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int N, B;
	static int[] H;
	static boolean[] visited;
	static int result;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			B = Integer.parseInt(st.nextToken());
			H = new int[N];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				H[i] = Integer.parseInt(st.nextToken());
			}
			visited = new boolean[N];
			result = Integer.MAX_VALUE;
			dfs(0, 0);
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(result - B)
					.append("\n");
		}
		System.out.println(sb);
	}

	private static void dfs(final int depth, final int heights) {
		if (heights >= B) {
			if (heights < result) {
				result = heights;
			}
			return;
		}
		if (depth == N) {
			return;
		}
		visited[depth] = true;
		dfs(depth + 1, heights + H[depth]);
		visited[depth] = false;
		dfs(depth + 1, heights);
	}
}
