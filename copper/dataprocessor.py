# -*- coding: utf-8 -*-

"""
dataprocessor.py: module for preprocess and postprocess data.

__author__ = "Yoshitomi Eduardo Maehara Aliaga"
__copyright__ = "Copyright 2019, Copper Package"
__license__ = "GPL"
__maintainer__ = "Yoshitomi Eduardo Maehara Aliaga"
__credits__ = ["Agustin Guevara Cogorno", "Yoshitomi Eduardo Maehara Aliaga"]
__email__ = "ye.maeharaa@up.edu.pe"
__institution_ = "Universidad del Pacifico|University of the Pacific"
__version__ = "1.0"
__status__ = "Proof of Concept (POC)"

"""


def get_unique_items(database, item_separated=False):
    """
    Obtain a unique itemsets or items of sequence

    Extended description of function.

    Parameters
    ----------
    database : List
        database of sequences
    item_separated : Boolean
        True: items in itemsets are separated by colon
        False or blank: itemsets are separated by colon

    Returns
    -------
    List
        unique items list

    """
    sequence_set = []

    if not item_separated:
        #for sequence in database:
        #    for item in sequence:
        #        sequence_set += item
        for sequence in database:
            for itemset in sequence:
                if type(itemset) == list:
                    for item in itemset:
                        sequence_set.append(item)
                else:
                    sequence_set.append(itemset)
    else:
        for item in database:
            sequence_set += item

    sequence_set = list(set(sequence_set))
    sequence_set.sort()

    return sequence_set


def discretize_sequences(raw_db, item_separated=False):
    """
    Discretize a sequence in numbers

    Extended description of function.

    Parameters
    ----------
    raw_db : List
        database of sequences without preprocessing
    item_separated : Boolean
        True: items in itemsets which are in sequence are separated by colon
        False or blank: itemsets which are in sequence are separated by colon

    Returns
    -------
    List
        database discretized


    """
    sequence_set = get_unique_items(raw_db, item_separated)
    discrete_sequence = {sequence_set[i]: str(i + 1) for i in range(0, len(sequence_set))}

    db = []
    if not item_separated:
        # for sequence in raw_db:
        #     row = []
        #     for itemset in sequence:
        #         itemset_part = ''
        #         for item in itemset:
        #             itemset_part = itemset_part + ' ' + discrete_sequence[item]
        #         row.append(itemset_part.strip())
        #     db.append(row)
        for sequence in raw_db:
            row = []
            for itemset in sequence:
                if type(itemset) == list:
                    cell = []
                    for item in itemset:
                        cell.append(discrete_sequence[item])
                    row.append(cell)
                else:
                    row.append(discrete_sequence[itemset])
            db.append(row)
    else:
        for sequence in raw_db:
            row = []
            for itemset in sequence:
                row.append(discrete_sequence[itemset])
            db.append(row)
    return db


def result_patterns_to_str(result_patterns):
    """
    cast patterns to string

    Extended description of function.

    Parameters
    ----------
    result_patterns : List
        results patterns of sequential pattern mining


    Returns
    -------
    string
        database discretized

    """
    str_result_patterns = result_patterns
    for i in range(len(result_patterns)):
        str_result_patterns[i][0] = str(result_patterns[i][0])
    return str_result_patterns


def pattern_to_list(result_patterns):
    """
    convert pattern format to list

    Extended description of function.

    Parameters
    ----------
    result_patterns : List
        results patterns of sequential pattern mining


    Returns
    -------
    list
        patterns mined in a list
    """
    str_result_patterns = result_patterns_to_str(result_patterns)
    result_pattern_list = []
    itemset = ''
    for row_pattern in str_result_patterns:
        pattern = []
        for ch in row_pattern[0]:
            if ch != '<'and ch != '>' and ch != ' ' and ch != ',':
                itemset += ch
                itemset += ' '

            if ch == '>':
                pattern.append(itemset.split( ))
                itemset = ''
        result_pattern_list.append([pattern, row_pattern[1]])
    return result_pattern_list


def undiscretize_sequences(raw_db, result_pattern_list, item_separated=False):
    """
    cast patterns to string

    Extended description of function.

    Parameters
    ----------
    result_patterns : List
        results patterns of sequential pattern mining


    Returns
    -------
    string
        database discretized

    """
    
    sequence_set = get_unique_items(raw_db, item_separated)
    undiscrete_sequence = {str(i + 1): sequence_set[i] for i in range(0, len(sequence_set))}
    
    result_pattern = pattern_to_list(result_pattern_list)
    encoded_result = []
    if not item_separated:
        # for pattern in result_pattern:
        #     pattern_encoded = []
        #     for itemset in pattern[0]:
        #         item_part = ''
        #         for item in itemset:
        #             item_part = item_part + undiscrete_sequence[item]
        #         pattern_encoded.append(item_part)
        #     encoded_result.append([pattern_encoded, pattern[1]])
        for pattern in result_pattern:
            pattern_encoded = []
            print(pattern)
            for itemset in pattern[0]:
                if type(itemset) == list:
                    cell = []
                    for item in itemset:
                        cell.append(undiscrete_sequence[item])
                    pattern_encoded.append(cell)
                else:
                    pattern_encoded.append(undiscrete_sequence[itemset])
                
            encoded_result.append([pattern_encoded, pattern[1]])
    else:
        for pattern in result_pattern:
            pattern_encoded = []
            for itemset in pattern[0]:
                pattern_encoded.append(undiscrete_sequence[itemset])
            encoded_result.append([pattern_encoded, pattern[1]])

    return encoded_result
