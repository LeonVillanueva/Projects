'''
In front of you is a row of N coins, with values v1, v1, ..., vn.

You are asked to play the following game. You and an opponent take turns choosing either the first or last coin from the row, removing it from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty, if you move first, assuming your opponent plays optimally.
'''

def max_profit(coins, value):
    n = len(coins)
    profit = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        profit[i][i] = coins[i]

    for i in range(n - 1):
        profit[i][i + 1] = max(profit[i][i], profit[i + 1][i + 1])

    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            left = profit[i][j - 2]
            diagonal = profit[i + 1][j - 1]
            bottom = profit[i + 2][j]
            profit[i][i + gap] = max(
                coins[i] + min(diagonal, bottom),
                coins[j] + min(left, diagonal)
            )

    return profit[0][-1]
