'''

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock. You're also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as you like.

For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since you could buy the stock at 1 dollar, and sell at 8 dollars, and then buy it at 4 dollars and sell it at 10 dollars. Since we did two transactions, there is a 4 dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees.

'''

prices = [10, 3, 2, 8, 5, 12]

def max_price (n, fee)
    # assume list is numericals
    current_max = 0
    hold = n[0]

    history = []
    for p in n[1:]:
        current_max = max (current_max, n[p]-hold-fee)
        hold = max(hold, current_max-p)
        history.append (current_max, hold)
    return current_max, history

profit, history = max_price(prices)
print (profit)
print (history)
