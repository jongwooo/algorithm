import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {

	static final int[] dirX = { 0, -1, 1, 0, 0 };
	static final int[] dirY = { 0, 0, 0, -1, 1 };

	static int N, M, K;
	static List<Microbe> microbes;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			microbes = new ArrayList<>();
			for (int k = 0; k < K; k++) {
				st = new StringTokenizer(br.readLine());
				final int x = Integer.parseInt(st.nextToken());
				final int y = Integer.parseInt(st.nextToken());
				final int count = Integer.parseInt(st.nextToken());
				final int dir = Integer.parseInt(st.nextToken());
				microbes.add(new Microbe(x * N + y, x, y, count, dir));
			}
			for (int time = 0; time < M; time++) {
				for (int i = 0; i < microbes.size(); i++) {
					final Microbe microbe = microbes.get(i);
					microbe.x += dirX[microbe.dir];
					microbe.y += dirY[microbe.dir];
					microbe.pos = microbe.x * N + microbe.y;
					if (microbe.x == 0 || microbe.y == 0 || microbe.x == N - 1 || microbe.y == N - 1) {
						microbe.count /= 2;
						microbe.turnBack();
						if (microbe.count == 0) {
							microbes.remove(i);
							i--;
						}
					}
				}
				Collections.sort(microbes);
				for (int i = 0; i < microbes.size() - 1; i++) {
					final Microbe now = microbes.get(i);
					final Microbe next = microbes.get(i + 1);
					if (now.pos == next.pos) {
						now.count += next.count;
						microbes.remove(i + 1);
						i--;
					}
				}
			}
			int total = 0;
			for (final Microbe microbe : microbes) {
				total += microbe.count;
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(total)
					.append("\n");
		}
		System.out.println(sb);
	}
}

class Microbe implements Comparable<Microbe> {

	int pos;
	int x;
	int y;
	int count;
	int dir;

	public Microbe(final int pos, final int x, final int y, final int count, final int dir) {
		super();
		this.pos = pos;
		this.x = x;
		this.y = y;
		this.count = count;
		this.dir = dir;
	}

	public void turnBack() {
		if (dir == 1) {
			dir = 2;
		} else if (dir == 2) {
			dir = 1;
		} else if (dir == 3) {
			dir = 4;
		} else if (dir == 4) {
			dir = 3;
		}
	}

	@Override
	public int compareTo(final Microbe other) {
		if (this.pos == other.pos) {
			return other.count - this.count;
		}
		return this.pos - other.pos;
	}
}