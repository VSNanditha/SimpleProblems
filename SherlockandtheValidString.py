# Sherlock considers a string to be valid if all characters of the string appear the same number of times.
# It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will
# occur the same number of times. Given a string s, determine if it is valid. If so, return YES, otherwise return NO.
#
# For example, if s = sbc, it is a valid string because frequencies are {a : 1, b : 1, c : 1}.
# So is s = abcc because we can remove one c and have 1 of each character in the remaining string.
# If s = abccc however, the string is not valid as we can only remove 1 occurrence of c. That would leave character
# frequencies of {a : 1, b : 1, c : 2}.
#
# Input Format
#
# A single string s.
#
# Constraints
#
# * 1 <= |s| <= 10^5
# * Each character s[i] E ascii[a - z]
#
# Output Format
#
# Print YES if string s is valid, otherwise, print NO.


def is_valid(s):
    """
    :param s: input string
    :return: YES/NO indicating if the string is valid
    """
    string_dict = {}
    for i in range(len(s)):
        if s[i] in string_dict.keys():
            string_dict[s[i]] += 1
        else:
            string_dict[s[i]] = 1
    if len(list(set(string_dict.values()))) == 1:
        return 'YES'
    current = string_dict[s[0]]
    flag = 0
    for value in string_dict.values():
        if value != current:
            if flag == 1:
                return 'NO'
            if value - 1 in (current, 0):
                flag = 1
                continue
            else:
                return 'NO'
    return 'YES'


if __name__ == '__main__':
    s = input()
    print(is_valid(s))
