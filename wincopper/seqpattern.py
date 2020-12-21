# -*- coding: utf-8 -*-

"""
Sequential pattern class for use with the prefixspan algorithm.
"""

import copy as copymodule
from itertools import chain


class Pattern(object):
    """
    Pattern Class
    """
    def __init__(self):
        """
        Constructor of Pattern class

        Parameters
        ----------


        Returns
        -------

        """
        self.__tail__ = []
        self.__head__ = set()  # Used to be Oset
        self.__last__ = -1
        return

    def copy(self):
        """
        Copy entire pattern

        Parameters
        ----------


        Returns
        -------
        Pattern
           Pattern copied
        """
        clone = Pattern()
        clone.__tail__ = copymodule.deepcopy(self.__tail__)
        clone.__head__ = copymodule.deepcopy(self.__head__)
        clone.__last__ = self.__last__
        return clone

    def assemble(self, item):
        """
        assemble the pattern

        Parameters
        ----------
        item: int
          item to assemble to pattern

        Returns
        -------

        """
        assert item > self.__last__
        new = self.copy()
        new.__head__.add(item)
        new.__last__ = item

        return new

    def appended(self):
        """
        Evaluate if item is appended in pattern

        Parameters
        ----------


        Returns
        -------
        Boolean

        """
        return len(self.__head__) == 1

    def append(self, item):
        """
        Append item in pattern

        Parameters
        ----------
        item: int
          item to append to pattern

        Returns
        -------
        Pattern
          Pattern with item appended
        """
        new = self.copy()
        if new.__head__:
            new.__tail__.append(new.__head__)
        new.__head__ = {item}  # Used to be Oset
        new.__last__ = item
        return new

    def last(self):
        """
        Get last item

        Parameters
        ----------

        Returns
        -------
        Int
          Last item the pattern

        """
        assert self.__last__ != -1
        return self.__last__

    def contained(self, itemset):
        """
        Evaluate if all items in other itemset is contained in this pattern

        Extended description of function.

        Parameters
        ----------
        itemset: string
          item to append to pattern

        Returns
        -------

        """
        return all((item in itemset for item in self.__head__))

    def project(self):
        """ Project pattern """
        return set(chain.from_iterable(self.__tail__+[self.__head__]))

    def __len__(self):
        """ Length of pattern """
        return len(self.__tail__) + bool(self.__head__)

    def size(self):
        """ Size of item pattern in top """
        return len(self.__head__)

    def __str__(self):
        """ Pattern representation in String """
        string = ''
        for iset in self.__tail__+[self.__head__]:
            string += '<'
            buffr = ''
            for item in iset:
                buffr += str(item) + ', '
            if buffr:
                string += buffr[:-2] + '>'
            else:
                string += '>'
        return string

    def __repr__(self):
        """ Printable representation """
        return str(self)