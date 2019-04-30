def compute(s):
    """
    :param s: input string
    :return:
    """
    dict = {}
    for i in range(len(s)):
        if s[i] not in dict.keys():
            dict[s[i]] = [i]
        else:
            dict[s[i]].append(i)
    if len(dict.keys()) == 1:
        return s
    sorted_chars = list(dict.keys())
    sorted_chars.sort()
    x = sorted_chars[len(sorted_chars)-1]
    index = dict[x].pop()
    positions = dict[x]
    if len(positions):
        i = len(positions) - 1
        while positions[i] + 1 == index:
            index = positions[i]
            i -= 1
    return s[index:]


if __name__ == '__main__':
    s = input()
    print(compute(s))
