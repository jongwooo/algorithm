import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Solution {

	static final int[] dirX = { -1, 1, 0, 0 };
	static final int[] dirY = { 0, 0, -1, 1 };

	static int H, W, N;
	static char[][] map;
	static char[] cmd;
	static int sx, sy, d;
	static Map<Character, Integer> dirMap;
	static Map<Integer, Character> dirRevMap;

	static {
		dirMap = new HashMap<>();
		dirMap.put('^', 0);
		dirMap.put('v', 1);
		dirMap.put('<', 2);
		dirMap.put('>', 3);
		dirRevMap = new HashMap<>();
		dirRevMap.put(0, '^');
		dirRevMap.put(1, 'v');
		dirRevMap.put(2, '<');
		dirRevMap.put(3, '>');
	}

	public static void main(String[] args) throws IOException {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			H = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			map = new char[H][W];
			for (int i = 0; i < H; i++) {
				map[i] = br.readLine()
						.toCharArray();
				for (int j = 0; j < W; j++) {
					if (dirMap.containsKey(map[i][j])) {
						sx = i;
						sy = j;
						d = dirMap.get(map[i][j]);
					}
				}
			}
			N = Integer.parseInt(br.readLine());
			cmd = new char[N];
			cmd = br.readLine()
					.toCharArray();
			play();
			sb.append("#")
					.append(testCase)
					.append(" ");
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++) {
					sb.append(map[i][j]);
				}
				sb.append("\n");
			}
		}
		System.out.println(sb);
	}

	private static void play() {
		for (char c : cmd) {
            if (c == 'U') {
                move(0);
            } else if (c == 'D') {
                move(1);
            } else if (c == 'L') {
                move(2);
            } else if (c == 'R') {
                move(3);
            } else if (c == 'S') {
                shell();
            }
		}
	}

	private static void move(int moveDir) {
		d = moveDir;
		int nx = sx + dirX[d];
		int ny = sy + dirY[d];
		if (nx < 0 || nx >= H || ny < 0 || ny >= W || map[nx][ny] != '.') {
			map[sx][sy] = dirRevMap.get(d);
			return;
		}
		map[sx][sy] = '.';
		map[nx][ny] = dirRevMap.get(d);
		sx = nx;
		sy = ny;
	}

	private static void shell() {
		int x = sx;
		int y = sy;
		while (true) {
			int nx = x + dirX[d];
			int ny = y + dirY[d];
			if (nx < 0 || nx >= H || ny < 0 || ny >= W || map[nx][ny] == '#') {
				return;
			}
			if (map[nx][ny] == '*') {
				map[nx][ny] = '.';
				return;
			}
			x = nx;
			y = ny;
		}
	}
}