import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int N, L;
	static int[] points;
	static int[] calories;
	static int result;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			L = Integer.parseInt(st.nextToken());
			points = new int[N];
			calories = new int[N];
			result = 0;
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				points[i] = Integer.parseInt(st.nextToken());
				calories[i] = Integer.parseInt(st.nextToken());
			}
			for (int i = 0; i < 1 << N; i++) {
				int pointSum = 0;
				int calorieSum = 0;
				for (int j = 0; j < N; j++) {
					if ((i & 1 << j) != 0) {
						pointSum += points[j];
						calorieSum += calories[j];
					}
				}
				if (calorieSum > L) {
					continue;
				}
				if (result < pointSum) {
					result = pointSum;
				}
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