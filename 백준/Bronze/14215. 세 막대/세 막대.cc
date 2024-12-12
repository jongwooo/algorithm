#include <iostream>
#include <algorithm>
using namespace std;

int edges[3];

int main() {
	cin.tie(0)->sync_with_stdio(0);

	for (int i = 0; i < 3; i++) {
		cin >> edges[i];
	}
	sort(edges, edges + 3);
	cout << edges[0] + edges[1] + min({ edges[2], edges[0] + edges[1] - 1 });
}