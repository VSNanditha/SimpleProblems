
def luck_balance(k, contests):
    """
    :param k:
    :param contests:
    :return:
    """
    max_luck = 0
    contests = sorted(contests, key=lambda contest: contest[0], reverse=True)
    print(contests)
    for contest in contests:
        if contest[1] == 0:
            max_luck += contest[0]
        elif contest[1] == 1 and k > 0:
            max_luck += contest[0]
            k -= 1
        else:
            max_luck -= contest[0]
    return max_luck


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    print(luck_balance(k, contests))
