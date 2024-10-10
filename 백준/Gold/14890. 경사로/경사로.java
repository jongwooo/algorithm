import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static BufferedReader br;
	static StringTokenizer st;

	static int N, L;
	static int[][] grid;
	static int count;

	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		L = Integer.parseInt(st.nextToken());
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
		System.out.println(count);
	}

	private static void rowSearch(final int r, final int c) {
		int length = 1;
		int height = grid[r][c];
		for (int i = 1; i < N; i++) {
			if (height - grid[i][c] == 0) {
				length++;
			} else if (height - grid[i][c] == 1) {
				if (N - i < L) {
					return;
				}
				for (int j = 1; j < L; j++) {
					if (height - grid[++i][c] != 1) {
						return;
					}
				}
				height = grid[i][c];
				length = 0;
			} else if (height - grid[i][c] == -1) {
				if (length >= L) {
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
				if (N - i < L) {
					return;
				}
				for (int j = 1; j < L; j++) {
					if (height - grid[r][++i] != 1) {
						return;
					}
				}
				height = grid[r][i];
				length = 0;
			} else if (height - grid[r][i] == -1) {
				if (length >= L) {
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
