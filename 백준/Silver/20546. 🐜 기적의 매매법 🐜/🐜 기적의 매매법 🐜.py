money = int(input())
stock_prices = list(map(int, input().split()))
junhyeon_budget, seongmin_budget = money, money
junhyeon_stock, seongmin_stock = 0, 0

for day in range(14):
    today_stock_price = stock_prices[day]

    if junhyeon_budget // today_stock_price > 0:
        junhyeon_stock += junhyeon_budget // today_stock_price
        junhyeon_budget -= (junhyeon_budget // today_stock_price) * today_stock_price

    if day > 2:
        three_day_chart = stock_prices[day - 3:day]
        if three_day_chart[0] < three_day_chart[1] < three_day_chart[2]:
            seongmin_budget += seongmin_stock * today_stock_price
            seongmin_stock = 0
        elif three_day_chart[2] < three_day_chart[1] < three_day_chart[0]:
            if seongmin_budget // today_stock_price > 0:
                seongmin_stock += seongmin_budget // today_stock_price
                seongmin_budget -= (seongmin_budget // today_stock_price) * today_stock_price

junhyeon_budget += junhyeon_stock * stock_prices[-1]
seongmin_budget += seongmin_stock * stock_prices[-1]

if seongmin_budget < junhyeon_budget:
    print("BNP")
elif junhyeon_budget < seongmin_budget:
    print("TIMING")
else:
    print("SAMESAME")
