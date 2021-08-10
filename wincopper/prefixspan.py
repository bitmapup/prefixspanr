# -*- coding: utf-8 -*-

"""
Implementation of Jiawei Han, Jian Pei, Behzad Mortazavi-Asl,
Helen Pinto, Qiming Chen, Umeshwar Dayal, MC Hsu, Prefixspan Algorithm
in Python.

With constraints added from Guevara-Cogorno, Flamand,
Alatrista-Salas in COPPER Paper and Window/Time Gap constraints added from Alatrista-Salas, Guevara-Cogorno,
Maehara, Nuñez del Prado in WinCOPPER Paper.
"""

from seqpattern import Pattern
from dbpointer import DBPointer, CopperPointer, WindowGapPointer, WinCopPointer
from infinity import Infinity
import logiceval
import dataprocessor as dp
import fileprocessor as fp
import profiling as pro
import math
import time


def validate_db(db, options):
    """
    validate if database contain only 1-itemsets or
    contain any k-itemset and is setted correctly

    Parameters
    ----------
    db : string
        Database to validate
    options: dict
        options used to configure

    Returns
    -------
    boolean
        Value of validation

    """    
    valid = True
    for sequence in db:
        for itemset in sequence:
            if type(itemset) == list and options['itemsSeparated']:
                valid = False
    
    return valid


def __parse_db__(db):
    """
    Takes a list of strings in the expected format
    and parses them into the db, a converter from zone to zone_id
    and a frequency dictionary each item on the database.

    Parameters
    ----------
    db : list
        Database in string format

    Returns
    -------
    list, int, list
        Database Parsed in format, zone2int, itembag

    """
    zone2int = {}
    parsed_db = []
    itembag = {}
    for line in db:
        sequence_bag = set()
        sequence = []
        i = line.split('\0')
        if i[0] not in zone2int:
            zone2int[i[0]] = len(zone2int)
        for itemset in i[1:]:
            iset = set()  # !
            for item in itemset.split('|'):
                if item:
                    sequence_bag.add(int(item))
                    iset.add(int(item))
            sequence.append(iset)
        parsed_db.append(sequence)
        for item in sequence_bag:
            if item in itembag:
                itembag[item] += 1
            else:
                itembag[item] = 1
    return parsed_db, zone2int, itembag


def __parse_options__(options):
    """
    Parses options and checks the minimum set of options is present.
    Selects the correct classes for each version of the algorithm.

    Parameters
    ----------
    options : dict
        options used to configure

    Returns
    -------
    options: dict
        options parsed

    """

    assert 'threshold' in options
    assert isinstance(options['threshold'], (int, float))

    options['Pattern'] = Pattern

    # ratio threshold
    if type(options['threshold']) == float:
        options['thresholdRatio'] = options['threshold']
        options['threshold'] = int(math.ceil(options['threshold'] * options['databaseLen']))
    elif type(options['threshold']) == int:
        options['thresholdRatio'] = round(float(options['threshold']) / float(options['databaseLen']), 2)

    if 'itemsSeparated' not in options:
        options['itemsSeparated'] = True

    if 'resultFile' not in options:
        options['resultFile'] = True

    # Standard prefixspan
    options['DBPointer'] = DBPointer
    options['algorithm'] = "PrefixSpan"
    
    # COPPER
    if any(param in options for param in ['minSseq', 'maxSseq', 'minSize', 'maxSize']):
        options['DBPointer'] = CopperPointer
        options['algorithm'] = "Copper"
        if 'logic' not in options:
            options['logic'] = lambda x: True
        else:
            # options['logic'] turns a function which evaluate a expression
            options['logic'] = logiceval.evaluator(options['logic'])
            # options['minSseq'] minimum size of a itemize
        if 'minSseq' not in options:
            options['minSseq'] = 0
            # options['maxSseq'] maximum size of a itemize
        if 'maxSseq' not in options:
            options['maxSseq'] = Infinity()
            # options['minSize'] minimum size of a pattern
        if 'minSize' not in options:
            options['minSize'] = 0
            # options['maxSize'] maximum size of a pattern
        if 'maxSize' not in options:
            options['maxSize'] = Infinity()
    # Window - Gap
    if any(param in options for param in ['window', 'gap']):
        options['DBPointer'] = WindowGapPointer
        options['algorithm'] = "WinGap"
        if 'gap' in options:
            options['gapVal'] = options['gap']
            gap = options['gap'] + 1
            options['gap'] = lambda x, y: map(lambda z: [z + 1, min(z + gap + 1, y)], x)
        else:
            options['gapVal'] = 'default'
            options['gap'] = lambda x, y: [[x[0] + 1, y]]
        if 'window' in options:
            options['winVal'] = options['window']
            window = options['window']
            options['window'] = lambda x, y: map(lambda z: [z + 1, min(z + window + 1, y)], x)
        else:
            options['winVal'] = 'default'
            options['window'] = lambda x, y: [[0, y]]
    # WinCopper
    if all(param in options for param in ['minSseq', 'minSize', 'window', 'gap']):
        options['DBPointer'] = WinCopPointer
        options['algorithm'] = "WinCopper"
    return options


def __ffi__(support, itembag):
    """
    Returns frequent items from the itembag given support and itembag

    Parameters
    ----------
    support : Integer
        options used to configure
    itembag : List
        bag of items

    Returns
    -------
    List
        Frequent items list which satisfy the threshold of support

    """
    return [i for i in itembag if itembag[i] >= support]


def __itembag_merge__(itembag_list):
    """
    Merges Multiple itembags while keeping count
    in how many a given item appears

    Parameters
    ----------
    itembag_list : List
        list of itembags to merge

    Returns
    -------
    Dict
        Merge itembags

    """
    mergedbag = {}
    for bag in itembag_list:
        for item in bag:
            if item in mergedbag:
                mergedbag[item] += 1
            else:
                mergedbag[item] = 1
    return mergedbag


def __prefixspan__(u_pointerdb, u_pattern, options, freqpatterns):
    """
    Prefixspan proper recursive call

    Parameters
    ----------
    u_pointerdb : List
        pointer
    u_pattern : List
        pattern
    options: Dict
        options used to configure
    freqpatterns: List
        frequent patterns list


    Returns
    -------


    """
    # Projection
    pointerdb = []
    for entry in (entry.project(u_pattern, options) for entry in u_pointerdb):
        if entry:
            pointerdb.append(entry)
    freqpatterns.append([u_pattern, len(pointerdb), float(len(pointerdb))/float(options['databaseLen'])])

    # Assemble - Get assemble candidates
    candidates = __itembag_merge__(map(lambda e: e.assemble_candidates(options), pointerdb))
    assemblings = filter(lambda i: candidates[i] >= options['threshold'], candidates)
    for assembling in assemblings:
        pattern = u_pattern.copy().assemble(assembling)
        __prefixspan__(pointerdb, pattern, options, freqpatterns)

    # Append - Get append candidates
    candidates = __itembag_merge__(map(lambda e: e.append_candidates(options), pointerdb))
    appendings = filter(lambda i: candidates[i] >= options['threshold'], candidates)
    for appending in appendings:
        pattern = u_pattern.copy().append(appending)
        __prefixspan__(pointerdb, pattern, options, freqpatterns)

    return


def prefixspan(sequences, raw_options):
    """
    Prefixspan entry call, takes a database in the null separator
    format and a dictionary of options and returns frequent patterns
    and their frequency.

    Parameters
    ----------
    sequences: List
        database
    raw_options : List
        options used to configure

    Returns
    -------
    List
        frequent patterns list

    """

    raw_options['minSeqLen'] = dp.min_seq_len(sequences)
    raw_options['maxSeqLen'] = dp.max_seq_len(sequences)
    raw_options['avgSeqLen'] = dp.avg_seq_len(sequences)
    raw_options['minISLen'] = dp.min_itemsets_len(sequences)
    raw_options['maxISLen'] = dp.max_itemsets_len(sequences)
    raw_options['avgISLen'] = dp.avg_itemsets_len(sequences)
    raw_options['quantDiffitems'] = len(dp.get_unique_items(sequences, raw_options['itemsSeparated']))
    raw_options['databaseLen'] = len(sequences)

    assert validate_db(sequences, raw_options), \
        "Probably sequences have n-itemsets separated by commas, please options['itemsSeparated'] in False"

    options = __parse_options__(raw_options)

    seq = dp.encode_sequences(sequences, options['itemsSeparated'])
    u_db = fp.db_to_spmf(seq)
    s_db = fp.read_db_format(u_db, options)
    p_db, z2i, ibag = __parse_db__(s_db)

    mem_before = pro.process_memory()
    mem_max_before = pro.max_resident_memory()
    time_start = time.time()

    candidates = __ffi__(options['threshold'], ibag)
    db = map(lambda seq: map(lambda iset: filter(lambda x: x in candidates, iset), seq), p_db)
    pointer_db = [options['DBPointer'](z_id, db) for z_id in range(len(db))]
    candidates = list(map(lambda x: options['Pattern']().assemble(x), candidates))
    freq_patterns = []
    for atomic_seq in candidates:
        __prefixspan__(pointer_db, atomic_seq, options, freq_patterns)
    if 'logic' in options:
        freq_patterns = list(filter(lambda x: options['logic'](x[0])
                                    and options['minSize'] <= len(x[0])
                                    and options['minSseq'] <= x[0].size(), freq_patterns))
    
    time_end = time.time()
    mem_max_after = pro.max_resident_memory()
    mem_after = pro.process_memory()

    freq_patterns_c = dp.decode_sequences(sequences, freq_patterns, options['itemsSeparated'])
    
    if options['resultFile']:
        fp.result_file(freq_patterns_c, options, time_start, time_end, 
                       mem_after, mem_before, mem_max_after, mem_max_before)
    
    return freq_patterns_c
