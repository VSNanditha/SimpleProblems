def max_min(k, arr):
    """
    :param k: window size
    :param arr: list of numbers
    :return: minimum unfairness
    """
    arr.sort()
    min_unfairness = max(arr[:k]) - min(arr[:k])
    for i in range(1, len(arr)-k+1):
        min_unfairness = max(arr[i:i+k]) - min(arr[i:i+k]) if (max(arr[i:i+k]) - min(arr[i:i+k])) < min_unfairness \
            else min_unfairness
        print(max(arr[i:i+k]) - min(arr[i:i+k]), min_unfairness, arr[i:i+k])
        if min_unfairness == 0:
            break
    return min_unfairness


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)
    print(max_min(k, arr))
