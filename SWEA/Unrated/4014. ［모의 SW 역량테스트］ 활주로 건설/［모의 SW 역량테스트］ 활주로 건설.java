import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static BufferedReader br;
	static StringBuilder sb;
	static StringTokenizer st;

	static int N, X;
	static int[][] grid;
	static int count;

	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			X = Integer.parseInt(st.nextToken());
			grid = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					grid[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			count = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (i == 0) {
						rowSearch(i, j);
					}
					if (j == 0) {
						colSearch(i, j);
					}
				}
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(count)
					.append("\n");
		}
		System.out.println(sb);
	}

	private static void rowSearch(final int r, final int c) {
		int length = 1;
		int height = grid[r][c];
		for (int i = 1; i < N; i++) {
			if (height - grid[i][c] == 0) {
				length++;
			} else if (height - grid[i][c] == 1) {
				if (N - i < X) {
					return;
				}
				for (int j = 1; j < X; j++) {
					if (height - grid[++i][c] != 1) {
						return;
					}
				}
				height = grid[i][c];
				length = 0;
			} else if (height - grid[i][c] == -1) {
				if (length >= X) {
					height = grid[i][c];
					length = 1;
				} else {
					return;
				}
			} else {
				return;
			}
		}
		count++;
	}

	private static void colSearch(final int r, final int c) {
		int length = 1;
		int height = grid[r][c];
		for (int i = 1; i < N; i++) {
			if (height - grid[r][i] == 0) {
				length++;
			} else if (height - grid[r][i] == 1) {
				if (N - i < X) {
					return;
				}
				for (int j = 1; j < X; j++) {
					if (height - grid[r][++i] != 1) {
						return;
					}
				}
				height = grid[r][i];
				length = 0;
			} else if (height - grid[r][i] == -1) {
				if (length >= X) {
					height = grid[r][i];
					length = 1;
				} else {
					return;
				}
			} else {
				return;
			}
		}
		count++;
	}
}