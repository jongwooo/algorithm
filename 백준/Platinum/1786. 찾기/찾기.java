import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	static BufferedReader br;
	static StringBuilder sb;

	static String T;
	static String P;
	static int count;

	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		T = br.readLine();
		P = br.readLine();
		count = 0;
		initializeTable(P);
		KMP(T, P);
		System.out.println(count);
		System.out.println(sb);
	}

	private static void KMP(String parent, String pattern) {
		final int[] table = initializeTable(pattern);
		final int n1 = parent.length();
		final int n2 = pattern.length();
		int begin = 0;
		int matched = 0;
		while (begin <= n1 - n2) {
			if (matched < n2 && parent.charAt(begin + matched) == pattern.charAt(matched)) {
				matched++;
				if (matched == n2) {
					sb.append((begin + 1) + " ");
					count++;
				}
			} else {
				if (matched == 0) {
					begin++;
				} else {
					begin += matched - table[matched - 1];
					matched = table[matched - 1];
				}
			}
		}
	}

	private static int[] initializeTable(final String pattern) {
		final int n = pattern.length();
		final int[] table = new int[n];
		int idx = 0;
		for (int i = 1; i < n; i++) {
			while (idx > 0 && pattern.charAt(i) != pattern.charAt(idx)) {
				idx = table[idx - 1];
			}
			if (pattern.charAt(i) == pattern.charAt(idx)) {
				idx++;
				table[i] = idx;
			}
		}
		return table;
	}
}
