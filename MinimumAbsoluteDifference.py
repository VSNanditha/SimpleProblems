# Consider an array of integers, arr = [arr[0], arr[1] arr[2], ...., arr[n-1]].
# We define the absolute difference between two elements, a[i] and a[j] (where i != j), to be the absolute value of
# a[i] - a[j].
#
# Given an array of integers, find and print the minimum absolute difference between any two elements in the array.
# For example, given the array arr = [-2, 2, 4], we can create 3 pairs of numbers: [-2, 2], [-2, 4] and [2, 4].
# The absolute differences for these pairs are |(-2)-2| = 4, |(-2)-4| = 6 and |2 - 4| = 2.
# The minimum absolute difference is 2.
#
# Input Format
#
# The first line contains a single integer n, the size of arr.
# The second line contains n space-separated integers arr[i].
#
# Constraints
# * 2 <= n <= 10^5
# * -10^9 <= arr[i] <= 10^9


def minimum_absolute_difference(arr):
    """
    :param arr: input array of numbers
    :return:
    """
    arr.sort()
    min_diff = abs(arr[0] - arr[1])
    for i in range(1, len(arr)-1):
        # print(min_diff)
        if min_diff > abs(arr[i] - arr[i+1]):
            min_diff = abs(arr[i] - arr[i+1])
        if min_diff == 0:
            break
    return min_diff


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(minimum_absolute_difference(arr))
