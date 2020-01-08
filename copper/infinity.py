# -*- coding: utf-8 -*-

"""
infinity.py: Infinity class for not relying on os/sys
depandant calls such as MAXINT.

__author__ = "Agustin Guevara Cogorno"
__copyright__ = "Copyright 2015, Copper Package"
__license__ = "GPL"
__maintainer__ = "Yoshitomi Eduardo Maehara Aliaga"
__credits__ = ["Agustin Guevara Cogorno", "Yoshitomi Eduardo Maehara Aliaga"]
__email__ = "ye.maeharaa@up.edu.pe"
__institution_ = "Universidad del Pacifico"
__version__ = "1.1"
__status__ = "Proof of Concept (POC)"

"""


class Infinity(object):

    def __init__(self):
        return

    def __eq__(self, other):
        return False

    def __gt__(self, other):
        return True

    def __ge__(self, other):
        return True

    def __le__(self, other):
        return False

    def __lt__(self, other):
        return False
