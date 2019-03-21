# You are given an array and you need to find number of tripets of indices (i, j, k)
# such that the elements at those indices are in geometric progression for a given common ratio r and i < j < k.
#
# For example, arr = [1, 4, 16, 64]. If r = 4, we have [1, 4, 16] and [4, 16, 64] at indices (0, 1, 2) and (1, 2, 3).
#
# countTriplets has the following parameter(s):
#
# arr: an array of integers
# r: an integer, the common ratio
#
# Input Format
#
# The first line contains two space-separated integers n and r, the size of arr and the common ratio.
# The next line contains n space-separated integers arr[i].
#
# Constraints
#
# * 1 <= n <= 10^5
# * 1 <= r <= 10^9
# * 1 <= arr[i] <= 10^9
#
# Output Format
#
# Return the count of triplets that form a geometric progression.
from collections import defaultdict


def count_triplets(arr, r):
    """
    :param arr: array of numbers
    :param r: common ratio
    :return: number of triplets
    """
    m1, m2 = defaultdict(int), defaultdict(int)
    triplets = 0
    for number in reversed(arr):
        if (number * r) in m2:
            triplets += m2[number * r]
        if (number * r) in m1:
            m2[number] += m1[number * r]
        m1[number] += 1
    return triplets


if __name__ == '__main__':
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = count_triplets(arr, r)
    print(ans)
