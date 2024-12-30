#include <iostream>
#define MAX 16
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int v;
	cin >> v;
	char votes[MAX];
	cin >> votes;
	int a = 0, b = 0;
	for (int i = 0; i < v; i++) {
		if (votes[i] == 'A') a++;
		else b++;
	}
	if (a > b) cout << 'A';
	else if (a < b) cout << 'B';
	else cout << "Tie";
}