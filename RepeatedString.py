# Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.
#
# Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.
#
# For example, if the string s = 'abcac' and n = 10, the substring we consider is abcacabcac,
# the first 10 characters of her infinite string. There are 4 occurrences of a in the substring.
#
# repeatedString has the following parameter(s):
#
# s: a string to repeat
# n: the number of characters to consider
# Input Format
#
# The first line contains a single string, s.
# The second line contains an integer, n.
#
# Constraints
#
# * 1 <= |s| <= 100
# * 1 <= n <= 10^12
# * for 25% of the test cases, n <= 10^6
#
# Output Format
#
# Print a single integer denoting the number of letter a's in the first n letters of the infinite string
# created by repeating s infinitely many times.


import math


def repeated_string(s, n):
    """

    :param s: input string
    :param n: number of characters to consider
    :return: number of occurences of 'a' in the string s in range n
    """
    occurrences = 0
    if s == 'a':
        return n
    for i in range(len(s)):
        if i == n:
            return occurrences
        occurrences += 1 if s[i] == 'a' else 0
    if n > len(s):
        occurrences = occurrences * math.floor(n / len(s))
        i = 0
        while i < n % len(s):
            occurrences += 1 if s[i] == 'a' else 0
            i += 1
    return occurrences


if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeated_string(s, n)
    print(result)
