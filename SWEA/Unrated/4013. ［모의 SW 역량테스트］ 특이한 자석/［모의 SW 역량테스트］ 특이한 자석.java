import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {

	static BufferedReader br;
	static StringBuilder sb;
	static StringTokenizer st;

	static int T;
	static int K;
	static int[][] magnets;
	static int[] rotateDirs;

	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			K = Integer.parseInt(br.readLine());
			magnets = new int[4][8];
			for (int i = 0; i < 4; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < 8; j++) {
					magnets[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			rotateDirs = new int[4];
			for (int i = 0; i < K; i++) {
				Arrays.fill(rotateDirs, 0);
				st = new StringTokenizer(br.readLine());
				final int targetMagnet = Integer.parseInt(st.nextToken()) - 1;
				final int rotateDir = Integer.parseInt(st.nextToken());
				rotateDirs[targetMagnet] = rotateDir;
				rotateMagnets(targetMagnet);
			}
			int scoreSum = 0;
			int score = 1;
			for (int i = 0; i < 4; i++) {
				if (magnets[i][0] == 1) {
					scoreSum += score;
				}
				score *= 2;
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(scoreSum)
					.append("\n");
		}
		System.out.println(sb);
	}

	private static void rotateMagnets(final int targetMagnet) {
		for (int i = targetMagnet - 1; i >= 0; i--) {
			if (magnets[i][2] != magnets[i + 1][6]) {
				rotateDirs[i] = -rotateDirs[i + 1];
			} else {
				break;
			}
		}
		for (int i = targetMagnet + 1; i < 4; i++) {
			if (magnets[i][6] != magnets[i - 1][2]) {
				rotateDirs[i] = -rotateDirs[i - 1];
			} else {
				break;
			}
		}
		for (int i = 0; i < 4; i++) {
			rotateMagnet(i);
		}
	}

	private static void rotateMagnet(final int targetMagnet) {
		if (rotateDirs[targetMagnet] == 1) {
			final int temp = magnets[targetMagnet][7];
			for (int i = 7; i > 0; i--) {
				magnets[targetMagnet][i] = magnets[targetMagnet][i - 1];
			}
			magnets[targetMagnet][0] = temp;
		}
		if (rotateDirs[targetMagnet] == -1) {
			final int temp = magnets[targetMagnet][0];
			for (int i = 0; i < 7; i++) {
				magnets[targetMagnet][i] = magnets[targetMagnet][i + 1];
			}
			magnets[targetMagnet][7] = temp;
		}
	}
}