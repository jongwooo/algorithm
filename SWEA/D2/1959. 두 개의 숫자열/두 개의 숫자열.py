import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    static int T, N, M;
    static int tempSum, max;
    static int[] A, B;
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= T; test_case++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            A = new int[N];
            B = new int[M];
            max = 0;
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                A[i] = Integer.parseInt(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                B[j] = Integer.parseInt(st.nextToken());
            }
            if (N > M) {
                int temp = N;
                N = M;
                M = temp;
                int[] tempArr = A;
                A = B;
                B = tempArr;
            }
            for (int i = 0; i <= Math.abs(M - N); i++) {
                tempSum = 0;
                for (int j = 0; j < N; j++) {
                    tempSum += A[j] * B[i + j];
                }
                if (max < tempSum) {
                    max = tempSum;
                }
            }
            sb.append('#')
                    .append(test_case)
                    .append(' ')
                    .append(max)
                    .append('\n');
        }
        System.out.println(sb);
    }
}
