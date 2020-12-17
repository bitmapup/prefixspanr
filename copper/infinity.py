# -*- coding: utf-8 -*-

"""
Infinity class for not relying on os/sys dependant calls such as MAXINT.
"""


class Infinity(object):

    def __init__(self):
        """
        Constructor of Infinity class
        """
        return

    def __eq__(self, other):
        """
        overload equal operator
        """
        return False

    def __gt__(self, other):
        """
        overload greater operator
        """
        return True

    def __ge__(self, other):
        """
        overload of greater equal operator
        """
        return True

    def __le__(self, other):
        """
        overload of less equal operator
        """
        return False

    def __lt__(self, other):
        """
        overload of less operator
        """
        return False
