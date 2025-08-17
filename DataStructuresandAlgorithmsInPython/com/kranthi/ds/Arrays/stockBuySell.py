def stockAndBySell(prices):
    n = len(prices)
    if n == 1:
        return
    i = 0
    profit = 0
    while i < (n-1):
        # find local min
        while i < (n-1) and prices[i + 1] <= prices[i]:
            i += 1
            if i == n-1:
                break
        buy = i
        i += 1

        # find local max
        while i < n and prices[i] >= prices[i-1]:
            i += 1

        sell = i-1

        print(f"Buy on day: {buy} and sell on day: {sell}")
        profit += prices[sell] - prices[buy]
    print(f"Multiple buy and sell profit: {profit}")

def maxProfilt_SecondLogic(prices):
    n = len(prices)
    if n < 2:
        return
    profit = 0
    max_profit = 0
    buy = prices[0]
    for i in range(1, n):
        if prices[i] > buy:
            diff = prices[i] - buy
            profit = max(profit, diff)

        if prices[i] < buy or i == n-1:
            max_profit = max(max_profit, profit)
            # max_profit += max(max_profit, profit) # this is for multiple times buy and sell
            profit = 0
            buy = prices[i]

    print("Buy once and sell once: ", max_profit)

price = [100, 180, 260, 310, 40, 535, 695]
stockAndBySell(price)
maxProfilt_SecondLogic(price)