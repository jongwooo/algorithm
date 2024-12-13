#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

struct Person {
	int age;
	string name;
};

bool compare(const Person& p1, const Person& p2) {
	if (p1.age != p2.age) return p1.age < p2.age;
	return false;
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int n;
	cin >> n;
	Person persons[100001];
	for (int i = 0; i < n; i++) {
		cin >> persons[i].age >> persons[i].name;
	}
	stable_sort(persons, persons + n, compare);
	for (int i = 0; i < n; i++) {
		cout << persons[i].age << ' ' << persons[i].name << '\n';
	}
}