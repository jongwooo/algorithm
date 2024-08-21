import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static int N;
	public static String S;
	public static int[][] map, answer;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			S = st.nextToken();
			map = new int[N][N];
			answer = new int[N][N];
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			if (S.equals("up")) {
				up();
			} else if (S.equals("down")) {
				down();
			} else if (S.equals("left")) {
				left();
			} else if (S.equals("right")) {
				right();
			}
			sb.append("#")
					.append(testCase)
					.append("\n");
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					sb.append(answer[i][j])
							.append(" ");
				}
				sb.append("\n");
			}
		}
		System.out.println(sb);
	}

	public static void up() {
		for (int j = 0; j < N; j++) {
			for (int i = 0; i < N - 1; i++) {
				if (map[i][j] == 0) {
					continue;
				}
				int idx = i + 1;
				while (map[idx][j] == 0) {
					if (idx == N - 1) {
						break;
					}
					idx++;
				}
				if (map[idx][j] == 0) {
					continue;
				}

				if (map[i][j] == map[idx][j]) {
					map[i][j] += map[idx][j];
					map[idx][j] = 0;
					i = idx;
				}
			}
			int cur = 0;
			for (int i = 0; i < N; i++) {
				if (map[i][j] != 0) {
					answer[cur++][j] = map[i][j];
				}
			}
		}
	}

	public static void down() {
		for (int j = 0; j < N; j++) {
			for (int i = N - 1; i > 0; i--) {
				if (map[i][j] == 0) {
					continue;
				}
				int idx = i - 1;
				while (map[idx][j] == 0) {
					if (idx == 0) {
						break;
					}
					idx--;
				}
				if (map[idx][j] == 0) {
					continue;
				}
				if (map[i][j] == map[idx][j]) {
					map[i][j] += map[idx][j];
					map[idx][j] = 0;
					i = idx;
				}
			}
			int cur = N - 1;
			for (int i = N - 1; i >= 0; i--) {
				if (map[i][j] != 0) {
					answer[cur--][j] = map[i][j];
				}
			}
		}
	}

	public static void left() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N - 1; j++) {
				if (map[i][j] == 0) {
					continue;
				}
				int idx = j + 1;
				while (map[i][idx] == 0) {
					if (idx == N - 1) {
						break;
					}
					idx++;
				}
				if (map[i][idx] == 0) {
					continue;
				}
				if (map[i][j] == map[i][idx]) {
					map[i][j] += map[i][idx];
					map[i][idx] = 0;
					j = idx;
				}
			}
			int cur = 0;
			for (int j = 0; j < N; j++) {
				if (map[i][j] != 0) {
					answer[i][cur++] = map[i][j];
				}
			}
		}
	}

	public static void right() {
		for (int i = 0; i < N; ++i) {
			for (int j = N - 1; j > 0; j--) {
				if (map[i][j] == 0) {
					continue;
				}
				int idx = j - 1;
				while (map[i][idx] == 0) {
					if (idx == 0) {
						break;
					}
					idx--;
				}
				if (map[i][idx] == 0) {
					continue;
				}
				if (map[i][j] == map[i][idx]) {
					map[i][j] += map[i][idx];
					map[i][idx] = 0;
					j = idx;
				}
			}
			int cur = N - 1;
			for (int j = N - 1; j >= 0; j--) {
				if (map[i][j] != 0) {
					answer[i][cur--] = map[i][j];
				}
			}
		}
	}
}