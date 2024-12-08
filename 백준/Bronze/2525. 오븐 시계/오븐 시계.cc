#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int a, b, c;
	cin >> a >> b >> c;

	int m = a * 60 + b + c;
	int h = (m / 60) % 24;
	m %= 60;

	cout << h << " " << m;
}