# You are in charge of the cake for your niece's birthday and have decided the cake will have one candle
# for each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones.
# Your task is to find out how many candles she can successfully blow out.
#
# For example, if your niece is turning 4 years old, and the cake will have 4 candles of height 4, 4, 1, 3,
# she will be able to blow out 2 candles successfully, since the tallest candles are of height 4
# and there are  such candles.
#
# Input Format
#
# The first line contains a single integer, n, denoting the number of candles on the cake.
# The second line contains n space-separated integers, where each integer i describes the height of candle i.
#
# Constraints
# * 1 <= n <= 10^5
# * 1 <= ar[i] <= 10^7


def birthday_cake_candles(ar):
    """
    :param ar: list of heights of the candles
    :return: number of candles that can be blown
    """
    ar.sort(reverse=True)
    return ar.count(ar[0])


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    print(birthday_cake_candles(ar))
