# Consider a staircase of size :
#
#    #
#   ##
#  ###
# ####
#
# Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces.
# The last line is not preceded by any spaces.
#
# Write a program that prints a staircase of size n.
#
# Input Format
#
# A single integer, n, denoting the size of the staircase.
#
# Constraints
#
#  * 0 < n <= 100.


def staircase(n):
    """
    :param n: number of stairs
    :return:
    """
    for i in range(1, n+1):
        for j in range(n-i, 0, -1):
            print(' ', end='')
        print('#' * i)


if __name__ == '__main__':
    n = int(input())
    staircase(n)
