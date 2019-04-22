# Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams
# of each other if the first string's letters can be rearranged to form the second string.
# In other words, both strings must contain the same exact letters in the same exact frequency For example,
# bacdc and dcbac are anagrams, but bacdc and dcbad are not.
#
# Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number
# of character deletions required to make the two strings anagrams. Can you help her find this number?
#
# Given two strings, a and b, that may or may not be of the same length, determine the minimum number of character
# deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.
#
# For example, if a = cde and b = dcf, we can delete a from string a and f from string b so that both remaining strings
# are cd and dc which are anagrams.
#
# Input Format
#
# The first line contains a single string, a.
# The second line contains a single string, b.
#
# Constraints
#
# * 1 <= |a|, |b| <= 10^4
# The strings a and b consist of lowercase English alphabetic letters ascii[a-z].


def make_anagram(a, b):
    """
    :param a: first string
    :param b: second string
    :return: minimum number oif characters to be deleted to make the strings anagrams
    """
    a_dict, b_dict = {}, {}
    count = 0
    for i in range(len(a)):
        if a[i] in a_dict.keys():
            a_dict[a[i]] += 1
        else:
            a_dict[a[i]] = 1
    for i in range(len(b)):
        if b[i] in b_dict.keys():
            b_dict[b[i]] += 1
        else:
            b_dict[b[i]] = 1
    a_list = list(filter(lambda x: x not in b_dict.keys(), a_dict.keys()))
    b_list = list(filter(lambda x: x not in a_dict.keys(), b_dict.keys()))
    count += sum(a_dict[x] for x in a_list)
    count += sum(b_dict[x] for x in b_list)
    a_list = list(filter(lambda x: x[0] in b_dict.keys() and x[1] != b_dict[x[0]], a_dict.items()))
    count += sum(abs(x[1]-b_dict[x[0]]) for x in a_list)
    return count


if __name__ == '__main__':
    a = input()
    b = input()
    print(make_anagram(a, b))
