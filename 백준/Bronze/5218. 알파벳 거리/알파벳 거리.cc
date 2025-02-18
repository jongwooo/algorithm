#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		string x, y;
		cin >> x >> y;
		cout << "Distances: ";
		for (int j = 0; j < x.length(); j++) {
			int xpos = x[j] - 'A';
			int ypos = y[j] - 'A';
			if (ypos - xpos >= 0) cout << ypos - xpos << ' ';
			else cout << ypos - xpos + 26 << ' ';
		}
		cout << '\n';
	}
}