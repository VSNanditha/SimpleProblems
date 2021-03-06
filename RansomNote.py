# Problem
#
# Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced
# back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from
# it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive
# and he must use only whole words available in the magazine. He cannot use substrings or concatenation
# to create the words he needs.
#
# Given the words in the magazine and the words in the ransom note,
# print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
#
# For example, the note is "Attack at dawn". The magazine contains only "attack at dawn".
# The magazine has all the right words, but there's a case mismatch. The answer is No.
#
# Input Format
#
# The first line contains two space-separated integers, m and n, the numbers of words in the magazine and the note.
# The second line contains m space-separated strings, each magazine[i].
# The third line contains n space-separated strings, each note[i].
#
# Constraints
#
# * 1 <= m, n <=30000
# * 1 <= |magazine[i]|, |note[i]| <= 5
# * Each word consists of English alphabetic letters (i.e., a to z and A to Z).
#
# Output Format
#
# Print Yes if he can use the magazine to create an untraceable replica of his ransom note. Otherwise, print No.


def check_magazine(magazine, note):
    """
    :param magazine: list of all words
    :param note: list of the words
    :return:
    """
    dictionary = {}
    for word in magazine:
        dictionary[word] = dictionary[word] + 1 if word in dictionary.keys() else 1
    for word in note:
        if word in dictionary.keys() and dictionary[word] > 0:
            dictionary[word] -= 1
            continue
        else:
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    check_magazine(magazine, note)
