#include <iostream>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	const int pieceCount[6] = { 1, 1, 2, 2, 2, 8 };

	int v;
	for (int i = 0; i < 6; i++) {
		cin >> v;
		cout << pieceCount[i] - v << " ";
	}
}