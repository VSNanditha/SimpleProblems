# You will be given a list of integers, arr, and a single integer k. You must create an array of length k from
# elements of arr such that its unfairness is minimized. Call that array subarr. Unfairness of an array is calculated as
#                                   max(subarr) - min(subarr)
# Where:
# - max denotes the largest integer in subarr.
# - min denotes the smallest integer in subarr.
#
# As an example, consider the array [1, 4, 7, 2] with a k of 2. Pick any two elements, test subarr = [4, 7].
# unfairness = max(4, 7) - min(4, 7) = 7 - 4 = 3
#
# Testing for all pairs, the solution [1, 2] provides the minimum unfairness.
#
# Note: Integers in arr may not be unique.
#
# Input Format
#
# The first line contains an integer n, the number of elements in array arr.
# The second line contains an integer k.
# Each of the next n lines contains an integer arr[i] where 0 <= i <= n.
#
# Constraints
# 2 <= n <= 10^5
# 2 <= k <= n
# 0 <= arr[i] <= 10^9


def max_min(k, arr):
    """
    :param k: window size
    :param arr: list of numbers
    :return: minimum unfairness
    """
    arr.sort()
    min_unfairness = max(arr[:k]) - min(arr[:k])
    for i in range(1, len(arr)-k+1):
        min_unfairness = max(arr[i:i+k]) - min(arr[i:i+k]) if (max(arr[i:i+k]) - min(arr[i:i+k])) < min_unfairness \
            else min_unfairness
        print(max(arr[i:i+k]) - min(arr[i:i+k]), min_unfairness, arr[i:i+k])
        if min_unfairness == 0:
            break
    return min_unfairness


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)
    print(max_min(k, arr))
