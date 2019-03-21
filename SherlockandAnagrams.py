# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
# Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
#
# For example , the list of all anagrammatic pairs is  at positions  respectively.
#
# Input Format
#
# The first line contains an integer q, the number of queries.  
# Each of the next q lines contains a string s to analyze.
#
# Constraints
#
# * 1 <= q <= 10
# * 2 <= |s| <= 100
# * String s contains only lowercase letters belonging to ascii[a-z].
#
# Output Format
# For each query, return the number of unordered anagrammatic pairs.


def sherlock_and_anagrams(s):
    """
    :param s: input string
    :return: number of anagrams
    """
    anagrams = 0
    substrings = {}
    for i in range(len(s)):
        j = i
        while j < len(s):
            sorted_word = ''.join(sorted(s[i:j+1]))
            if sorted_word in substrings.keys():
                substrings[sorted_word].append(s[i:j+1])
            else:
                substrings[sorted_word] = [s[i:j+1]]
            j += 1
    for key, value in substrings.items():
        length = len(value)
        anagrams += ((length-1)*length)/2 if len(value) >= 2 else 0
    return int(anagrams)


if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = sherlock_and_anagrams(s)
        print(result)
