# Given an array of integers, find the sum of its elements.
#
# For example, if the array ar = [1, 2, 3], 1 + 2 + 3 = 6, so return 6.
#
# Input Format
#
# The first line contains an integer, n, denoting the size of the array.
# The second line contains n space-separated integers representing the array's elements.
#
# Constraints
#
# * 0 <= n, ar[i] <= 1000
#
# Output Format
#
# Print the sum of the array's elements as a single integer.


def simple_array_sum(ar):
    """
    :param ar: array of numbers
    :return:
    """
    sum = 0
    for i in range(len(ar)):
        sum += ar[i]
    return sum


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    print(simple_array_sum(ar))
