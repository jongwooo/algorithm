#include <iostream>
#include <string>
using namespace std;

struct Time {
	int h;
	int m;
	int s;
};

Time toTime(string s) {
	return Time{
		stoi(s.substr(0, 2)),
		stoi(s.substr(3, 2)),
		stoi(s.substr(6, 2))
	};
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	string cur, start;
	cin >> cur >> start;
	Time curTime = toTime(cur);
	Time startTime = toTime(start);
	Time res;
	res.s = startTime.s - curTime.s;
	if (res.s < 0) {
		res.s += 60;
		startTime.m--;
	}
	res.m = startTime.m - curTime.m;
	if (res.m < 0) {
		res.m += 60;
		startTime.h--;
	}
	res.h = startTime.h - curTime.h;
	if (res.h < 0) res.h += 24;
	string hour = to_string(res.h);
	string minute = to_string(res.m);
	string second = to_string(res.s);
	if (hour.size() == 1) hour = '0' + hour;
	if (minute.size() == 1) minute = '0' + minute;
	if (second.size() == 1) second = '0' + second;
	cout << hour << ':' << minute << ':' << second;
}