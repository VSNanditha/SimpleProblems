# You will be given an array of integers and a target value. Determine the number of pairs of array elements that have
# a difference equal to a target value.
#
# For example, given an array of [1, 2, 3, 4] and a target value of 1, we have three values meeting the condition:
# 2 - 1 = 1, 3 - 2 = 1, and 4 - 3 = 1.
#
# Input Format
#
# The first line contains two space-separated integers n and k, the size of arr and the target value.
# The second line contains n space-separated integers of the array arr.
#
# Constraints
# * 2 <= n <= 10^5
# * 0 <= k <= 10^9
# * 0 <= arr[i] <= 2^31 - 1
# * each integer arr[i] will be unique


def pairs(k, arr):
    """
    :param k: difference
    :param arr: number list
    :return: number of pairs with given difference
    """
    pairs = 0
    for number in arr:
        pairs += 1 if number-k in arr else 0
    return pairs


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    print(pairs(k, arr))
