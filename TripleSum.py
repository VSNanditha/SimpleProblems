# Given 3 arrays a, b, c of different sizes, find the number of distinct triplets (p, q, r) where p is an element of a,
# written as p E a, q E b, and r E c, satisfying the criteria: p <= q and q >= r.
#
# For example, given a = [3, 5, 7], b = [3, 6] and c = [4, 6, 9], we find four distinct triplets: (3, 6, 4), (3, 6, 6),
# (5, 6, 4), (5, 6, 6).
#
# Input Format
#
# The first line contains 3 integers lena, lenb and lenc, the sizes of the three arrays.
# The next 3 lines contain space-separated integers numbering lena, lenb and lenc respectively.
#
# Constraints
#
# * 1 <= lena, lenb, lenc <= 10^5
# * 1 <= all elements in a, b c <= 10^8


from bisect import bisect


def triplets(a, b, c):
    """
    :param a: array list a
    :param b: array list b
    :param c: array list c
    :return: count of triplets
    """
    a, b, c = sorted(list(set(a))), list(set(b)), sorted(list(set(c)))
    print(a,  b,  c)
    count = sum([bisect(a, b_number) * bisect(c, b_number) for b_number in b])
    return count


if __name__ == '__main__':
    lenaLenbLenc = input().split()
    lena = int(lenaLenbLenc[0])
    lenb = int(lenaLenbLenc[1])
    lenc = int(lenaLenbLenc[2])
    arra = list(map(int, input().rstrip().split()))
    arrb = list(map(int, input().rstrip().split()))
    arrc = list(map(int, input().rstrip().split()))
    ans = triplets(arra, arrb, arrc)
    print(str(ans) + '\n')
