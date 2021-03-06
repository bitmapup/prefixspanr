# -*- coding: utf-8 -*-

"""
 Pointer to Database class for use with Prefixspan.
 Different classes correspond to different functionality and capabilities.
 * DBPointer - Prefixspan
 * CopperPointer - COPPER
 * WindowGap - PrefixSpan with Time Constraints (Window/Gap)
 * WinCop - COPPER with Time Constraints with Time Constraints
"""

import itertools
import interval


class DBPointer(object):
    """
    PrefixSpan Database Pointer Class
    """

    def __init__(self, zid, db):
        """
        Constructor of PrefixSpan Database Pointer class.

        Extended description of function.

        Parameters
        ----------
        db : list(list())
            database of sequences
        zid : list()
            Identificator of zone

        Returns
        -------
        None
        """
        self.__origin__ = db
        self.__entry__ = zid
        self.__positions__ = [-1]
        self.__last__ = -1

    def partial_copy(self):
        """
        Copy pointer sharing values.

        Parameters
        ----------

        Returns
        -------
        Pointer
            Pointer Copied
        """
        new = self.__class__(self.__entry__, self.__origin__)
        return new

    def project(self, pattern, options):
        """
        Project sequence pattern.

        Parameters
        ----------
        pattern :
            Pattern of sequence
        options :
            Options used to obtain projections


        Returns
        -------
        Pointer
            Pointer Copied
        """
        result = self.partial_copy()
        result.__last__ = pattern.last()
        if pattern.appended():
            result.__positions__ = [index + self.__positions__[0] + 1
                                    for index, itemset in
                                    enumerate(self.__origin__[self.__entry__][self.__positions__[0] + 1:])
                                    if pattern.last() in itemset]
        else:
            result.__positions__ = list(
                filter(lambda pos: pattern.last() in self.__origin__[result.__entry__][pos], self.__positions__))
        return result

    def append_candidates(self, options):
        """
        Add candidate to candidate set.

        Extended description of function.

        Parameters
        ----------
        options :
            Options used to obtain candidates

        Returns
        -------
        List(string)
            Candidates
        """
        candidates = set()
        for itemset in self.__origin__[self.__entry__][self.__positions__[0] + 1:]:
            for item in itemset:
                candidates.add(item)
        return candidates

    def assemble_candidates(self, options):
        """
        Assemble the candidates set

        Extended description of function.

        Parameters
        ----------
        options :
            Options used to obtain candidates

        Returns
        -------
        List(string)
            Candidates
        """
        candidates = set()
        for pos in self.__positions__:
            for val in filter(lambda x: x > self.__last__, self.__origin__[self.__entry__][pos]):
                candidates.add(val)
        return candidates

    def __nonzero__(self):
        """
        add candidates.

        Extended description of function.

        Parameters
        ----------

        Returns
        -------
        Boolean
            Logic value of nonzero
        """
        return bool(self.__positions__)

    def __str__(self):
        return "PrefixSpan"


class WindowGapPointer(DBPointer):
    """
    WindowGap Database Pointer Class
    """

    def __init__(self, zid, db):
        """
        Constructor of WindowGap Database Pointer class.

        Extended description of function.

        Parameters
        ----------
        db :
            database of sequences
        zid :
            Identificator of zone

        Returns
        -------
        None
        """
        super(WindowGapPointer, self).__init__(zid, db)
        self.__progenitor__ = []

    def partial_copy(self):
        """
        Share Pointer
        """
        new = super(WindowGapPointer, self).partial_copy()
        new.__progenitor__ = self.__progenitor__
        return new

    def project(self, pattern, options):
        if self.__last__ == -1:
            result = super(WindowGapPointer, self).project(pattern, options)
            return result
        result = self.partial_copy()
        result.__last__ = pattern.last()
        if pattern.appended():
            if not self.__progenitor__:
                result.__progenitor__ = self.__positions__
            ranges = interval.__intervaln__(
                interval.__intervalu__(options['window'](result.__progenitor__, len(self.__origin__[self.__entry__]))),
                interval.__intervalu__(options['gap'](self.__positions__, len(self.__origin__[self.__entry__]))))
            range_iter = itertools.chain.from_iterable((range(interval_e[0], interval_e[1]) for interval_e in ranges))
            result.__positions__ = [index
                                    for index, itemset in
                                    ((pos, self.__origin__[self.__entry__][pos]) for pos in range_iter)
                                    if pattern.last() in itemset]
        else:
            result.__positions__ = list(
                filter(lambda pos: pattern.last() in self.__origin__[result.__entry__][pos], self.__positions__))
        return result

    def append_candidates(self, options):
        candidates = set()
        progenitor = self.__progenitor__
        if not progenitor:
            progenitor = self.__positions__
        ranges = interval.__intervaln__(
            interval.__intervalu__(options['window'](progenitor, len(self.__origin__[self.__entry__]))),
            interval.__intervalu__(options['gap'](self.__positions__, len(self.__origin__[self.__entry__]))))
        rangeiter = itertools.chain.from_iterable(
            (range(interval_e[0], min(interval_e[1], len(self.__origin__[self.__entry__])))
             for interval_e in ranges))
        for pos in rangeiter:
            for item in self.__origin__[self.__entry__][pos]:
                candidates.add(item)
        return candidates


class CopperPointer(DBPointer):
    """
    Copper Database Pointer Class
    """

    def __init__(self, zid, db):
        super(CopperPointer, self).__init__(zid, db)
        self.__pattern__ = None

    def project(self, pattern, options):
        result = super(CopperPointer, self).project(pattern, options)
        result.__pattern__ = pattern
        return result

    def append_candidates(self, options):
        candidates = []
        if self.__pattern__.size() >= options['minSseq'] and len(self.__pattern__) < options['maxSize']:
            candidates = super(CopperPointer, self).append_candidates(options)
        return candidates

    def assemble_candidates(self, options):
        candidates = []
        if self.__pattern__.size() < options['maxSseq']:
            candidates = super(CopperPointer, self).assemble_candidates(options)
        return candidates


class WinCopPointer(CopperPointer, WindowGapPointer):
    """
    WinCop Database Pointer Class
    """

    def __init__(self, zid, db):
        super(WinCopPointer, self).__init__(zid, db)

    """
    Share Pointer
    """

    def partial_copy(self):
        new = WinCopPointer(self.__entry__, self.__origin__)
        new.__progenitor__ = self.__progenitor__
        return new

    def project(self, pattern, options):
        result = WindowGapPointer.project(self, pattern, options)
        result.__pattern__ = pattern
        return result

    def append_candidates(self, options):
        candidates = []
        if self.__pattern__.size() >= options['minSseq'] and len(self.__pattern__) < options['maxSize']:
            candidates = WindowGapPointer.append_candidates(self, options)
        return candidates

    def assemble_candidates(self, options):
        candidates = []
        if self.__pattern__.size() < options['maxSseq']:
            candidates = WindowGapPointer.assemble_candidates(self, options)
        return candidates
