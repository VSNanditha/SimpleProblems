# Borussia Dortmund are a famous football ( soccer ) club from Germany. Apart from their fast-paced style of playing,
# the thing that makes them unique is the hard to pronounce names of their players
# ( błaszczykowski , papastathopoulos , großkreutz etc. ).
#
# The team's coach is your friend.
# He is in a dilemma as he can't decide how to make it easier to call the players by name, during practice sessions.
# So, you advise him to assign easy names to his players. A name is easy to him if
#
# 1. It consists of only one word.
# 2. It consists of only lowercase english letters.
# 3. Its length is exactly N.
# 4. It contains exactly K different letters from the 26 letters of English alphabet.
# 5. At least one of its proper prefixes matches with its proper suffix of same length.
#
# Given, N and K you have to tell him the number of easy names he can choose from modulo (10^9 + 9).
#
# Note : A prefix P of a name W is proper if, P != W. Similarly, a suffix S of a name W is proper if, S != W.
#
# Input Format
# The first line of the input will contain  T( the number of testcases ).
# Each of the next T lines will contain 2 space separated integers N and K.
#
# Output Format
# For each test case, output the number of ways the coach can assign names to his players modulo (10^9 + 9).
#
# Constraints
#
# * 1 <= T <= 10^5
# * 1 <= N <= 10^5
# * 1 <= k <= 26
import math
import itertools


def dortmund_dilemma(n, k):
    """
    :param n:
    :param k:
    :return:
    """
    if n == k or n < k:
        return 0
    if k == 1:
        return 26
    alphabet_selection = abs(math.factorial(26)/(math.factorial(26-k) * math.factorial(k)))
    arrangements = k * (pow(k, n - 2)) - k
    print('arrangements1', arrangements)
    for i in range(2, int(n/2)):
        arrangements += k * (pow(k, n - (2*i)))
        print('arrangements2', arrangements)
    if n % 2 == 0:
        arrangements += pow(k, n/2) - pow(k, n/4) if n/2 % 2 == 0 else pow(k, math.ceil(n/2)) - pow(k, math.floor(((n/2)-1)/2)+1)
    # print(pow(k, math.ceil(n/2)), pow(k, (n-1)/2), pow(k, n/2) - pow(k, n/2), n/2 % 2 == 0)
    print('arrangements3', arrangements)
    print(alphabet_selection, arrangements)
    return int(alphabet_selection * arrangements)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        print(dortmund_dilemma(n, k))
