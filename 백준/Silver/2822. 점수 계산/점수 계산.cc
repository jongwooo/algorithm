#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int inputScore[8] = { 0, };
	vector<int> score;
	for (int i = 0; i < 8; i++) {
		cin >> inputScore[i];
		score.emplace_back(inputScore[i]);
	}
	sort(inputScore, inputScore + 8, greater<int>());
	int sum = 0;
	int index[5] = { 0, };
	for (int i = 0; i < 5; i++) {
		sum += inputScore[i];
		int idx = find(score.begin(), score.end(), inputScore[i]) - score.begin();
		index[i] = idx + 1;
	}
	sort(index, index + 5);
	cout << sum << '\n';
	for (int i = 0; i < 5; i++) {
		cout << index[i] << ' ';
	}
}