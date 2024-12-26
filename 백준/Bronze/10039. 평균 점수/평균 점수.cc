#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int score, sum = 0;
	for (int i = 0; i < 5; i++) {
		cin >> score;
		if (score < 40) score = 40;
		sum += score;
	}
	cout << sum / 5;
}