# You are given an unordered array consisting of consecutive integers 🇻🇪⍷ [1, 2, 3, ..., n] without any duplicates.
# You are allowed to swap any two elements.
# You need to find the minimum number of swaps required to sort the array in ascending order.
#
# For example, given the array arr = [7, 1, 3, 2, 4, 5, 6] we perform the following steps:
#
# i   arr                     swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]
# It took 5 swaps to sort the array.
#
# minimumSwaps has the following parameter(s):
#
# arr: an unordered array of integers
#
# Input Format
#
# The first line contains an integer, n, the size of arr.
# The second line contains n space-separated integers arr[i].
#
# Constraints
#
# * 1 <= n <= 10^5
# * 1 <= arr[i] <= n
#
# Output Format
#
# Return the minimum number of swaps to sort the given array.


def minimum_swaps(arr):
    """
    :param arr: array of elements
    :return: number of swaps
    """
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key=lambda it: it[1])
    vis = {k: False for k in range(n)}
    swaps = 0
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            swaps += (cycle_size - 1)
    return swaps


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimum_swaps(arr)
    print(res)
