import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static BufferedReader br;
	static StringBuilder sb;
	static StringTokenizer st;

	static int n, m, k;
	static long[] nums;
	static long[] segmentTree;

	public static void main(String[] args) throws Exception {
		br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());
		nums = new long[n];
		for (int i = 0; i < n; i++) {
			nums[i] = Long.parseLong(br.readLine());
		}
		segmentTree = new long[n * 4];
		init(1, n, 1);
		for (int i = 0; i < m + k; i++) {
			st = new StringTokenizer(br.readLine());
			final int a = Integer.parseInt(st.nextToken());
			final int b = Integer.parseInt(st.nextToken());
			final long c = Long.parseLong(st.nextToken());
			if (a == 1) {
				final long num = c - nums[b - 1];
				nums[b - 1] = c;
				update(1, n, 1, b, num);
			}
			if (a == 2) {
				sb.append(find(1, n, 1, b, (int) c))
						.append("\n");
			}
		}
		System.out.println(sb);
	}

	private static long init(final int start, final int end, final int index) {
		if (start == end) {
			segmentTree[index] = nums[start - 1];
			return segmentTree[index];
		}
		final int mid = (start + end) / 2;
		segmentTree[index] = init(start, mid, 2 * index) + init(mid + 1, end, 2 * index + 1);
		return segmentTree[index];
	}

	private static long find(final int start, final int end, final int index, final int left, final int right) {
		if (start > right || end < left) {
			return 0;
		}
		if (start >= left && end <= right) {
			return segmentTree[index];
		}
		final int mid = (start + end) / 2;
		return find(start, mid, 2 * index, left, right) + find(mid + 1, end, 2 * index + 1, left, right);
	}

	private static void update(final int start, final int end, final int index, final int updateIndex,
			final long data) {
		if (start > updateIndex || end < updateIndex) {
			return;
		}
		segmentTree[index] += data;
		if (start == end) {
			return;
		}
		final int mid = (start + end) / 2;
		update(start, mid, 2 * index, updateIndex, data);
		update(mid + 1, end, 2 * index + 1, updateIndex, data);
	}
}
