import java.util.Scanner;

public class Solution {

	static int N;
	static long[] heights;
	static int[] high;
	static int[] low;

	public static void main(String[] args) throws Exception {
		final Scanner sc = new Scanner(System.in);
		final StringBuilder sb = new StringBuilder();
		final int T = sc.nextInt();
		for (int testCase = 1; testCase <= T; testCase++) {
			N = sc.nextInt();
			heights = new long[N + 1];
			high = new int[N + 1];
			low = new int[N + 1];
			int hIndex = 0;
			int lIndex = 0;
			for (int i = 1; i <= N; i++) {
				heights[i] = sc.nextLong();
			}
			if (heights[1] < heights[2]) {
				low[lIndex++] = 1;
			}
			for (int i = 2; i <= N; i++) {
				if (i == N) {
					if (heights[i - 1] > heights[i]) {
						low[lIndex++] = i;
					}
					continue;
				}
				if (heights[i - 1] < heights[i] && heights[i] > heights[i + 1]) {
					high[hIndex++] = i;
				} else if (heights[i - 1] > heights[i] && heights[i] < heights[i + 1]) {
					low[lIndex++] = i;
				}
			}
			int l = 0;
			int h = 0;
			int result = 0;
			while (l < lIndex && h < hIndex) {
				if (high[h] < low[l]) {
					h++;
					continue;
				}
				result += (high[h] - low[l]) * (low[l + 1] - high[h]);
				l++;
				h++;
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(result)
					.append("\n");
		}
		System.out.println(sb);
	}
}