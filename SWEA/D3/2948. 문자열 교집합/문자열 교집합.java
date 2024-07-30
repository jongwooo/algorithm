import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Solution {

	static int N, M;

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("input.txt"));
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			final Set<String> strSet = new HashSet<>();
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				strSet.add(st.nextToken());
			}
			st = new StringTokenizer(br.readLine());
			int result = 0;
			for (int i = 0; i < M; i++) {
				if (strSet.contains(st.nextToken())) {
					result++;
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
