# Given five positive integers, find the minimum and maximum values that can be calculated by summing
# exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#
# For example, arr = [1, 3, 5, 7, 9]. Our minimum sum is 1 + 3 + 5 + 7 = 16 and our maximum sum is 3 + 5 + 7 + 9 = 24.
# We would print
#
# 16 24
#
# Input Format
#
# A single line of five space-separated integers.
#
# Constraints
#
# * 1 <= arr[i] <= 10^9


def mini_max_sum(arr):
    """
    :param arr: list of numbers
    :return:
    """
    arr.sort()
    min = arr[0] + arr[1] + arr[2] + arr[3]
    max = arr[1] + arr[2] + arr[3] + arr[4]
    print(min, max)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    mini_max_sum(arr)
