# import math
# from fractions import Fraction


def min_time(machines, goal):
    """
    :param machines:
    :param goal:
    :return:
    """
    items, days = 0, 0
    while items < goal:
        days += 1
        items += sum(1 for machine in machines if days % machine == 0)
        print(items, days)
    return days

    # one_day_work = sum(Fraction(1/machine) for machine in machines)
    # days = round(goal/one_day_work, 1)
    # print(days, one_day_work, goal/one_day_work, min(machines) * goal)
    # return int(math.ceil(days))


if __name__ == '__main__':

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = min_time(machines, goal)

    print(str(ans) + '\n')
