import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int[][] ladder;

	static {
		ladder = new int[100][100];
	}

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		for (int testCase = 1; testCase <= 10; testCase++) {
			final int T = Integer.parseInt(br.readLine());
			int end = 0;
			for (int i = 0; i < 100; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < 100; j++) {
					ladder[i][j] = Integer.parseInt(st.nextToken());
					if (i == 99 && ladder[i][j] == 2) {
						end = j;
					}
				}
			}
			sb.append("#")
					.append(T)
					.append(" ")
					.append(climbUp(end))
					.append("\n");
		}
		System.out.println(sb);
	}

	public static int climbUp(final int end) {
		int cur = end;
		for (int depth = 99; depth >= 0; depth--) {
			// 좌
			if (cur > 1 && ladder[depth][cur - 1] == 1) {
				while (cur > 1 && ladder[depth][cur - 1] != 0) {
					cur--;
				}
				continue;
			}
			// 우
			if (cur < 99 && ladder[depth][cur + 1] == 1) {
				while (cur < 99 && ladder[depth][cur + 1] != 0) {
					cur++;
				}
			}
		}
		return cur;
	}
}
