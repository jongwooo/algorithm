import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int[] gyuyeong;
	static int[] inyeong;
	static int[] deck;
	static boolean[] exist;
	static boolean[] isSelected;
	static int win;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			win = 0;
			gyuyeong = new int[9];
			inyeong = new int[9];
			deck = new int[9];
			exist = new boolean[18];
			isSelected = new boolean[9];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < 9; i++) {
				gyuyeong[i] = Integer.parseInt(st.nextToken());
				exist[gyuyeong[i] - 1] = true;
			}
			int idx = 0;
			for (int i = 0; i < 18; i++) {
				if (exist[i]) {
					continue;
				}
				deck[idx++] = i + 1;
			}
			dfs(0);
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(win)
					.append(" ")
					.append(362880 - win) // 9!
					.append("\n");
		}
		System.out.println(sb);
	}

	public static void dfs(final int count) {
		if (count == 9) {
			int gyuyeongPoint = 0;
			int inyeongPoint = 0;
			for (int i = 0; i < 9; i++) {
				if (gyuyeong[i] > inyeong[i]) {
					gyuyeongPoint += gyuyeong[i] + inyeong[i];
					continue;
				}
				inyeongPoint += gyuyeong[i] + inyeong[i];
			}
			if (gyuyeongPoint > inyeongPoint) {
				win++;
			}
			return;
		}
		for (int i = 0; i < 9; i++) {
			if (isSelected[i]) {
				continue;
			}
			inyeong[count] = deck[i];
			isSelected[i] = true;
			dfs(count + 1);
			isSelected[i] = false;
		}
	}
}