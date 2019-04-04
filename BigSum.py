# Calculate and print the sum of the elements in an array,
# keeping in mind that some of those integers may be quite large.
#
# Input Format
#
# The first line of the input consists of an integer n.
# The next line contains n space-separated integers contained in the array.
#
# Output Format
#
# Print the integer sum of the elements in the array.
#
# Constraints
# * 1 <= n <= 10
# * 0 <= ar[i] <= 10^10


def big_sum(ar):
    """
    :param ar: array of the numbers
    :return: sum of the array elements
    """
    sum = 0
    for element in ar:
        sum += element
    return sum


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    print(big_sum(ar))
