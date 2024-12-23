#include <iostream>
#include <algorithm>
#include <string>
#include <unordered_map>
using namespace std;

int n, m;
string word;
string voca[100'000];
unordered_map<string, int> freq;

bool compare(string a, string b) {
	if (freq[a] != freq[b]) return freq[a] > freq[b];
	if (a.size() != b.size()) return a.size() > b.size();
	return a < b;
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n >> m;
	int index = 0;
	for (int i = 0; i < n; i++) {
		cin >> word;
		if ((int)word.size() < m) continue;
		if (freq.find(word) == freq.end()) {
			freq[word] = 0;
			voca[index++] = word;
		}
		freq[word]++;
	}
	sort(voca, voca + index, compare);
	for (int i = 0; i < index; i++) {
		cout << voca[i] << '\n';
	}
}