import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	static int N, M;
	static String[] s1, s2;

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
			st = new StringTokenizer(br.readLine());
			s1 = new String[N];
			for (int i = 0; i < N; i++) {
				s1[i] = st.nextToken();
			}
			st = new StringTokenizer(br.readLine());
			s2 = new String[M];
			for (int i = 0; i < M; i++) {
				s2[i] = st.nextToken();
			}
			Arrays.sort(s1);
			Arrays.sort(s2);
			int result = 0;
			int p1 = 0;
			int p2 = 0;
			while (p1 < N && p2 < M) {
				final int compare = s1[p1].compareTo(s2[p2]);
				if (compare == 0) {
					result++;
					p1++;
					p2++;
				} else if (compare < 0) {
					p1++;
				} else if (compare > 0) {
					p2++;
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
