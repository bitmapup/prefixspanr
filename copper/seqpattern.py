"""
seqpattern.py: Sequential pattern class for use with the prefixspan algorithm.

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

import copy as copymodule
from itertools import chain

class Pattern(object):
    """
    Pattern Class
    """
    def __init__(self):
        """ Constructor """
        self.__tail__ = []
        self.__head__ = set() # Used to be Oset
        self.__last__ = -1
        return
    
    
    def copy(self):
        """ Copy entire pattern """
        clone = Pattern()
        clone.__tail__ = copymodule.deepcopy(self.__tail__)
        clone.__head__ = copymodule.deepcopy(self.__head__)
        clone.__last__ = self.__last__
        return clone        
        
    def assemble(self, item):
        """ assemble the pattern """
        assert item > self.__last__
        new = self.copy()
        new.__head__.add(item)
        new.__last__ = item
        return new

    def appended(self):
        """ Evaluate if item is appended in pattern """
        return len(self.__head__) == 1

    def append(self, item):
        """ Append item in pattern """
        new = self.copy()
        if new.__head__:
            new.__tail__.append(new.__head__)
        new.__head__ = set([item]) #Used to be Oset
        new.__last__ = item
        return new

    def last(self):
        """ Get last item """        
        assert self.__last__ != -1
        return self.__last__

    def contained(self, itemset):
        """ Evaluate if all items in other itemset is contained in this pattern """
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
            string+='<'
            buffr = ''
            for item in iset:
                buffr+=str(item)+', '
            if buffr:
                string+=buffr[:-2]+'>'
            else:
                string+='>'
        return string

    def __repr__(self):
        """ Printable representation """
        return str(self)
