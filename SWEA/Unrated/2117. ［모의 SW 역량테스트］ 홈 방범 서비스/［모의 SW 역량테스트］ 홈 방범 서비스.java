import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

	static final int[] dirX = { -1, 1, 0, 0 };
	static final int[] dirY = { 0, 0, 1, -1 };
	static final int[] K = new int[26];

	static int N, M;
	static int[][] map;
	static int maxCount;

	static {
		for (int k = 0; k < 26; k++) {
			K[k] = (k * k) + (k - 1) * (k - 1);
		}
	}

	public static void main(final String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			map = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			maxCount = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					bfs(i, j);
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

	private static void bfs(final int x, final int y) {
		final Queue<Pos> queue = new ArrayDeque<>();
		queue.add(new Pos(x, y));
		final boolean[][] visited = new boolean[N][N];
		visited[x][y] = true;
		int home = map[x][y];
		int k = 1;
		if (K[k] <= home * M) {
			if (maxCount < home) {
				maxCount = home;
			}
		}
		while (k < N + 2) {
			final int queueSize = queue.size();
			for (int i = 0; i < queueSize; i++) {
				final Pos pos = queue.poll();
				for (int d = 0; d < 4; d++) {
					final int nx = pos.x + dirX[d];
					final int ny = pos.y + dirY[d];
					if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nx][ny]) {
						queue.add(new Pos(nx, ny));
						visited[nx][ny] = true;
						if (map[nx][ny] == 1) {
							home++;
						}
					}
				}
			}
			if (K[k + 1] <= home * M) {
				if (maxCount < home) {
					maxCount = home;
				}
			}
			k++;
		}
	}
}

class Pos {

	final int x;
	final int y;

	public Pos(final int x, final int y) {
		this.x = x;
		this.y = y;
	}
}