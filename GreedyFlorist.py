def get_minimum_cost(k, c):
    """
    :param k: number of friends
    :param c: cost array of flowers
    :return: minimum cost for k friends to buy n flowers
    """
    c.sort()
    min_cost = 0
    for i in range(n-k, len(c)):
        min_cost += c[i]
    if n-k >= k:
        iteration = 1
        temp = c[:n-k]
        temp.sort(reverse=True)
        k_temp = k
        for i in range(n-k):
            min_cost += (iteration + 1) * temp[i]
            k_temp -= 1
            if k_temp == 0:
                iteration += 1
                k_temp = k
    else:
        for i in range(n-k):
            min_cost += 2 * c[i]
    return min_cost


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    print(get_minimum_cost(k, c))
