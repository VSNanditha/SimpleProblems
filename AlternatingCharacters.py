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
