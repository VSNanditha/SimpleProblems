# Given two strings, determine if they share a common substring. A substring may be as small as one character.
#
# For example, the words "a", "and", "art" share the common substring a.
# The words "be" and "cat" do not share a substring.
#
# twoStrings has the following parameter(s):
#
# s1, s2: two strings to analyze.
#
# Input Format
#
# The first line contains a single integer p, the number of test cases.
#
# The following p pairs of lines are as follows:
#
# The first line contains string s1.
# The second line contains string s2.
# Constraints
#
# * s1 and s2 consist of characters in the range ascii[a-z].
# * 1 <= p <= 10
# * 1 <= |s1|, |s2| <= 10^5
#
# Output Format
#
# For each pair of strings, return YES or NO.


def two_strings(s1, s2):
    """
    :param s1: string 1
    :param s2: string 2
    :return:
    """
    s1_dict = {}
    for char in s1:
        s1_dict[char] = char
    for char in s2:
        if char in s1_dict.keys():
            return 'YES'
        else:
            continue
    return 'NO'


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = two_strings(s1, s2)
