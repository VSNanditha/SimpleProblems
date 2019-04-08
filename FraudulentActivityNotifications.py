# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity.
# If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending
# for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't
# send the client any notifications until they have at least that trailing number of prior days' transaction data.
#
# Given the number of trailing days d and a client's total daily expenditures for a period of n days,
# find and print the number of times the client will receive a notification over all n days.
#
# For example, d = 3 and expenditures = [10, 20, 30, 40, 50]. On the first three days, they just collect spending data.
# At day 4, we have trailing expenditures of [10, 20, 30]. The median is 20 and the day's expenditure is 40.
# Because 40 >= 2 x 20, there will be a notice. The next day, our trailing expenditures are [20, 30, 40]
# and the expenditures are 50. This is less than 2 x 30 so no notice will be sent.
# Over the period, there was one notice sent.
#
# Note: The median of a list of numbers can be found by arranging all the numbers from smallest to greatest.
# If there is an odd number of numbers, the middle one is picked. If there is an even number of numbers,
# median is then defined to be the average of the two middle values.
#
# Input Format
#
# The first line contains two space-separated integers n and d, the number of days of transaction data,
# and the number of trailing days' data used to calculate median spending.
# The second line contains n space-separated non-negative integers where each integer i denotes expenditure[i].
#
# Constraints
#
# * 1 <= n <= 2 x 10^5
# * 1 <= d <= n
# * 0 <= expenditure[i] <= 200

import statistics


def activity_notifications(expenditure, d):
    """
    :param expenditure: list of expenditures each day
    :param d: number of trailing days to be considered for the check
    :return: number of days notifications are tobe send
    """
    notifications_count = 0
    for i in range(d, len(expenditure)):
        # print(expenditure[i - d:i])
        median = statistics.median(expenditure[i-d:i])
        # print(expenditure[i - d:i], median)
        notifications_count += 1 if expenditure[i] >= 2 * median else 0
    return notifications_count


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, input().rstrip().split()))
    print(activity_notifications(expenditure, d))
