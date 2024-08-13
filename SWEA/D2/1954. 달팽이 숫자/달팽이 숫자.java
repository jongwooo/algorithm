import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			sb.append("#")
					.append(testCase)
					.append("\n");
			final int N = Integer.parseInt(br.readLine());
			if (N == 1) {
				sb.append(1)
						.append("\n");
				continue;
			}
			final int[][] arr = new int[N][N];
			int x = 0;
			int y = 0;
			int d = 0;
			for (int i = 1; i <= Math.pow(N, 2); i++) {
				arr[x][y] = i;
				if (d == 0) {
					y++;
					if (y == N - 1 || arr[x][y + 1] != 0) {
						d++;
					}
				} else if (d == 1) {
					x++;
					if (x == N - 1 || arr[x + 1][y] != 0) {
						d++;
					}
				} else if (d == 2) {
					y--;
					if (y == 0 || arr[x][y - 1] != 0) {
						d++;
					}
				} else if (d == 3) {
					x--;
					if (x == 0 || arr[x - 1][y] != 0) {
						d = 0;
					}
				}
			}
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					sb.append(arr[i][j])
							.append(" ");
				}
				sb.append("\n");
			}
		}
		System.out.println(sb);
	}
}
