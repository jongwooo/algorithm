#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n, maxPrice = 0;;
	cin >> n;
	while (n--) {
		int dice[3];
		for (int i = 0; i < 3; i++) {
			cin >> dice[i];
		}
		sort(dice, dice + 3);
		int price = 0;
		if (dice[0] == dice[2]) price = 10'000 + dice[0] * 1'000;
		else if (dice[0] == dice[1] || dice[1] == dice[2]) price = 1'000 + dice[1] * 100;
		else price = dice[2] * 100;
		if (maxPrice < price) maxPrice = price;
	}
	cout << maxPrice;
}