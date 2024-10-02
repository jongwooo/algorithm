import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static BufferedReader br;
	static StringBuilder sb;
	static StringTokenizer st;

	static int N;
	static int[] sequence;
	static int[] dp;

	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			N = Integer.parseInt(br.readLine());
			sequence = new int[N];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				sequence[i] = Integer.parseInt(st.nextToken());
			}
			dp = new int[N];
			int lis = 0;
			for (int i = 0; i < N; i++) {
				final int index = binarySearch(sequence[i], 0, lis, lis + 1);
				if (index == -1) {
					dp[lis++] = sequence[i];
				} else {
					dp[index] = sequence[i];
				}
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(lis)
					.append("\n");
		}
		System.out.println(sb);
	}

	private static int binarySearch(final int num, int start, int end, final int size) {
		int index = 0;
		while (start <= end) {
			final int mid = (start + end) / 2;
			if (num <= dp[mid]) {
				index = mid;
				end = mid - 1;
			} else {
				start = mid + 1;
			}
		}
		if (start == size) {
			return -1;
		}
		return index;
	}
}