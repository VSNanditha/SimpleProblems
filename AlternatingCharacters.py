# You are given a string containing characters A and B only.
# Your task is to change it into a string such that there are no matching adjacent characters.
# To do this, you are allowed to delete zero or more characters in the string.
#
# Your task is to find the minimum number of required deletions.
#
# For example, given the string s = AABAAB, remove an A at positions 0 and 3 to make s = ABAB in 2 deletions.
#
# Input Format
#
# The first line contains an integer q, the number of queries.
# The next q lines each contain a string s.
#
# Constraints
#
# * 1 <= q <= 10
# * 1 <= |s| <= 10^5
# * Each string s will consist only of characters A and B



def alternating_characters(s):
    """
    :param s:
    :return:
    """
    count = 0
    list_s = list(s)
    current = s[0]
    for i in range(1, len(list_s)):
        if list_s[i] == current:
            count += 1
        else:
            current = list_s[i]
    return count


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        print(alternating_characters(s))
