#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, vote, yes = 0, no = 0;
	cin >> n;
	while (n--) {
		cin >> vote;
		if (vote == 1) yes++;
		else no++;
	}
	cout << "Junhee is " << (yes > no ? "" : "not ") << "cute!";
}