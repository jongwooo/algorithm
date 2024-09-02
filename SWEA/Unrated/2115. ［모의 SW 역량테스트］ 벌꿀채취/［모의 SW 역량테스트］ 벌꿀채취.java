import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int N, M, C;
	static int[][] honeys;
	static int maxRevenue;

	public static void main(final String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			C = Integer.parseInt(st.nextToken());
			honeys = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					honeys[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(combination())
					.append("\n");
		}
		System.out.print(sb);
	}

	private static int combination() {
		int result = 0;
		int max1 = 0;
		int max2 = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j <= N - M; j++) {
				maxRevenue = 0;
				dfs(i, j, 0, 0, 0);
				max1 = maxRevenue;
				maxRevenue = 0;
				max2 = 0;
				for (int j2 = j + M; j2 <= N - M; j2++) {
					dfs(i, j2, 0, 0, 0);
					max2 = Math.max(max2, maxRevenue);
				}
				for (int i2 = i + 1; i2 < N; i2++) {
					for (int j2 = 0; j2 <= N - M; j2++) {
						dfs(i2, j2, 0, 0, 0);
						max2 = Math.max(max2, maxRevenue);
					}
				}
				result = Math.max(result, max1 + max2);
			}
		}
		return result;
	}

	private static void dfs(final int i, final int j, final int depth, final int sum, final int revenue) {
		if (sum > C) {
			return;
		}
		if (depth == M) {
			if (maxRevenue < revenue) {
				maxRevenue = revenue;
			}
			return;
		}
		dfs(i, j + 1, depth + 1, sum + honeys[i][j], revenue + honeys[i][j] * honeys[i][j]);
		dfs(i, j + 1, depth + 1, sum, revenue);
	}
}