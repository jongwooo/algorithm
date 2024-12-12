#include <iostream>
#include <algorithm>
using namespace std;

int triangle[3];

int main() {
	cin.tie(0)->sync_with_stdio(0);

	while (true) {
		for (int i = 0; i < 3; i++) {
			cin >> triangle[i];
		}
		if (triangle[0] + triangle[1] + triangle[2] == 0) break;
		sort(triangle, triangle + 3);
		if (triangle[0] + triangle[1] <= triangle[2]) cout << "Invalid";
		else if (triangle[0] == triangle[1] && triangle[1] == triangle[2] && triangle[2] == triangle[0]) cout << "Equilateral";
		else if (triangle[0] == triangle[1] || triangle[1] == triangle[2] || triangle[2] == triangle[0]) cout << "Isosceles";
		else cout << "Scalene";
		cout << '\n';
	}
}