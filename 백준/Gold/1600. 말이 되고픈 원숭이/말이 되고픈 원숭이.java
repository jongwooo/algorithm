import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static final int[] monkeyDirX = { -1, 1, 0, 0 };
	static final int[] monkeyDirY = { 0, 0, 1, -1 };
	static final int[] horseDirX = { -2, -1, 1, 2, -2, -1, 1, 2 };
	static final int[] horseDirY = { -1, -2, -2, -1, 1, 2, 2, 1 };

	static int K;
	static int W, H;
	static int[][] map;
	static int[][][] visited;

	public static void main(final String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		K = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		W = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		map = new int[H][W];
		visited = new int[H][W][K + 1];
		for (int i = 0; i < H; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < W; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				Arrays.fill(visited[i][j], -1);
			}
		}
		System.out.println(bfs());
	}

	private static int bfs() {
		final Queue<Pos> queue = new ArrayDeque<>();
		queue.add(new Pos(0, 0, 0));
		visited[0][0][0] = 0;
		while (!queue.isEmpty()) {
			final Pos pos = queue.poll();
			if (pos.x == H - 1 && pos.y == W - 1) {
				return visited[pos.x][pos.y][pos.ability];
			}
			for (int d = 0; d < 4; d++) {
				final int nx = pos.x + monkeyDirX[d];
				final int ny = pos.y + monkeyDirY[d];
				if (0 <= nx && nx < H && 0 <= ny && ny < W && map[nx][ny] == 0 && visited[nx][ny][pos.ability] == -1) {
					queue.add(new Pos(nx, ny, pos.ability));
					visited[nx][ny][pos.ability] = visited[pos.x][pos.y][pos.ability] + 1;
				}
			}
			if (pos.ability < K) {
				for (int d = 0; d < 8; d++) {
					final int nx = pos.x + horseDirX[d];
					final int ny = pos.y + horseDirY[d];
					if (0 <= nx && nx < H && 0 <= ny && ny < W && map[nx][ny] == 0
							&& visited[nx][ny][pos.ability + 1] == -1) {
						queue.add(new Pos(nx, ny, pos.ability + 1));
						visited[nx][ny][pos.ability + 1] = visited[pos.x][pos.y][pos.ability] + 1;
					}
				}
			}
		}
		return -1;
	}
}

class Pos {

	final int x;
	final int y;
	final int ability;

	public Pos(final int x, final int y, final int ability) {
		super();
		this.x = x;
		this.y = y;
		this.ability = ability;
	}
}