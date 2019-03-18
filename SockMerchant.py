# Problem
#
# John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
# Given an array of integers representing the color of each sock, determine how many pairs of socks
# with matching colors there are.

# For example, there are n = 7 socks with colors ar = [1, 2, 1, 2, 1, 3, 2].
# There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color.
# The number of pairs is 2.
#
# Function Description
#
# The sockMerchant function must return an integer representing the number
# of matching pairs of socks that are available.
#
# sockMerchant has the following parameter(s):
#
# n: the number of socks in the pile
# ar: the colors of each sock
#
# Input Format
#
# The first line contains an integer n, the number of socks represented in ar.
# The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile.
#
# Constraints
#
# * 1 <= n <= 100
# * 1 <= ar[i] <= 100 where i 0<= i < n
#
# Output Format
#
# Return the total number of matching pairs of socks that John can sell.


def sock_merchant(n, ar):
    """

    :param n: number of socks
    :param ar: array of colors of the socks available
    :return: number of matching color pairs of socks that can be sold
    """
    ar.sort()
    count, i = 0, 0
    print(n, ar)
    while i + 1 < n:
        print(i, i+1)
        if ar[i] == ar[i + 1]:
            count += 1
            i += 2
        else:
            i += 1
    return count


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sock_merchant(n, ar)
    print(result)
