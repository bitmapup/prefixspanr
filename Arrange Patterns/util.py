import numpy as np
import pandas as pd
from ast import literal_eval

def read_results(result_path):
    result_file = open(result_path, 'r')
    sequences_raw = result_file.readlines() 
    result_file.close()
    return sequences_raw

def parseOptions(result_path):
    line = read_results(result_path)[0]
    return literal_eval(line[0:len(line)-1])

def extractPatterns(result_path):
    sequences = []
    sequences_raw = read_results(result_path)
    sequences_raw = sequences_raw[1:]

    for row in range(len(sequences_raw)):
        sequences.append(pd.Series(literal_eval(sequences_raw[row][0:len(sequences_raw[row])-1]), index=["patterns","supp", "%supp"]))

    result = pd.DataFrame(columns=['patterns', 'supp', "%supp"]).append(sequences, ignore_index=True)
    result['patterns'] = result.patterns.apply(lambda x: literal_eval(str(x)))
    return result

def getLabels(patterns):
    labels = []
    for i in range(1,getMaxpatternLen(patterns) + 1):
        labels.append("IS" + str(i))

    labels.append("supp")
    labels.append("%supp")
    return labels

def getMaxpatternLen(patterns):
    len_seq = []
    for s in patterns:
        len_seq.append(len(s))
    seq_len = np.array(len_seq)
    return max(seq_len)

def resultsTopatterns(result_path):
    patterns_raw = extractPatterns(result_path)
    list_series = []
    patterns = list(patterns_raw['patterns'])
    pattern_list = patterns_raw.values.tolist()

    for r in pattern_list:
        row_l = []
        for itemset in r[0]:
            if type(itemset) == list:
                item_format  = "< "
                for item in itemset:
                    item_format += str(item) + " "
                item_format += ">"
                row_l.append(str(item_format))
            else:
                row_l.append(str(itemset))
        
        while len(row_l) < getMaxpatternLen(patterns):
            row_l.append(" ")

        row_l.append(r[1])
        row_l.append(r[2])

        labels = getLabels(patterns)

        list_series.append(pd.Series(row_l, index=labels))

    return pd.DataFrame(columns=labels).append(list_series, ignore_index=True)


