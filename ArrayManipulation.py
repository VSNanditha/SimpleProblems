# Starting with a 1-indexed array of zeros and a list of operations,
# for each operation add a value to each of the array element between two given indices, inclusive.
# Once all operations have been performed, return the maximum value in your array.
#
# For example, the length of your array of zeros n = 10. Your list of queries is as follows:
#
#     a b k
#     1 5 3
#     4 8 7
#     6 9 1
#
# Add the values of k between the indices a and b inclusive:
#
# index->	 1 2 3  4  5 6 7 8 9 10
# 	        [0,0,0, 0, 0,0,0,0,0, 0]
# 	        [3,3,3, 3, 3,0,0,0,0, 0]
# 	        [3,3,3,10,10,7,7,7,0, 0]
# 	        [3,3,3,10,10,8,8,8,1, 0]
# The largest value is 10 after all operations are performed.
#
# arrayManipulation has the following parameters:
#
# n - the number of elements in your array
# queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
# Input Format
#
# The first line contains two space-separated integers n and m, the size of the array and the number of operations.
# Each of the next m lines contains three space-separated integers a, b and k, the left index, right index and summand.
#
# Constraints
#
# * 3 <= n <= 10^7
# * 1 <= m <= 2 * 10^5
# * 1 <= a <= b <=n
# * 0 <= k <= 10^9
#
# Output Format
#
# Return the integer maximum value in the finished array.


def array_manipulation(n, queries):
    """
    :param n: number of elements in the array to be manipulated
    :param queries: array of start, end  indexes and changes to be made
    :return:
    """
    changes = [0] * (n+1)
    for i in range(m):
        start, end, add = queries[i][0] - 1, queries[i][1] - 1, queries[i][2]
        changes[start-1] += add
        if end <= len(changes):
            changes[end] -= add
    maximum = total = 0
    for change in changes:
        total += change
        maximum = total if total > maximum else maximum
    return maximum


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = array_manipulation(n, queries)
