# -*- coding: utf-8 -*-

"""
interval.py: Pointer to interval and interval operations friend functions .

__author__ = "Agustin Guevara Cogorno"
__copyright__ = "Copyright 2015, Copper Package"
__license__ = "GPL"
__maintainer__ = "Yoshitomi Eduardo Maehara Aliaga"
__credits__ = ["Agustin Guevara Cogorno", "Yoshitomi Eduardo Maehara Aliaga"]
__email__ = "ye.maeharaa@up.edu.pe"
__institution_ = "Universidad del Pacifico|University of the Pacific"
__version__ = "1.1"
__status__ = "Proof of Concept (POC)"
"""


class __IntervalPointer__(object):
    """ Interval Pointer Class"""
    def __init__(self, ref):
        self.ref = ref
        self.pos = 0
        self.lim = len(ref)

    def __getitem__(self, arg):
        return self.ref[self.pos][arg]

    def peek(self, arg):
        return self.ref[self.pos+1][arg]

    def next(self):
        self.pos += 1
        return

    def check(self):
        return bool(self) and self.pos + 1 < self.lim

    def __nonzero__(self):
        return self.pos < self.lim


def __intervalu__(intervallist):
    """
    Clopen interval union using linesweep.

    Extended description of function.

    Parameters
    ----------
    intervallist : list
        interval list to operate

    Returns
    -------
    Boolean
        Logical Expression Value

    """
    result = []
    for interval in intervallist:
        if not result:
            result.append([x for x in interval])
        else:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append([x for x in interval])
    return result


def __intervaln__(intervallist1, intervallist2):
    """
    Interval intersection between two list of disjoint clopen intervals
    using linesweep.

    Extended description of function.

    Parameters
    ----------
    intervallist : list
        interval list to operate

    Returns
    -------
    Boolean
        Logical Expression Value

    """
    result = []
    if not(intervallist1 and intervallist2):
        return result
    if (intervallist1[0][0] < intervallist2[0][0]) and (intervallist1[0][1] > intervallist2[-1][1]):
        return intervallist2
    if (intervallist2[0][0] < intervallist1[0][0]) and (intervallist2[0][1] > intervallist1[-1][1]):
        return intervallist1
    j = 0 if intervallist1[0][0] < intervallist2[0][0] else 1
    q = (j + 1) % 2
    i = (__IntervalPointer__(intervallist1), __IntervalPointer__(intervallist2))
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
        assert result[0][0] >= intervallist1[0][0]
        assert result[0][0] >= intervallist2[0][0]
    return result
