import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int N;
	static int[] nums;
	static int[] operators; // '+', '-', '*', '/'
	static int max, min;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			N = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			operators = new int[4];
			for (int i = 0; i < 4; i++) {
				operators[i] = Integer.parseInt(st.nextToken());
			}
			st = new StringTokenizer(br.readLine());
			nums = new int[N];
			for (int i = 0; i < N; i++) {
				nums[i] = Integer.parseInt(st.nextToken());
			}
			max = Integer.MIN_VALUE;
			min = Integer.MAX_VALUE;
			dfs(0, nums[0]);
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(max - min)
					.append("\n");
		}
		System.out.println(sb);
	}

	private static void dfs(final int depth, final int num) {
		if (depth == N - 1) {
			if (max < num) {
				max = num;
			}
			if (num < min) {
				min = num;
			}
			return;
		}
		if (operators[0] > 0) {
			operators[0]--;
			dfs(depth + 1, num + nums[depth + 1]);
			operators[0]++;
		}
		if (operators[1] > 0) {
			operators[1]--;
			dfs(depth + 1, num - nums[depth + 1]);
			operators[1]++;
		}
		if (operators[2] > 0) {
			operators[2]--;
			dfs(depth + 1, num * nums[depth + 1]);
			operators[2]++;
		}
		if (operators[3] > 0) {
			operators[3]--;
			dfs(depth + 1, num / nums[depth + 1]);
			operators[3]++;
		}
	}
}