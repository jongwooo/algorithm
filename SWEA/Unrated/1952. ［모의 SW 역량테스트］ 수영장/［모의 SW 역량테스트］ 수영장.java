import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {

	static int[] prices;
	static int[] plans;
	static int[] dp;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			prices = new int[4];
			plans = new int[13];
			for (int i = 0; i < 4; i++) {
				prices[i] = Integer.parseInt(st.nextToken());
			}
			st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= 12; i++) {
				final int days = Integer.parseInt(st.nextToken());
				plans[i] = Math.min(plans[i - 1] + days * prices[0], plans[i - 1] + prices[1]);
				if (i >= 3) {
					plans[i] = Math.min(plans[i], plans[i - 3] + prices[2]);
				}
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(Math.min(plans[12], prices[3]))
					.append("\n");
		}
		System.out.println(sb);
	}
}