# There is a row of seats. Assume that it contains N seats adjacent to each other.
# There is a group of people who are already seated in that row randomly.
# i.e. some are sitting together & some are scattered.
#
# An occupied seat is marked with a character 'x' and an unoccupied seat is marked with a dot ('.')
#
# Now your target is to make the whole group sit together i.e. next to each other,
# without having any vacant seat between them in such a way that the total number of hops or jumps
# to move them should be minimum.
import statistics


def seats_rearrange(n, seat_arrangement):
    """
    :param n: number of seats
    :param seat_arrangement: seat arrangement of the audience
                            '.' --> empty position
                            'x' --> occupied position
    :return: number of hops
    """
    x_midpos, hops = -1, 0
    arrangement = [*enumerate(seat_arrangement)]
    x_pos = list(filter(lambda x: x[1] == 'x', arrangement))
    median = round(statistics.median([item[0] for item in x_pos]))
    i, j = median, median+1
    while i in range(median, -1, -1) and j in range(median+1, n):
        if seat_arrangement[i] == 'x':
            x_midpos = i
            break
        else:
            i -= 1
        if seat_arrangement[j] == 'x':
            x_midpos = j
            break
        else:
            j += 1
    i, j, mid_left, mid_right = 0, 0, x_midpos-1, x_midpos
    seat_arrangement = ['.'] * n
    x_pos_left = list(filter(lambda x : x[0] < x_midpos, x_pos))
    x_pos_left.sort(reverse=True)
    x_pos_right = list(filter(lambda x : x[0] >= x_midpos, x_pos))
    for position in x_pos_left:
        hops += abs(position[0] - mid_left) if seat_arrangement[mid_left] != position[0] else 0
        seat_arrangement[mid_left] = 'x'
        mid_left -= 1
    for position in x_pos_right:
        hops += abs(position[0] - mid_right) if seat_arrangement[mid_right] != position[0] else 0
        seat_arrangement[mid_right] = 'x'
        mid_right += 1
    return hops


if __name__ == '__main__':
    n = int(input("Enter the number of seats"))
    seat_arrangement = list(map(str, input("Enter the seat arrangement with space separation").rstrip().split()))
    if len(seat_arrangement) != n:
        print('Please input the arrangement for specified n value')
    else:
        print('Number of hops needed: ', seats_rearrange(n, seat_arrangement))
