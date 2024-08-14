import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		for (int testCase = 1; testCase <= 10; testCase++) {
			final int n = Integer.parseInt(br.readLine());
			final char[] parentheses = br.readLine()
					.toCharArray();
			final Stack<Character> stack = new Stack<>();
			for (int i = 0; i < n; i++) {
				if (parentheses[i] == '(' || parentheses[i] == '{' || parentheses[i] == '[' || parentheses[i] == '<') {
					stack.add(parentheses[i]);
					continue;
				}
				if (parentheses[i] == ')' && stack.peek() == '(') {
					stack.pop();
					continue;
				}
				if (parentheses[i] == '}' && stack.peek() == '{') {
					stack.pop();
					continue;
				}
				if (parentheses[i] == ']' && stack.peek() == '[') {
					stack.pop();
					continue;
				}
				if (parentheses[i] == '>' && stack.peek() == '<') {
					stack.pop();
					continue;
				}
				break;
			}
			int result = 0;
			if (stack.isEmpty()) {
				result = 1;
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