import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

	static Queue<Integer> queue;

	static {
		queue = new ArrayDeque<>();
	}

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		for (int testCase = 1; testCase <= 10; testCase++) {
			final int T = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			queue.clear();
			for (int i = 0; i < 8; i++) {
				queue.add(Integer.parseInt(st.nextToken()));
			}
			int sub = 1;
			while (true) {
				int num = queue.poll();
				num -= sub;
				if (num <= 0) {
					queue.add(0);
					break;
				}
				sub++;
				if (sub > 5) {
					sub = 1;
				}
				queue.add(num);
			}
			sb.append("#")
					.append(T)
					.append(" ");
			for (int i = 0; i < 8; i++) {
				sb.append(queue.poll())
						.append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}
}