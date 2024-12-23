#include <iostream>
using namespace std;

int n, k, cnt = 0, res = -1;
int* a;
int* tmp;

void merge(int a[], int p, int q, int r) {
	int i = p;
	int j = q + 1;
	int t = 1;
	while (i <= q && j <= r) {
		if (a[i] <= a[j]) tmp[t++] = a[i++];
		else tmp[t++] = a[j++];
	}
	while (i <= q) {
		tmp[t++] = a[i++];
	}
	while (j <= r) {
		tmp[t++] = a[j++];
	}
	i = p;
	t = 1;
	while (i <= r) {
		a[i++] = tmp[t++];
		cnt++;
		if (cnt == k) {
			res = a[i - 1];
			break;
		}
	}
}

void merge_sort(int a[], int p, int r) {
	if (p < r) {
		int q = (p + r) / 2;
		merge_sort(a, p, q);
		merge_sort(a, q + 1, r);
		merge(a, p, q, r);
	}
}

int main() {
	cin.tie(0)->sync_with_stdio(0);

	cin >> n >> k;
	a = new int[n + 1];
	tmp = new int[n + 1];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	merge_sort(a, 0, n - 1);
	cout << res;
	delete[] a;
	delete[] tmp;
}