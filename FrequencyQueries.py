# You are given q queries. Each query is of the form two integers described below:
# - 1 x : Insert x in your data structure.
# - 2 y : Delete one occurrence of y from your data structure, if present.
# - 3 z : Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.
#
# The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation,
# and queries[i][1] contains the data element. For example, you are given array
# queries = [(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)]. The results of each operation are:
#
# Operation   Array   Output
# (1,1)       [1]
# (2,2)       [1]
# (3,2)                   0
# (1,1)       [1,1]
# (1,1)       [1,1,1]
# (2,1)       [1,1]
# (3,2)                   1
# Return an array with the output: [0,1].
#
# Input Format
#
# The first line contains of an integer q, the number of queries.
# Each of the next q lines contains two integers denoting the 2-d array queries.
#
# Constraints
#
# * 1 <= q <= 10^6
# * 1 <= x,y,z <= 10^9
# * All queries[i][0] E {1, 2, 3}
# * 1 <= queries[i][1] <= 10^9
# Output Format
#
# Return an integer array consisting of all the outputs of queries of type 3.


def freq_query(queries):
    """
    :param queries:
    :return:
    """
    data, output = {}, []
    for query in queries:
        if query[0] == 1:
            if query[1] in data.keys():
                data[query[1]] += 1
            else:
                data[query[1]] = 1
        elif query[0] == 2:
            if query[1] in data.keys():
                if data[query[1]] == 1:
                    del data[query[1]]
                else:
                    data[query[1]] -= 1
        elif query[0] == 3:
            output.append(1) if query[1] in data.values() else output.append(0)
    return output


if __name__ == '__main__':
    q = int(input().strip())
    queries, data = [], []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    ans = freq_query(queries)
    print('\n'.join(map(str, ans)))
