# -*- coding: utf-8 -*-
import pandas as pd
from ast import literal_eval
import wincopper as wc

# path = '.'
# path_res = '%s/pei_dataset_modif.csv' % path
path_res = "pei_dataset_modif.csv"

threshold = 3
items_separated = False
options = {'threshold': threshold, 'itemsSeparated': items_separated}

data = pd.read_csv(path_res, sep=",", header=0, converters={"sequence": literal_eval})
sids = list(data["sid"])
sequences = list(data["sequence"])

result_mining = wc.prefixspan(sequences, options)
print(result_mining)
# for l in result_mining:
#    print(l)
