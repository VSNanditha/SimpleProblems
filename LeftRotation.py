# Problem
#
# A left rotation operation on an array shifts each of the array's elements 1 unit to the left.
# For example, if 2 left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].
#
# Given an array a of n integers and a number, d, perform d left rotations on the array.
# Return the updated array to be printed as a single line of space-separated integers.
#
# Function Description
#
# Complete the function rotLeft in the editor below. It should return the resulting array of integers.
#
# rotLeft has the following parameter(s):
#
# An array of integers a.
# An integer d, the number of rotations.
#
# Input Format
#
# The first line contains two space-separated integers n and d,
# the size of a and the number of left rotations you must perform.
# The second line contains n space-separated integers a[i].
#
# Constraints
#
# * 1 <= n <= 10^5
# * 1 <= d <= n
# * 1 <= a[i] <= 10^6
#
# Output Format
#
# Print a single line of n space-separated integers denoting the final
# state of the array after performing d left rotations.


def rot_left(a, d):
    """

    :param a: input array of integers
    :param d: number of rotations
    :return: resultant array after d rotations
    """
    temp, new = [], []
    for rot in range(d):
        temp.append(a[rot])
    for i in range(d, len(a)):
        new.append(a[i])
    new = new + temp
    return new


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))
    result = rot_left(a, d)
    print(' '.join(map(str, result)))
