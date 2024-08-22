import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int[] prices;
	static int[] plan;
	static int minPrice;

	static {
		prices = new int[4];
		plan = new int[13];
	}

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < 4; i++) {
				prices[i] = Integer.parseInt(st.nextToken());
			}
			st = new StringTokenizer(br.readLine());
			for (int i = 1; i <= 12; i++) {
				plan[i] = Integer.parseInt(st.nextToken());
			}
			minPrice = prices[3];
			dfs(1, 0);
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(minPrice)
					.append("\n");
		}
		System.out.println(sb);
	}

	static void dfs(final int month, final int price) {
		if (minPrice < price) {
			return;
		}
		if (month > 12) {
			if (price < minPrice) {
				minPrice = price;
			}
			return;
		}
		final int temp = plan[month];
		// 1일
		plan[month] = 0;
		dfs(month + 1, price + temp * prices[0]);
		plan[month] = temp;
		// 1달
		plan[month] = 0;
		dfs(month + 1, price + prices[1]);
		plan[month] = temp;
		// 3달
		if (month <= 10) {
			final int[] tempPlan = new int[3];
			for (int i = 0; i < 3; i++) {
				tempPlan[i] = plan[month + i];
				plan[month + i] = 0;
			}
			dfs(month + 1, price + prices[2]);
			for (int i = 0; i < 3; i++) {
				plan[month + i] = tempPlan[i];
			}
		}
	}
}