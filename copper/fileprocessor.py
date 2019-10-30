# -*- coding: utf-8 -*-

"""
fileprocessor.py: Read Databases in Kosara's Format and spmf Format.

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

def readDB(u_db, options):
    """
    Read a database in a format

    Extended description of function.

    Parameters
    ----------
    u_db : string
        Logical expression to evaluate
    
    options : dict(String, Variant)
        options to formats ["ascii", "spmf"]

    Returns
    -------
    List(String)
        Database formated in a list
    """

    if options['format'] == 'ascii':
        return asciiFormater(u_db)
    elif options['format'] == 'spmf':
        return minOneFormater(u_db)
    else:
        print("This File Format do not exists")
        return

def unsafeJoin(x, base=''):
    string = base
    for i in x:
        string+=i
    return string

def asciiFormater(asciiFile):
    """
    Read a database in format of Kosara Format

    Extended description of function.

    Parameters
    ----------
    asciiFile : string
        Database in string in Kosara format

    Returns
    -------
    List(String)
        Database readed in a list
    """
    pDB = []
    for index, line in enumerate(asciiFile):
        pattern = []
        itemset = ''
        splitLine = line.replace(' \n','').split(' ')
        ignore = True
        first = True
        counter = 0
        for slot in splitLine:
            if not ignore:
                if not counter:
                    counter = int(slot)
                    if first:
                        first = False
                    else:
                        pattern.append(itemset[:-1]+'\0')
                        itemset = ''
                else:
                    counter -= 1
                    itemset+=slot+'|'
            else:
                ignore = False
        pDB.append((str(index)+ unsafeJoin(pattern,'\0'))[:-1] )
    return pDB

def asciiToMinOne(asciiFile):
    """
    Read a database in format of spmf

    Extended description of function.

    Parameters
    ----------
    asciiFile : string
        Database in string in spmf format

    Returns
    -------
    List(String)
        Database readed in a list
    """
    pDB = []
    for index, line in enumerate(asciiFile):
        pattern = []
        itemset = ''
        splitLine = line.replace(' \n','').split(' ')
        ignore = True
        first = True
        counter = 0
        for slot in splitLine:
            if not ignore:
                if not counter:
                    counter = int(slot)
                    if first:
                        first = False
                    else:
                        pattern.append(itemset[:-1]+' -1 ')
                        itemset = ''
                else:
                    counter -= 1
                    itemset+=slot+' '
            else:
                ignore = False
        pDB.append(((str(1)+ unsafeJoin(pattern,''))[:-1] + '-2')[1:])
    return pDB

def minOneFormater(moDB):
    """
    Convert database in spmf format to Kosara's format

    Extended description of function.

    Parameters
    ----------
    MoDB : string
        Database in string in format of spmf

    Returns
    -------
    String
        Database in string in format of Kosara
    """
    patternDB = []
    for line, entry in enumerate(moDB):
        splitted = entry.rstrip().replace("-1","\0").replace("-2","").split('\0')[:-1]
        patternDB.append(str(line)+unsafeJoin(map(lambda x: x.lstrip().rstrip().replace(' ','|')+"\0", splitted),'\0')[:-1])
    return patternDB