# -*- coding: utf-8 -*-
import pandas as pd
from ast import literal_eval

path = './datasets'
path_res='%s/pei_dataset_modif.csv' %(path)

threshold = 0.2
items_separated = False
options = {'threshold': threshold, 'itemsSeparated': items_separated}

data = pd.read_csv(path_res, sep=",", header=0 ,converters={"sequence": literal_eval})
sids = list(data["sid"])
sequences = list(data["sequence"])

from copper import prefixspan as ps

result_mining = ps.prefixspan(sequences, options)
print(result_mining)