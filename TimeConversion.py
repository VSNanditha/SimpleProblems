# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
#
# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
# Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
#
# Input Format
#
# A single string s containing a time in 12-hour clock format (i.e.: hh:mm:ssPM or hh:mm:ssAM), where 01 <= hh <= 12 and
# 00<= mm,ss <= 59.
#
# Constraints
#
# All input times are valid
# Output Format
#
# Convert and print the given time in 24-hour format, where 00 <= hh <= 12.


def timeConversion(s):
    """
    :param s: 12 - hour format time string
    :return: 24 - hour format time string
    """
    hh, mm, ss = map(int,s[:-2].split(':'))
    meridian = s[-2:]
    hh = (hh % 12) + 12 if meridian == 'PM' else hh % 12
    return '%02d:%02d:%02d' % (hh, mm, ss)


if __name__ == '__main__':
    s = input()
    print(timeConversion(s))
