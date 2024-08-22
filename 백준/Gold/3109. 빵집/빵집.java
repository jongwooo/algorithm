import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static final int[] dirX = { -1, 0, 1 };
	static final int[] dirY = { 1, 1, 1 };

	static int R, C;
	static char[][] map;
	static int count;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		map = new char[R][C];
		for (int i = 0; i < R; i++) {
			map[i] = br.readLine()
					.toCharArray();
		}
		for (int i = 0; i < R; i++) {
			if (connect(i, 0)) {
				count++;
			}
		}
		System.out.println(count);
	}

	static boolean connect(final int x, final int y) {
		map[x][y] = '-';
		if (y == C - 1) {
			return true;
		}
		for (int d = 0; d < 3; d++) {
			final int nx = x + dirX[d];
			final int ny = y + dirY[d];
			if (0 <= nx && nx < R && 0 <= ny && ny < C && map[nx][ny] == '.') {
				if (connect(nx, ny)) {
					return true;
				}
			}
		}
		return false;
	}
}
