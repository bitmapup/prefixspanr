# -*- coding: utf-8 -*-

"""
fileprocessor.py: Read Databases in Kosara's Format and spmf Format.

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

from dbpointer import DBPointer, CopperPointer, WindowGapPointer, WinCopPointer
import math


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
    # ratio threshold -- separate
    if type(options['threshold']) == float:
        options['threshold'] = int(math.ceil(options['threshold'] * len(u_db)))

    if 'format' not in options:
        options['format'] = 'spmf'

    if options['format'] == 'ascii':
        return asciiFormater(u_db)
    elif options['format'] == 'spmf':
        return minOneFormater(u_db)
    else:
        print("This File Format do not exists")
        return


def unsafeJoin(x, base=''):
    """
    Join Unsafe Strings

    Extended description of function.

    Parameters
    ----------
    x : string
    base : string

    Returns
    -------
    string
       String join with the base
    """
    string = base
    for i in x:
        string += i
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
        splitLine = line.replace(' \n', '').split(' ')
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
                    itemset += slot + '|'
            else:
                ignore = False
        pDB.append((str(index) + unsafeJoin(pattern, '\0'))[:-1])
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
        splitLine = line.replace(' \n', '').split(' ')
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
                    itemset += slot + ' '
            else:
                ignore = False
        pDB.append(((str(1) + unsafeJoin(pattern, ''))[:-1] + '-2')[1:])
    return pDB


def minOneFormater(moDB):
    """
    Convert database in spmf format to Kosara's format

    Extended description of function.

    Parameters
    ----------
    moDB : string
        Database in string in format of spmf

    Returns
    -------
    String
        Database in string in format of Kosara
    """
    patterndb = []
    for line, entry in enumerate(moDB):
        splitted = entry.rstrip().replace("-1", "\0").replace("-2", "").split('\0')[:-1]
        patterndb.append(str(line)+unsafeJoin(map(lambda x: x.lstrip().rstrip().replace(' ', '|')+"\0", splitted), '\0')[:-1])
    return patterndb


def db_to_spmf(db):
    """
    Convert database in csv format to spmf format

    Extended description of function.

    Parameters
    ----------
    db : string
        Database in string in format csv

    Returns
    -------
    String
        Database in string in format spmf
    """
    spmf_db = []
    for sequence in db:
        str_sequence = ""
        for itemset in sequence:
            if type(itemset) == list:
                for item in itemset:
                    str_sequence += str(item)
                    str_sequence += " "
                str_sequence += "-1 "
            else:
                str_sequence += str(itemset)
                str_sequence += " -1 "
        str_sequence += "-2 \n"
        spmf_db.append(str_sequence)
    return spmf_db


def get_result_file_name(base, options):
    """
    obtain name of results file

    Extended description of function.

    Parameters
    ----------
    base : string
    options : dict    

    Returns
    -------
    String
        Database in string in format of Kosara
    """
    outfile = base + "_"
    for opt in options:
        if opt == 'DBPointer':
            if options[opt] == DBPointer:
                outfile += 'PrefixSpan'
            elif options[opt] == CopperPointer:
                outfile += 'Copper'
            elif options[opt] == WinCopPointer:
                outfile += 'Windowed-Cooper'
            elif options[opt] == WindowGapPointer:
                outfile += 'Window-Gap'
        elif opt == 'Pattern':
            continue
        else:
            outfile += str(opt[0]) + str(options[opt])
        outfile += "_"

    outfile += '.txt'
    return outfile


def get_result_file(result_mining, options, time_start=-1, time_end=-1, mem_after=-1, mem_before=-1, mem_max_after=-1, mem_max_before=-1, base='Results'):
    """
    Obtain summary results file of mining

    Extended description of function.

    Parameters
    ----------
    result_mining : list
        Database in string in format of spmf
    options : dict

    time_start: float
        time of start process
    time_end: float
        time of end process
    mem_before: float

    mem_after: float

    mem_max_before: float

    mem_max_after: float

    base: string

    Returns
    -------
    File
		
    """
    outfile = get_result_file_name(base, options)
    with open(outfile, "w") as out:
        out.write("Options: " + str(options) + '\n')
        out.write("Patterns Found: " + str(len(result_mining)) + ' patterns' + '\n')
        if time_start != -1 and time_end != -1:
            out.write("Time Taken: " + str(time_end - time_start) + ' seconds' + '\n')

        if mem_after != -1 and mem_before != -1:
            out.write("Memory used: " + str(mem_after - mem_before) + ' Bytes' + '\n')
        
        if mem_max_after != -1 and mem_max_before != -1:
            out.write("Max Memory used: " + str(mem_max_after - mem_max_before) + ' Bytes' + '\n')

        for pat in sorted(result_mining, key=lambda x: x[1]):
                out.write(str(pat) + '\n')
