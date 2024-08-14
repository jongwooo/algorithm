import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int[][] prefixSum;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			final int N = Integer.parseInt(st.nextToken());
			final int M = Integer.parseInt(st.nextToken());
			prefixSum = new int[N + 1][N + 1];
			for (int i = 1; i <= N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 1; j <= N; j++) {
					prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1]
							+ Integer.parseInt(st.nextToken());
				}
			}
			int result = 0;
			for (int i = M; i <= N; i++) {
				for (int j = M; j <= N; j++) {
					final int kill = prefixSum[i][j] - prefixSum[i][j - M] - prefixSum[i - M][j]
							+ prefixSum[i - M][j - M];
					if (result < kill) {
						result = kill;
					}
				}
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(result)
					.append("\n");
		}
		System.out.println(sb);
	}
}
