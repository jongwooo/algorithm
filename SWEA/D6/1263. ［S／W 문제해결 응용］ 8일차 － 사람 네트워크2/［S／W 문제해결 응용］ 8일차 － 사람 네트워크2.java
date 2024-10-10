import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	static BufferedReader br;
	static StringBuilder sb;
	static StringTokenizer st;

	static final int INF = (int) 1e9;

	static int N;
	static int[][] graph;

	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			graph = new int[N][N];
			for (int i = 0; i < N; i++) {
				Arrays.fill(graph[i], INF);
			}
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					final int n = Integer.parseInt(st.nextToken());
					if (n != 0) {
						graph[i][j] = n;
					}
					if (i == j) {
						graph[i][j] = 0;
					}
				}
			}
			for (int k = 0; k < N; k++) {
				for (int a = 0; a < N; a++) {
					if (k == a) {
						continue;
					}
					for (int b = 0; b < N; b++) {
						if (k == a || k == b) {
							continue;
						}
						graph[a][b] = Math.min(graph[a][b], graph[a][k] + graph[k][b]);
					}
				}
			}
			int minCC = INF;
			for (int i = 0; i < N; i++) {
				int sum = 0;
				for (int j = 0; j < N; j++) {
					sum += graph[i][j];
				}
				minCC = Math.min(minCC, sum);
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(minCC)
					.append("\n");
		}
		System.out.println(sb);
	}
}