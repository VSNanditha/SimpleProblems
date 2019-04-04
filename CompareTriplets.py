# Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges,
# awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.
#
# We define the rating for Alice's challenge to be the triplet a = (a[0], a[1], a[2]),
# and the rating for Bob's challenge to be the triplet b = (b[0], b[1], b[2]).
#
# Your task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].
#
# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.
# Comparison points is the total points a person earned.
#
# Given a and b, determine their respective comparison points.
#
# Input Format
#
# The first line contains 3 space-separated integers, a[0], a[1], and a[2],
# describing the respective values in triplet a.
#
# The second line contains 3 space-separated integers, b[0], b[1], and b[2],
# describing the respective values in triplet b.
#
# Constraints
#
# * 1 <= a[i] <= 100
# * 1 <= b[i] <= 100
#
# Output Format
#
# Return an array of two integers denoting the respective comparison points earned by Alice and Bob.


def compare_triplets(a, b):
    """
    :param a: Alice's scores
    :param b: Bob's scores
    :return:
    """
    alice_score, bob_score = 0, 0
    for i in range(3):
        if a[i] < b[i]:
            bob_score += 1
        elif a[i] > b[i]:
            alice_score += 1
    return [alice_score, bob_score]


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    print(' '.join(map(str, compare_triplets(a, b))))
