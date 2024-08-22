import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static final int[] dirX = { -1, 1, 0, 0 };
	static final int[] dirY = { 0, 0, 1, -1 };

	static int N;
	static int[][] A;
	static int maxRoom, maxMove;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			N = Integer.parseInt(br.readLine());
			A = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					A[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			maxRoom = N * N + 1;
			maxMove = 0;
			for (int x = 0; x < N; x++) {
				for (int y = 0; y < N; y++) {
					moveRoom(x, y, 1);
				}
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(maxRoom)
					.append(" ")
					.append(maxMove)
					.append("\n");
		}
		System.out.println(sb);
	}

	static int moveRoom(final int x, final int y, int move) {
		for (int d = 0; d < 4; d++) {
			final int nx = x + dirX[d];
			final int ny = y + dirY[d];
			if (0 > nx || 0 > ny || nx >= N || ny >= N) {
				continue;
			}
			if (A[x][y] + 1 != A[nx][ny]) {
				continue;
			}
			move = moveRoom(nx, ny, move + 1);
			if (maxMove < move) {
				maxMove = move;
				maxRoom = A[x][y];
			} else if (maxMove == move && maxRoom > A[x][y]) {
				maxRoom = A[x][y];
			}
			break;
		}
		return move;
	}
}

class Pos {

	final int x;
	final int y;

	public Pos(int x, int y) {
		super();
		this.x = x;
		this.y = y;
	}
}