import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {

	static int N;
	static int P;
	static int[][] map;
	static boolean[] visited;
	static List<Pos> stairs;
	static List<Pos> persons;
	static int minTime;

	public static void main(String[] args) throws IOException {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			N = Integer.parseInt(br.readLine());
			map = new int[N][N];
			stairs = new ArrayList<>();
			persons = new ArrayList<>();
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
					if (map[i][j] == 1) {
						persons.add(new Pos(j, i));
					}
					if (map[i][j] >= 2) {
						stairs.add(new Pos(j, i));
					}
				}
			}
			P = persons.size();
			visited = new boolean[P];
			minTime = Integer.MAX_VALUE;
			combination(0);
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(minTime)
					.append("\n");
		}
		System.out.println(sb);
	}

	private static void combination(final int depth) {
		if (depth == P) {
			final List<Person> group0 = new ArrayList<>();
			final List<Person> group1 = new ArrayList<>();
			for (int i = 0; i < P; i++) {
				final int x = persons.get(i).x;
				final int y = persons.get(i).y;
				int distance = 0;
				if (visited[i]) {
					distance = Math.abs(x - stairs.get(0).x) + Math.abs(y - stairs.get(0).y);
					group0.add(new Person(x, y, distance));
				} else {
					distance = Math.abs(x - stairs.get(1).x) + Math.abs(y - stairs.get(1).y);
					group1.add(new Person(x, y, distance));
				}
			}
			Collections.sort(group0);
			Collections.sort(group1);
			minTime = Math.min(minTime, go(group0, group1));
			return;
		}
		visited[depth] = true;
		combination(depth + 1);
		visited[depth] = false;
		combination(depth + 1);
	}

	private static int go(final List<Person> group0, final List<Person> group1) {
		return Math.max(calculateTime(0, group0), calculateTime(1, group1));
	}

	static int calculateTime(final int index, final List<Person> group) {
		int time = 0;
		int stairTime = map[stairs.get(index).y][stairs.get(index).x];
		for (int i = 0; i < group.size(); i++) {
			if (i < 3) {
				time = group.get(i).distance + 1 + stairTime;
			} else {
				if (group.get(i - 3).distance + 1 + stairTime <= group.get(i).distance) {
					time = group.get(i).distance + 1 + stairTime;
				} else {
					time = group.get(i - 3).distance + 1 + stairTime + stairTime;
				}
			}
		}
		return time;
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

class Person implements Comparable<Person> {

	final int x;
	final int y;
	final int distance;

	public Person(final int x, final int y, final int distance) {
		super();
		this.x = x;
		this.y = y;
		this.distance = distance;
	}

	@Override
	public int compareTo(final Person other) {
		return this.distance - other.distance;
	}
}