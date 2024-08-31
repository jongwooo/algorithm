import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {

	static final int[] dirX = { -1, 1, 0, 0 };
	static final int[] dirY = { 0, 0, 1, -1 };

	static int N;
	static int[][] cell;
	static List<Maxynos> cores;
	static int maxynosCount;
	static int alreadyConnected;
	static int maxConnected;
	static int minLength;

	public static void main(final String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			N = Integer.parseInt(br.readLine());
			cell = new int[N][N];
			cores = new ArrayList<>();
			maxynosCount = 0;
			alreadyConnected = 0;
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					cell[i][j] = Integer.parseInt(st.nextToken());
					if (cell[i][j] == 1) {
						maxynosCount++;
						if (isEdgeCell(i, j)) {
							alreadyConnected++;
							continue;
						}
						cores.add(new Maxynos(i, j));
					}
				}
			}
			maxConnected = alreadyConnected;
			minLength = Integer.MAX_VALUE;
			dfs(0, alreadyConnected, 0);
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(minLength)
					.append("\n");
		}
		System.out.print(sb);
	}

	private static void dfs(final int depth, final int connected, final int length) {
		if (depth == maxynosCount - alreadyConnected) {
			if (connected < maxConnected) {
				return;
			}
			if (maxConnected < connected) {
				maxConnected = connected;
				minLength = Integer.MAX_VALUE;
			}
			if (length < minLength) {
				minLength = length;
			}
			return;
		}
		final Maxynos core = cores.get(depth);
		for (int d = 0; d < 4; d++) {
			int newConnect = 0;
			int newWireLength = 0;
			int cx = core.x + dirX[d];
			int cy = core.y + dirY[d];
			while (true) {
				if (cell[cx][cy] != 0) {
					cx -= dirX[d];
					cy -= dirY[d];
					break;
				}
				if (isEdgeCell(cx, cy)) {
					newConnect++;
					newWireLength = connect(core, d);
					break;
				}
				cx += dirX[d];
				cy += dirY[d];
			}
			dfs(depth + 1, connected + newConnect, length + newWireLength);
			while (cell[cx][cy] == -1) {
				cell[cx][cy] = 0;
				cx -= dirX[d];
				cy -= dirY[d];
			}
		}
	}

	private static int connect(final Maxynos core, final int d) {
		int length = 0;
		int x = core.x;
		int y = core.y;
		while (!isEdgeCell(x, y)) {
			length++;
			x += dirX[d];
			y += dirY[d];
			cell[x][y] = -1;
		}
		return length;
	}

	private static boolean isEdgeCell(final int x, final int y) {
		return x == 0 || x == N - 1 || y == 0 || y == N - 1;
	}
}

class Maxynos {

	final int x;
	final int y;

	public Maxynos(final int x, final int y) {
		this.x = x;
		this.y = y;
	}
}