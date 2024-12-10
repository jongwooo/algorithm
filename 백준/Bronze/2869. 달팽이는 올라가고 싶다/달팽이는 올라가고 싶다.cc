#include <iostream>

using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int a, b, v;
	cin >> a >> b >> v;
	if (v == a) {
		cout << "1";
		return 0;
	}
	int day = 1;
	day += (v - a) / (a - b);
	if ((v - a) % (a - b)) day++;
	cout << day;
}