# -*- coding: utf-8 -*-

"""
module for preprocess and postprocess data.
"""

import numpy as np


def get_unique_items(database, item_separated=False):
    """
    Obtain a unique itemsets or items of sequence

    Parameters
    ----------
    database : list
        database of sequences
    item_separated : bool
        True: items in itemsets are separated by colon
        False or blank: itemsets are separated by colon

    Returns
    -------
    list
        unique items list

    """
    sequence_set = []

    if not item_separated:
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


def encode_sequences(raw_db, item_separated=False):
    """
    Encode a sequence in numbers

    Parameters
    ----------
    raw_db : list
        database of sequences without preprocessing
    item_separated : bool
        True: items in itemsets which are in sequence are separated by colon
        False or blank: itemsets which are in sequence are separated by colon

    Returns
    -------
    list
        database encoded

    """
    # isolate this part
    sequence_set = get_unique_items(raw_db, item_separated)
    discrete_sequence = {sequence_set[i]: str(i + 1) for i in range(0, len(sequence_set))}

    db = []
    if not item_separated:
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

    Parameters
    ----------
    result_patterns : list
        results patterns of sequential pattern mining

    Returns
    -------
    string
        pattern convert to string
    """
    str_result_patterns = result_patterns
    for i in range(len(result_patterns)):
        str_result_patterns[i][0] = str(result_patterns[i][0])
    return str_result_patterns


def pattern_to_list(result_patterns):
    """
    convert pattern format to list

    Parameters
    ----------
    result_patterns : list
        results patterns of sequential pattern mining


    Returns
    -------
    list
        results patterns mined in a list
    """
    str_result_patterns = result_patterns_to_str(result_patterns)
    result_pattern_list = []
    itemset = ''
    for row_pattern in str_result_patterns:
        pattern = []
        for ch in row_pattern[0]:
            if ch != '<' and ch != '>' and ch != ' ':
                itemset += ch

            if ch == '>':
                if ',' in itemset:
                    pattern.append(itemset.split(','))
                else:
                    pattern.append(itemset)
                itemset = ''
        if len(pattern) == 1:
            if type(pattern[0]) == list:
                pattern = pattern[0]
        result_pattern_list.append([pattern, row_pattern[1], row_pattern[2]])
    return result_pattern_list


def decode_sequences(raw_db, result_pattern_list, item_separated=False):
    """
    cast patterns to string

    Parameters
    ----------
    raw_db : list
        database of sequences without preprocessing

    result_pattern_list : list
        results patterns of sequential pattern mining

    item_separated : bool
        True: items in itemsets which are in sequence are separated by colon
        False or blank: itemsets which are in sequence are separated by colon

    Returns
    -------
    string
        database decoded
    """

    # isolate this part
    sequence_set = get_unique_items(raw_db, item_separated)
    decoded_sequence = {str(i + 1): sequence_set[i] for i in range(0, len(sequence_set))}

    result_pattern = pattern_to_list(result_pattern_list)
    decoded_result = []
    if not item_separated:
        for pattern in result_pattern:
            pattern_decoded = []
            for itemset in pattern[0]:
                if type(itemset) == list:
                    cell = []
                    for item in itemset:
                        cell.append(decoded_sequence[item])
                    pattern_decoded.append(cell)
                else:
                    pattern_decoded.append(decoded_sequence[itemset])

            decoded_result.append([pattern_decoded, pattern[1], pattern[2]])
    else:
        for pattern in result_pattern:
            pattern_decoded = []
            for itemset in pattern[0]:
                pattern_decoded.append(decoded_sequence[itemset])
            decoded_result.append([pattern_decoded, pattern[1], pattern[2]])
    return decoded_result


def encode_logic(raw_db, options):
    """
    encode parse logic of soft inclussion constraint

    Parameters
    ----------
    raw_db : list
        database of sequences without preprocessing

    options : dict
        options to config

    Returns
    -------
    string
        logic encoded
    """
    logic = str(options['logic'])
    logic = ''.join(logic.split())
    encoded = ''
    item = ''
    i = 0
    sequence_set = get_unique_items(raw_db)
    discrete_sequence = {sequence_set[i]: str(i + 1) for i in range(0, len(sequence_set))}
    while True:

        if logic[i] != '(' and logic[i] != '|' and logic[i] != '&' and logic[i] != ')':
            item += logic[i]
            i += 1

        if logic[i] == '(':
            encoded += logic[i]
            i += 1

        if logic[i] == '|' or logic[i] == '&' or logic[i] == ')':
            item = discrete_sequence[item]
            encoded += item
            encoded += logic[i]
            item = ''
            i += 1

        if i >= len(logic):
            break

    return encoded


def seqs_len(sequences):
    """
    obtain all length of sequences

    Parameters
    ----------
    sequences : list
        database of sequences without preprocessing

    Returns
    -------
    array
        length of sequences
    """
    len_seq = []
    for sequence in sequences:
        len_seq.append(len(sequence))
    return np.array(len_seq)


def max_seq_len(sequences):
    """
    obtain maximum length of sequences

    Parameters
    ----------
    sequences : list
        database of sequences without preprocessing

    Returns
    -------
    int
        maximum length of sequences
    """
    return max(seqs_len(sequences))


def min_seq_len(sequences):
    """
    obtain minimum length of sequences

    Parameters
    ----------
    sequences : list
        database of sequences without preprocessing

    Returns
    -------
    Numpy Array
        minimum length of sequences
    """
    return min(seqs_len(sequences))


def avg_seq_len(sequences):
    """
    obtain average length of sequences

    Parameters
    ----------
    sequences : list
        database of sequences without preprocessing

    Returns
    -------
    Numpy Array
        average length of sequences
    """
    return int(round(np.mean(seqs_len(sequences)), 0))


def itemsets_len(sequences):
    """
    obtain length of all itemsets of all sequences

    Parameters
    ----------
    sequences : list
        database of sequences without preprocessing

    Returns
    -------
    Numpy Array
        average length of sequences
    """
    len_is = []
    for sequence in sequences:
        for itemset in sequence:
            if type(itemset) == list:
                len_is.append(len(itemset))
            else:
                len_is.append(len([itemset]))

    return np.array(len_is)


def max_itemsets_len(sequences):
    """
    obtain maximum length of all itemsets of all sequences

    Parameters
    ----------
    sequences : list
        database of sequences without preprocessing

    Returns
    -------
    int
        maximum length of itemsets of all sequences
    """
    return max(itemsets_len(sequences))


def min_itemsets_len(sequences):
    """
    obtain minimum length of all itemsets of all sequences

    Parameters
    ----------
    sequences : list
        database of sequences without preprocessing

    Returns
    -------
    int
        minimum length of itemsets of all sequences
    """
    return min(itemsets_len(sequences))


def avg_itemsets_len(sequences):
    """
    obtain average length of all itemsets of all sequences

    Parameters
    ----------
    sequences : list
        database of sequences without preprocessing

    Returns
    -------
    int
        average length of itemsets of all sequences
    """
    return int(round(np.mean(itemsets_len(sequences)), 0))
