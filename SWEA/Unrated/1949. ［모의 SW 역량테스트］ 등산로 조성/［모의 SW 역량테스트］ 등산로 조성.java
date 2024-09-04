import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Solution {

	static final int[] dirX = { -1, 1, 0, 0 };
	static final int[] dirY = { 0, 0, 1, -1 };

	static int N, K;
	static int[][] map;
	static int maxHeight;
	static List<Pos> maxHeightPos;
	static int maxLength;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			map = new int[N][N];
			maxHeight = 0;
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					if (maxHeight < map[i][j]) {
						maxHeight = map[i][j];
					}
				}
			}
			maxHeightPos = new ArrayList<>();
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (map[i][j] == maxHeight) {
						maxHeightPos.add(new Pos(i, j));
					}
				}
			}
			maxLength = 0;
			for (int k = 0; k <= K; k++) {
				for (int i = 0; i < N; i++) {
					for (int j = 0; j < N; j++) {
						if (map[i][j] - k < 0) {
							continue;
						}
						map[i][j] -= k;
						for (final Pos pos : maxHeightPos) {
							dfs(pos.x, pos.y, 1);
						}
						map[i][j] += k;
					}
				}
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(maxLength)
					.append("\n");
		}
		System.out.println(sb);
	}

	private static void dfs(final int x, final int y, final int length) {
		for (int d = 0; d < 4; d++) {
			final int nx = x + dirX[d];
			final int ny = y + dirY[d];
			if (0 <= nx && nx < N && 0 <= ny && ny < N && map[nx][ny] < map[x][y]) {
				dfs(nx, ny, length + 1);
			}
		}
		if (maxLength < length) {
			maxLength = length;
		}
	}
}

class Pos {

	final int x;
	final int y;

	public Pos(final int x, final int y) {
		super();
		this.x = x;
		this.y = y;
	}
}