# -*- coding: utf-8 -*-

"""
Read and process databases in Kosarak's Format and SPMF Format.
"""

from dbpointer import DBPointer, CopperPointer, WindowGapPointer, WinCopPointer
from infinity import Infinity


def unsafe_join(x, base=''):
    """
    Join Unsafe Strings

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


def read_db_format(u_db, options):
    """
    Read a database in a format

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
    
    if 'format' not in options:
        options['format'] = 'spmf'

    if options['format'] == 'ascii':
        return ascii_formater(u_db)
    elif options['format'] == 'spmf':
        return spmf_formater(u_db)
    else:
        print("This File Format do not exists")
        return


def ascii_formater(ascii_file):
    """
    Read a database in format of Kosarak's Format

    Parameters
    ----------
    ascii_file : string
        Database in string in Kosarak's format

    Returns
    -------
    list
        Database converted in spmf format
    """
    p_db = []
    for index, line in enumerate(ascii_file):
        pattern = []
        itemset = ''
        split_line = line.replace(' \n', '').split(' ')
        ignore = True
        first = True
        counter = 0
        for slot in split_line:
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
        p_db.append((str(index) + unsafe_join(pattern, '\0'))[:-1])
    return p_db


def ascii_to_spmf(ascii_file):
    """
    Read a database in format of Kosarak's convert to SPMF format

    Parameters
    ----------
    ascii_file : string
        Database in string in Kosarak format

    Returns
    -------
    list
        Database converted in spmf
    """
    p_db = []
    for index, line in enumerate(ascii_file):
        pattern = []
        itemset = ''
        split_line = line.replace(' \n', '').split(' ')
        ignore = True
        first = True
        counter = 0
        for slot in split_line:
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
        p_db.append(((str(1) + unsafe_join(pattern, ''))[:-1] + '-2')[1:])
    return p_db


def spmf_formater(mo_db):
    """
    Convert database in spmf format to Kosarak's format

    Parameters
    ----------
    mo_db : string
        Database in string in format of spmf

    Returns
    -------
    String
        Database in string in format of Kosarak
    """
    patterndb = []
    for line, entry in enumerate(mo_db):
        splitted = entry.rstrip().replace("-1", "\0").replace("-2", "").split('\0')[:-1]
        patterndb.append(str(line) + unsafe_join(map(lambda x: x.lstrip().rstrip().replace(' ', '|') + "\0", splitted),
                                                 '\0')[:-1])
    return patterndb


def db_to_spmf(db):
    """
    Convert database in csv format to spmf format

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


def result_file_name(base, options):
    """
    obtain name of results file

    Parameters
    ----------
    base : string
    options : dict    

    Returns
    -------
    String
        name of result file name
    """
    outfile = base + "_"
    for opt in options:
        if opt == 'DBPointer':
            if options[opt] == DBPointer:
                # PrefixSpan
                outfile += 'ps' + '_'
            elif options[opt] == CopperPointer:
                # Copper
                outfile += 'copper' + '_'
            elif options[opt] == WinCopPointer:
                # Windowed-Cooper
                outfile += 'wincopper' + '_'
            elif options[opt] == WindowGapPointer:
                # Windowed Gapped Copper
                outfile += 'wingap' + '_'
        elif opt == 'algorithm':
            continue
        elif opt == 'Pattern':
            continue
        elif opt == 'itemsSeparated':
            continue
        elif opt == 'threshold':
            outfile += 'at' + '_' + str(options[opt]) + '_'			
        elif opt == 'thresholdRatio':
            outfile += 'rt' + '_' + str(int(options[opt] * 100)) + '_'
        elif opt == 'winVal':
            continue
        elif opt == 'databaseLen':
            continue
        elif opt == 'gapVal':
            continue
        elif opt == 'minSeqLen':
            continue
        elif opt == 'maxSeqLen':
            continue
        elif opt == 'avgSeqLen':
            continue
        elif opt == 'minISLen':
            continue
        elif opt == 'maxISLen':
            continue
        elif opt == 'avgISLen':
            continue
        elif opt == 'itemsSeparated':
            continue
        elif opt == 'resultFile':
            continue
        elif opt == 'quantDiffitems':
            continue
        elif opt == 'test':
            continue
        elif opt == 'minSize':
            outfile += 'miis_' + str(options[opt]) + '_'
        elif opt == 'maxSize':
            if isinstance(options[opt], Infinity):
                outfile += 'mais_Inf_'
            else:
                outfile += 'mais_' + str(options[opt]) + '_'
        elif opt == 'minSseq':
            outfile += 'miss_' + str(options[opt]) + '_'
        elif opt == 'maxSseq':
            if isinstance(options[opt], Infinity):
                outfile += 'mass_Inf_'
            else:
                outfile += 'mass_' + str(options[opt]) + '_'
        elif opt == 'logic':
            if options[opt] == (lambda x: True):
                outfile += 'l_default_'
        elif opt == 'window':
            outfile += 'win_' + str(options['winVal']) + '_'
        elif opt == 'gap':
            outfile += 'gap_' + str(options['gapVal']) + '_'
        elif opt == 'dataDesc':
            outfile += str(options[opt]) + '_'
        else:
            outfile += str(opt[0]) + "_" + str(options[opt]) + '_'

    outfile += '.txt'
    return outfile


def result_file(result_mining, options, time_start=-1, time_end=-1, mem_after=-1, mem_before=-1,
                mem_max_after=-1, mem_max_before=-1, base='Results'):
    """
    Obtain summary results file of mining

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
    outfile = result_file_name(base, options)
    with open(outfile, "w") as out:
        out.write("{")
        out.write("\'algorithm\': " + "\'" + str(options['algorithm']) + "\'" + ", ")
        out.write("\'format\': " + "\'" + str(options['format']) + "\'" + ", ")
        # ================== Dataset Description ==================
        out.write("\'DBsize\': " + str(options['databaseLen']) + ", ")
        out.write("\'DBmaxSeqLen\': " + str(options['maxSeqLen']) + ", ")
        out.write("\'DBminSeqLen\': " + str(options['minSeqLen']) + ", ")
        out.write("\'DBavgSeqLen\': " + str(options['avgSeqLen']) + ", ")
        out.write("\'DBmaxISLen\': " + str(options['maxISLen']) + ", ")
        out.write("\'DBminISLen\': " + str(options['minISLen']) + ", ")
        out.write("\'DBavgISLen\': " + str(options['avgISLen']) + ", ")
        out.write("\'quantDiffitems\': " + str(options['quantDiffitems']) + ", ")

        # ================== Analysis Description ==================
        out.write("\'absMinSupp\': " + str(options['threshold']) + ", ")
        out.write("\'relMinSupp\': " + str(options['thresholdRatio']) + ", ")
        out.write("\'pattFound\': " + str(len(result_mining)))
        if time_start != -1 and time_end != -1:
            out.write(", " + "\'Time\': " + str(time_end - time_start))

        if mem_after != -1 and mem_before != -1:
            out.write(", " + "\'memory\': " + str(mem_after - mem_before))
        
        if mem_max_after != -1 and mem_max_before != -1:
            out.write(", " + "\'maxMemory\': " + str(mem_max_after - mem_max_before))
        
        # ================== Constraints Description ==================

        if 'maxSseq' in options and 'minSseq' in options:
            out.write(", " + "\'minSeqcons\': " + str(options['minSseq']))
            if type(options['maxSseq']) != Infinity:
                out.write(", " + "\'maxSeq\': " + "Yes")
                out.write(", " + "\'maxSeq value\': " + str(options['maxSseq']))
            else:
                out.write(", " + "\'maxSeq\': " + "No")
                out.write(", " + "\'maxSeq value\': " + "Infinity")
        
        if 'maxSize' in options and 'minSize' in options:
            out.write(", " + "\'minIScons\': " + str(options['minSize']))
            if type(options['maxSize']) != Infinity:
                out.write(", " + "\'maxIS\': " + "Yes")
                out.write(", " + "\'maxIs value\': " + str(options['maxSize']))
            else:
                out.write(", " + "\'maxIS\': " + "No")
                out.write(", " + "\'maxIs value\': " + "Infinity")
        
        if 'window' in options:
            out.write(", " + "\'windows\': " + "Yes")
            out.write(", " + "\'windows value\': " + str(options['winVal']))

        if 'gap' in options:
            out.write(", " + "\'gap\': " + "Yes")
            out.write(", " + "\'gap value\' " + str(options['gapVal']))
        
        out.write("}\n")

        for pat in sorted(result_mining, key=lambda x: x[1]):
            out.write(str(pat) + '\n')
