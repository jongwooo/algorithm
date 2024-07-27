import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Solution {

	private static final int[] dirX = { -1, 1, 0, 0 };
	private static final int[] dirY = { 0, 0, 1, -1 };

	private static int N;
	private static int[][] grid;
	private static int result;

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("input.txt"));
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			N = Integer.parseInt(br.readLine());
			grid = new int[N][N];
			result = Integer.MAX_VALUE;
			String temp;
			for (int i = 0; i < N; i++) {
				temp = br.readLine();
				for (int j = 0; j < N; j++) {
					grid[i][j] = temp.charAt(j) - '0';
				}
			}
			bfs();
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(result)
					.append("\n");
		}
		System.out.println(sb);
	}

	private static void bfs() {
		final PriorityQueue<Node> pq = new PriorityQueue<>();
		final boolean[][] visited = new boolean[N][N];
		pq.add(new Node(0, 0, 0));
		visited[0][0] = true;
		while (!pq.isEmpty()) {
			final Node cur = pq.poll();
			if (cur.x == N - 1 && cur.y == N - 1) {
				if (result > cur.t) {
					result = cur.t;
				}
			}
			int nx, ny;
			for (int d = 0; d < 4; d++) {
				nx = cur.x + dirX[d];
				ny = cur.y + dirY[d];
				if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nx][ny]) {
					pq.add(new Node(nx, ny, cur.t + grid[nx][ny]));
					visited[nx][ny] = true;
				}
			}
		}
	}
}

class Node implements Comparable<Node> {

	final int x;
	final int y;
	final int t;

	public Node(final int x, final int y, final int t) {
		this.x = x;
		this.y = y;
		this.t = t;
	}

	@Override
	public int compareTo(final Node other) {
		return this.t - other.t;
	}
}
