import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int[] dirX = { 1, 1, -1, -1 };
	static int[] dirY = { 1, -1, -1, 1 };

	static int N;
	static int[][] map;
	static boolean[][] visited;
	static boolean[] desserts;
	static int maxCount;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			N = Integer.parseInt(br.readLine());
			map = new int[N][N];
			maxCount = -1;
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			for (int i = 0; i < N - 2; i++) {
				for (int j = 0; j < N - 1; j++) {
					visited = new boolean[N][N];
					desserts = new boolean[101];
					visited[i][j] = true;
					desserts[map[i][j]] = true;
					dfs(1, i, j, i, j, 0);
				}
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(maxCount)
					.append("\n");
		}
		System.out.println(sb);
	}

	private static void dfs(final int count, final int x, final int y, final int sx, final int sy, final int dir) {
		for (int d = dir; d < 4; d++) {
			final int nx = x + dirX[d];
			final int ny = y + dirY[d];
			if (nx == sx && ny == sy) {
				if (2 < count && maxCount < count) {
					maxCount = count;
				}
				return;
			}
			if (0 > nx || nx >= N || 0 > ny || ny >= N) {
				continue;
			}
			if (visited[nx][ny] || desserts[map[nx][ny]]) {
				continue;
			}
			visited[nx][ny] = true;
			desserts[map[nx][ny]] = true;
			dfs(count + 1, nx, ny, sx, sy, d);
			visited[nx][ny] = false;
			desserts[map[nx][ny]] = false;
		}
	}
}