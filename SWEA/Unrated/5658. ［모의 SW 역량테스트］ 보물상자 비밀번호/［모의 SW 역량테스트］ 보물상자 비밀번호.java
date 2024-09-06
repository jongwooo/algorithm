import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeSet;

class Solution {

	static int N, K;
	static char[] nums;
	static Set<String> passwordSet;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			nums = br.readLine()
					.toCharArray();
			passwordSet = new TreeSet<>(Collections.reverseOrder());
			StringBuilder certgen;
			for (int i = 0; i < N / 4; i++) {
				char temp = nums[N - 1];
				for (int j = N - 1; j > 0; j--) {
					nums[j] = nums[j - 1];
				}
				nums[0] = temp;
				for (int j = 0; j < N; j += N / 4) {
					certgen = new StringBuilder();
					for (int k = j; k < j + (N / 4); k++) {
						certgen.append(nums[k]);
					}
					passwordSet.add(certgen.toString());
				}
			}
			final String[] passwords = passwordSet.toArray(new String[passwordSet.size()]);
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(Long.parseLong(passwords[K - 1], 16))
					.append("\n");
		}
		System.out.println(sb);
	}
}