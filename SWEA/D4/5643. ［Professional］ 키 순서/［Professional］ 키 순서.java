import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution {

	static final int INF = (int) 1e9;

	static int N;
	static int M;
	static int[][] map;
	static int[] count;
	static int result;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			N = Integer.parseInt(br.readLine());
			M = Integer.parseInt(br.readLine());
			map = new int[N][N];
			for (int i = 0; i < N; i++) {
				Arrays.fill(map[i], INF);
			}
			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				final int a = Integer.parseInt(st.nextToken()) - 1;
				final int b = Integer.parseInt(st.nextToken()) - 1;
				map[a][b] = 1;
			}
			for (int k = 0; k < N; k++) {
				for (int a = 0; a < N; a++) {
					if (k == a) {
						continue;
					}
					for (int b = 0; b < N; b++) {
						if (a == b || b == k) {
							continue;
						}
						if (map[a][k] + map[k][b] < map[a][b]) {
							map[a][b] = map[a][k] + map[k][b];
						}
					}
				}
			}
			result = 0;
			count = new int[N];
			for (int a = 0; a < N; a++) {
				for (int b = 0; b < N; b++) {
					if (map[a][b] != INF || map[b][a] != INF) {
						count[a]++;
					}
				}
			}
			for (int i = 0; i < N; i++) {
				if (count[i] == N - 1) {
					result++;
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