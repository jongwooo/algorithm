#include <iostream>
#include <string>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int date, month;
	cin >> date >> month;
	int daysInMonth[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	string days[7] = { "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday" };
	int totalDays = 0;
	totalDays += date;
	for (int i = 0; i < (month - 1); i++) {
		totalDays += daysInMonth[i];
	}
	cout << days[totalDays % 7];
}