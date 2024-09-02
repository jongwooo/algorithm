import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	
	static final int[] dirX = { -1, 1, 0, 0 };
	static final int[] dirY = { 0, 0, 1, -1 };
	
	static int M, N, K;
	static int[][] map;
	static boolean[][] visited;
	static List<Integer> sizes;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		map = new int[N][M];
		visited = new boolean[N][M];
		sizes = new ArrayList<>();
		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine());
			final int sx = Integer.parseInt(st.nextToken());
			final int sy = Integer.parseInt(st.nextToken());
			final int ex = Integer.parseInt(st.nextToken());
			final int ey = Integer.parseInt(st.nextToken());
			for (int x = sx; x < ex; x++) {
				for (int y = sy; y < ey; y++) {
					map[x][y] = 1;
				}
			}
		}
		for (int x = 0; x < N; x++) {
			for (int y = 0; y < M; y++) {
				if (map[x][y] == 0 && !visited[x][y]) {
					final int size = bfs(x, y);
					sizes.add(size);
				}
			}
		}
		Collections.sort(sizes);
		sb.append(sizes.size()).append("\n");
		for (final int size : sizes) {
			sb.append(size).append(" ");
		}
		System.out.println(sb);
	}
	
	private static int bfs(final int sx, final int sy) {
		final Queue<Pos> queue = new ArrayDeque<>();
		queue.add(new Pos(sx, sy));
		visited[sx][sy] = true;
		int size = 1;
		while (!queue.isEmpty()) {
			final Pos pos = queue.poll();
			for (int d = 0; d < 4; d++) {
				final int nx = pos.x + dirX[d];
				final int ny = pos.y + dirY[d];
				if (0 <= nx && nx < N && 0 <= ny && ny < M && map[nx][ny] == 0 && !visited[nx][ny]) {
					queue.add(new Pos(nx, ny));
					visited[nx][ny] = true;
					size++;
				}
			}
		}
		return size;
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