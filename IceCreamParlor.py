# Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream.
# On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.
#
# Given the value of money and the cost of each flavor for t trips to the Ice Cream Parlor, help Sunny and Johnny
# choose two distinct flavors such that they spend their entire pool of money during each visit.
# ID numbers are the 1- based index number associated with a cost. For each trip to the parlor, print the ID numbers
# for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line.
# You must print the smaller ID first and the larger ID second.
#
# For example, there are n = 5 flavors having cost = [2, 1, 3, 5, 6]. Together they have money = 5 to spend.
# They would purchase flavor ID's 1 and 3 for a cost of 2 + 3 = 5.
# Use 1 based indexing for your response.
#
# Note:
#
# Two ice creams having unique IDs i and j may have the same cost (i.e., cost[i] = cost[j]).
# There will always be a unique solution.
#
# Input Format
#
# The first line contains an integer, t, the number of trips to the ice cream parlor.
#
# Each of the next t sets of 3 lines is as follows:
#
# The first line contains money.
# The second line contains an integer, n, the size of the array cost.
# The third line contains n space-separated integers denoting the cost[i].
#
# Constraints
#
# * 1 <= t <= 50
# * 2 <= money <= 10^9
# * 2 <= n <= 5 * 10^4
# * 1 <= cost[i] <= 10^9


def what_flavors(cost, money):
    """
    :param cost: list of costs of available flavors
    :param money: money available with Sunny and Johnny
    :return: flavors that can be bought with money
    """
    values = {}
    for i in range(len(cost)):
        if money - cost[i] in values:
            return i+1, values[money - cost[i]] + 1
        values[cost[i]] = i


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        money = int(input())
        n = int(input())
        cost = list(map(int, input().rstrip().split()))
        print(' '.join(map(str(what_flavors(cost, money)))))
