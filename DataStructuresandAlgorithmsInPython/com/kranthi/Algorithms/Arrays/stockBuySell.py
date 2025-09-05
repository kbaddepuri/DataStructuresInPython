def stockBuySell(arr):
    n = len(arr)

    if n == 1:
        return arr[0]

    i = 0
    profit = 0

    while i < (n - 1):
        # find local min
        while i < (n - 1) and arr[i] >= arr[i + 1]:
            i += 1

        buy = i

        # find local max
        while i < (n - 1) and arr[i] <= arr[i + 1]:
            i += 1

        sell = i

        print(f"Buy on day: {buy+1} and Sell on day: {sell+1}")
        profit += arr[sell] - arr[buy]

    print(f"Total Profit: {profit}")


price = [100, 180, 260, 310, 40, 535, 695]
stockBuySell(price)
