import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int N, L;
	static int[] points;
	static int[] calories;
	static int[] array;
	static int result;

	public static void main(String[] args) throws Exception {
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			L = Integer.parseInt(st.nextToken());
			points = new int[N];
			calories = new int[N];
			result = 0;
			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				points[i] = Integer.parseInt(st.nextToken());
				calories[i] = Integer.parseInt(st.nextToken());
			}
			for (int i = 1; i <= N; i++) {
				array = new int[N];
				for (int j = array.length - 1; j > array.length - 1 - i; --j) {
					array[j] = 1;
				}
				combine();
			}
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(result)
					.append("\n");
		}
		System.out.println(sb);
	}

	private static void combine() {
		do {
			int point = 0;
			int calorie = 0;
			for (int i = 0; i < N; i++) {
				if (array[i] == 1) {
					point += points[i];
					calorie += calories[i];
				}
			}
			if (calorie > L) {
				continue;
			}
			if (result < point) {
				result = point;
			}
		} while (nextPermutation());
	}

	private static boolean nextPermutation() {
		int length = array.length;
		int top = length - 1;
		while (top > 0 && array[top - 1] >= array[top]) {
			top--;
		}
		if (top == 0) {
			return false;
		}
		int right = length - 1;
		while (array[top - 1] >= array[right]) {
			right--;
		}
		swap(top - 1, right);
		right = length - 1;
		while (top < right) {
			swap(top++, right--);
		}
		return true;
	}

	private static void swap(final int index1, final int index2) {
		final int temp = array[index1];
		array[index1] = array[index2];
		array[index2] = temp;
	}
}