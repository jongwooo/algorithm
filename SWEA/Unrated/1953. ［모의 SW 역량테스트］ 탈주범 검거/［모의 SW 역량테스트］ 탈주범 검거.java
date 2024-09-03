import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

class Solution {

	static final int[][] dir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
	static final int[][] haveDir = { {}, // 0
			{ 0, 1, 2, 3 }, // 1
			{ 0, 2 }, // 2
			{ 1, 3 }, // 3
			{ 0, 1 }, // 4
			{ 1, 2 }, // 5
			{ 2, 3 }, // 6
			{ 0, 3 }// 7
	};

	static int n, m, sr, sc, l;
	static int[][] graph;
	static boolean[][] visited;
	static int result;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			sr = Integer.parseInt(st.nextToken());
			sc = Integer.parseInt(st.nextToken());
			l = Integer.parseInt(st.nextToken());
			graph = new int[n][m];
			visited = new boolean[n][m];
			result = 1;
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < m; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
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

	private static boolean canGo(final int r, final int c, final int direct) {
		final int curDir = graph[r][c];
		for (final int d : haveDir[curDir]) {
			if (d == direct) {
				return true;
			}
		}
		return false;
	}

	private static void bfs() {
		final Queue<Node> queue = new ArrayDeque<>();
		queue.add(new Node(sr, sc));
		visited[sr][sc] = true;
		int time = 1;
		if (time == l) {
			return;
		}
		while (!queue.isEmpty()) {
			final int size = queue.size();
			for (int s = 0; s < size; s++) {
				final Node cur = queue.poll();
				final int curTunnel = graph[cur.r][cur.c];
				for (int i = 0; i < haveDir[curTunnel].length; i++) {
					final int curDir = haveDir[curTunnel][i];
					final int nr = cur.r + dir[curDir][0];
					final int nc = cur.c + dir[curDir][1];
					if (nr < 0 || nr >= n || nc < 0 || nc >= m) {
						continue;
					}
					if ((graph[nr][nc] == 0) || !canGo(nr, nc, (curDir + 2) % 4) || visited[nr][nc]) {
						continue;
					}
					visited[nr][nc] = true;
					result++;
					queue.add(new Node(nr, nc));
				}
			}
			if (++time == l) {
				return;
			}
		}
	}
}

class Node {

	final int r;
	final int c;

	public Node(final int r, final int c) {
		this.r = r;
		this.c = c;
	}
}