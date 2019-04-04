# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#
# For example, the square matrix  is shown below:
#
# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal = 1 + 5 + 9 = 15. The right to left diagonal = 3 + 5+ 9 = 17.
# Their absolute difference is |15 - 17| = 2.
#
# Input Format
#
# The first line contains a single integer, n, the number of rows and columns in the matrix arr.
# Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j].
#
# Constraints
#
# * -100 <= ar[i][j] <= 100
#
# Output Format
#
# Print the absolute difference between the sums of the matrix's two diagonals as a single integer.


def diagonal_difference(arr):
    """
    :param arr: 2D array of elements
    :return: absolute difference between the sums of matrix's diagonals
    """
    lr_diagonal, rl_diagonal = 0, 0
    for i in range(n):
        lr_diagonal += arr[i][i]
    i, j = n-1, 0
    while i >= 0 and j < n:
        rl_diagonal += arr[i][j]
        i -= 1
        j += 1
    return abs(lr_diagonal-rl_diagonal)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    print(diagonal_difference(arr))
