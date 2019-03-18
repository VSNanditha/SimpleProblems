# Problem
#
# Emma is playing a new mobile game that starts with consecutively numbered clouds.
# Some of the clouds are thunderheads and others are cumulus.
# She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2.
# She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump
# from her starting position to the last cloud. It is always possible to win the game.
#
# For each game, Emma will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.
# For example, c = [0, 1, 0, 0, 0, 1, 0] indexed from 0...6.
# The number on each cloud is its index in the list so she must avoid the clouds at indexes 1 and 5.
# She could follow the following two paths: 0 -> 2 -> 4 -> 6 or 0 -> 2 -> 3 -> 4 -> 6.
# The first path takes 3 jumps while the second takes 4.
#
# jumpingOnClouds has the following parameter(s):
#
# c: an array of binary integers
#
# Input Format
#
# The first line contains an integer n, the total number of clouds.
# The second line contains n space-separated binary integers describing clouds c[i] where 0 <= i < n.
#
# Constraints
#
# * 2 <= n <= 100
# * c[i] belongs to {0, 1}
# * c[0] = c[n-1] = 0
#
# Output Format
#
# Print the minimum number of jumps needed to win the game.


def jumping_on_clouds(c):
    """

    :param c: array of binary integers specifying the cloud types
    :return: number of minimum jumps
    """
    jumps, position = 0, 0
    while position+1 < len(c):
        if position + 2 < len(c):
            position = position + 2 if c[position+2] != 1 else position + 1
        else:
            position += 1
        jumps += 1
        print(jumps, position)
    return jumps


if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumping_on_clouds(c)
    print(result)
