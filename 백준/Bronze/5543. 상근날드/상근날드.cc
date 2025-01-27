#include <iostream>
using namespace std;

int main() {
	cin.tie(0)->sync_with_stdio(0);

	int minBurgerPrice = 2'000;
	int minDrinkPrice = 2'000;
	for (int i = 0; i < 3; i++) {
		int burgerPrice;
		cin >> burgerPrice;
		if (burgerPrice < minBurgerPrice) minBurgerPrice = burgerPrice;
	}
	for (int i = 0; i < 2; i++) {
		int drinkPrice;
		cin >> drinkPrice;
		if (drinkPrice < minDrinkPrice) minDrinkPrice = drinkPrice;
	}
	cout << minBurgerPrice + minDrinkPrice - 50;
}