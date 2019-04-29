# A string is said to be a child of a another string if it can be formed by deleting 0 or more characters from the other
# string. Given two strings of equal length, what's the longest string that can be constructed such that it is a
# child of both?
#
# For example, ABCD and ABDC have two children with maximum length 3, ABC and ABD. They can be formed by eliminating
# either the D or C from both strings. Note that we will not consider ABCD as a common child because we can't
# rearrange characters and ABCD != ABDC.
#
# Input Format
#
# There is one line with two space-separated strings, s1 and s2.
#
# Constraints
#
# * 1 <= |s1|, |s2| <= 5000
# * All characters are upper case in the range ascii[A-Z].


def common_child(s1, s2):
    """
    :param s1:
    :param s2:
    :return:
    """
    matrix = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
            if s1[j-1] == s2[i-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])
    return matrix[len(s1)][len(s2)]


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(common_child(s1, s2))
