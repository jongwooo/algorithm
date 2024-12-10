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
	int day = (v - b) / (a - b);
	if ((v - b) % (a - b)) day++;
	cout << day;
}