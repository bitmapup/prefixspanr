# -*- coding: utf-8 -*-

"""
Pointer to interval and interval operations friend functions.
"""


class IntervalPointer(object):
    """ Interval Pointer Class"""
    def __init__(self, ref):
        """
        Constructor of Interval Pointer class
        """
        self.ref = ref
        self.pos = 0
        self.lim = len(ref)

    def __getitem__(self, arg):
        """
        Obtain item in interval
        """
        return self.ref[self.pos][arg]

    def peek(self, arg):
        """
        Peek in interval
        """
        return self.ref[self.pos+1][arg]

    def next(self):
        """
        Next item in interval
        """
        self.pos += 1
        return

    def check(self):
        """
        Check if interval is not empty or is not reached limit
        """
        return bool(self) and self.pos + 1 < self.lim

    def __nonzero__(self):
        return self.pos < self.lim


def __intervalu__(interval_list):
    """
    Clopen interval union using linesweep.

    Extended description of function.

    Parameters
    ----------
    interval_list : list
        interval list to operate

    Returns
    -------
    Boolean
        Logical Expression Value

    """
    result = []
    for interval in interval_list:
        if not result:
            result.append([x for x in interval])
        else:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append([x for x in interval])

    return result


def __intervaln__(interval_list1, interval_list2):
    """
    Interval intersection between two list of disjoint clopen intervals
    using linesweep.

    Extended description of function.

    Parameters
    ----------
    interval_list1 : list
        interval list to operate

    interval_list1 : list
        interval list to operate

    Returns
    -------
    Boolean
        Logical Expression Value

    """
    result = []
    if not(interval_list1 and interval_list2):
        return result

    if (interval_list1[0][0] < interval_list2[0][0]) and (interval_list1[0][1] > interval_list2[-1][1]):
        return interval_list2

    if (interval_list2[0][0] < interval_list1[0][0]) and (interval_list2[0][1] > interval_list1[-1][1]):
        return interval_list1

    j = 0 if interval_list1[0][0] < interval_list2[0][0] else 1
    q = (j + 1) % 2
    i = (IntervalPointer(interval_list1), IntervalPointer(interval_list2))

    while i[0] and i[1]:
        while i[j].check() and i[j].peek(0) < i[q][0]:
            i[j].next()

        if i[q][0] >= i[j][1]:
            i[j].next()
            j, q = q, j
        else:
            result.append([max(i[j][0], i[q][0]), min(i[j][1], i[q][1])])
            if i[j][1] < i[q][1]:
                j, q = q, j
            i[q].next()

    if result:
        assert result[0][0] >= interval_list1[0][0]
        assert result[0][0] >= interval_list2[0][0]
    return result
