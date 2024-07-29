import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static int V, E;
	static int v1, v2;
	static Node[] nodes;
	static boolean[] visited;
	static int size;

	public static void main(String[] args) throws Exception {
//		System.setIn(new FileInputStream("input.txt"));
		final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		final StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		final int T = Integer.parseInt(br.readLine());
		for (int testCase = 1; testCase <= T; testCase++) {
			st = new StringTokenizer(br.readLine());
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			v1 = Integer.parseInt(st.nextToken());
			v2 = Integer.parseInt(st.nextToken());
			nodes = new Node[V + 1];
			for (int i = 1; i <= V; i++) {
				nodes[i] = new Node(i);
			}
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < E; i++) {
				final int parent = Integer.parseInt(st.nextToken());
				final int child = Integer.parseInt(st.nextToken());
				if (nodes[parent].leftChild == 0) {
					nodes[parent].leftChild = child;
				} else {
					nodes[parent].rightChild = child;
				}
				nodes[child].parent = parent;
			}
			visited = new boolean[V + 1];
			Node v1Node = nodes[v1];
			Node v2Node = nodes[v2];
			Node commonParent = nodes[1];
			while (v1Node.data != 1) {
				visited[v1Node.data] = true;
				v1Node = nodes[v1Node.parent];
			}
			while (v2Node.data != 1) {
				if (visited[v2Node.data]) {
					commonParent = v2Node;
					break;
				}
				visited[v2Node.data] = true;
				v2Node = nodes[v2Node.parent];
			}
			size = 0;
			traversal(commonParent);
			sb.append("#")
					.append(testCase)
					.append(" ")
					.append(commonParent.data)
					.append(" ")
					.append(size)
					.append("\n");
		}
		System.out.println(sb);
	}

	private static void traversal(final Node node) {
		size++;
		if (node.leftChild != 0) {
			traversal(nodes[node.leftChild]);
		}
		if (node.rightChild != 0) {
			traversal(nodes[node.rightChild]);
		}
	}
}

class Node {

	final int data;
	int parent, leftChild, rightChild;

	public Node(final int data) {
		this.data = data;
	}
}
