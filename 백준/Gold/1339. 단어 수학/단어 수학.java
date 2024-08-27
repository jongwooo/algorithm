import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Map;

public class Main {
	
	static int N;
	static String[] terms;
	static int[] alphabets;
	static int maxDepth;
	static int[] alphabetToNum;
	static boolean[] visited;
	static int result;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		terms = new String[N];
		alphabets = new int[26];
		maxDepth = 0;
		for (int i = 0; i < N; i++) {
			terms[i] = br.readLine().trim();
			for (final char c : terms[i].toCharArray()) {
				if (alphabets[c - 'A'] == 0) {
					maxDepth++;
				}
				alphabets[c - 'A']++;
			}
		}
		alphabetToNum = new int[26];
		visited = new boolean[26];
		dfs(0, 9);
		System.out.println(result);
	}
	
	private static void dfs(final int depth, final int num) {
		if (depth == maxDepth) {
			int sum = 0;
			for (final String term : terms) {
				final char[] termToChar = term.toCharArray();
				int temp = 0;
				int digit = 1;
				for (int i = termToChar.length - 1; i >= 0; i--) {
					temp += alphabetToNum[termToChar[i] - 'A'] * digit;
					digit *= 10;
				}
				sum += temp;
			}
			if (result < sum) {
				result = sum;
			}
			return;
		}
		for (int i = 0; i < 26; i++) {
			if (alphabets[i] == 0 || visited[i]) {
				continue;
			}
			visited[i] = true;
			alphabetToNum[i] = num;
			dfs(depth + 1, num - 1);
			visited[i] = false;
			alphabetToNum[i] = 0;
		}
	}
}
