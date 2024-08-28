import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

	static int length, start;
	static List<Integer>[] connect;
	static int maxTime;
	static int result;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		for (int testCase = 1; testCase <= 10; testCase++) {
			st = new StringTokenizer(br.readLine());
			length = Integer.parseInt(st.nextToken());
			start = Integer.parseInt(st.nextToken());
			connect = new List[101];
			for (int i = 1; i <= 100; i++) {
				connect[i] = new ArrayList<>();
			}
			maxTime = 0;
			result = 0;
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < length / 2; i++) {
				final int from = Integer.parseInt(st.nextToken());
				final int to = Integer.parseInt(st.nextToken());
				if (connect[from].contains(to)) {
					continue;
				}
				connect[from].add(to);
			}
			bfs();
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(result)
					.append("\n");
		}
		System.out.print(sb);
	}

	private static void bfs() {
		final Queue<int[]> queue = new ArrayDeque<>();
		queue.add(new int[] { start, 0 });
		final boolean[] call = new boolean[101];
		call[start] = true;
		while (!queue.isEmpty()) {
			final int[] now = queue.poll();
			for (final int next : connect[now[0]]) {
				if (call[next]) {
					continue;
				}
				queue.add(new int[] { next, now[1] + 1 });
				call[next] = true;
				if (maxTime < now[1] + 1) {
					maxTime = now[1] + 1;
					result = 0;
				}
				if (result < next) {
					result = next;
				}
			}
		}
	}
}