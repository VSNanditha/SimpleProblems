# Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some.
# There are a number of different toys lying in front of him, tagged with their prices.
# Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.
# Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy?
# For example, if prices = [1, 2, 3, 4] and Mark has k = 7 to spend, he can buy items [1, 2, 3] for 6,
# or [3, 7] for 7 units of currency. He would choose the first group of 3 items.
#
# Input Format
# The first line contains two integers, n and k, the number of priced toys and the amount Mark has to spend.
# The next line contains n space-separated integers prices[i].
#
# Constraints
# * 1 <= n <= 10^5
# * 1 <= k <= 10^9
# * 1 <= prices[i] <= 10^9
# A toy can't be bought multiple times.
#
# Output Format
# An integer that denotes the maximum number of toys Mark can buy for his son.


def maximumToys(prices, k):
    """
    :param prices:
    :param k:
    :return:
    """
    prices.sort()
    print(prices)
    max_price, i = 0, 0
    while max_price <= k and i < len(prices):
        print(max_price, i)
        max_price += prices[i]
        i += 1
    return i - 1


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    print(maximumToys(prices, k))
