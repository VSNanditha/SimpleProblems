# It's New Year's Day and everyone's in line for the Wonderland roller coaster ride!
# There are a number of people queued up, and each person wears a sticker indicating their initial position in the
# queue. Initial positions increment by 1 from 1 at the front of the line to  at the back.
#
# Any person in the queue can bribe the person directly in front of them to swap positions.
# If two people swap positions, they still wear the same sticker denoting their original places in line.
#
# One person can bribe at most two others. For example, if n = 8 and Person 5 bribes Person 4,
# the queue will look like this: 1, 2, 3, 5, 4, 6, 7, 8.
#
# Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place
# to get the queue into its current state!
#
# minimumBribes has the following parameter(s):
#
# q: an array of integers
#
# Input Format
#
# The first line contains an integer t, the number of test cases.
#
# Each of the next t pairs of lines are as follows:
# - The first line contains an integer t, the number of people in the queue
# - The second line has n space-separated integers describing the final state of the queue.
#
# Constraints
#
# * 1 <= t <= 10
# * 1 <= n <= 10^5
#
# Sub tasks
#
# For 60% score 1 <= n <= 10^3
# For 100% score 1 <= n <= 10^5
#
# Output Format
#
# Print an integer denoting the minimum number of bribes needed to get the queue into its final state.
# Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than 2 people.


def minimum_bribes(q):
    """
    :param q: array of order of persons
    :return:
    """
    bribes = 0
    for i in range(len(q)-1, -1, -1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2), i, 1):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimum_bribes(q)
