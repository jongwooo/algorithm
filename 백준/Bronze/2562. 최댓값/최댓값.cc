#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int maxValue = -1;
	int maxValueIndex = -1;
	int num;
	for (int i = 1; i <= 9; i++) {
		cin >> num;
		if (maxValue < num) {
			maxValue = num;
			maxValueIndex = i;
		}
	}

	cout << maxValue << '\n' << maxValueIndex;
}