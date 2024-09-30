import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static BufferedReader br;
	static StringBuilder sb;
	static StringTokenizer st;

	static int T;
	static int N, K;
	static int[] w, v;
	static int[][] dp;

	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			w = new int[N + 1];
			v = new int[N + 1];
			for (int i = 1; i <= N; i++) {
				st = new StringTokenizer(br.readLine());
				w[i] = Integer.parseInt(st.nextToken());
				v[i] = Integer.parseInt(st.nextToken());
			}
			dp = new int[K + 1][N + 1];
			for (int i = 1; i <= K; i++) {
				for (int j = 1; j <= N; j++) {
					if (w[j] <= i) {
						dp[i][j] = Math.max(dp[i][j - 1], dp[i - w[j]][j - 1] + v[j]);
					} else {
						dp[i][j] = dp[i][j - 1];
					}
				}
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(dp[K][N])
					.append("\n");
		}
		System.out.println(sb);
	}
}