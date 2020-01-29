# -*- coding: utf-8 -*-
import pandas as pd
from ast import literal_eval

path = './datasets'
path_res='%s/pei_dataset_modif.csv' %(path)

threshold = 0.2
options = {'threshold': threshold}

data = pd.read_csv(path_res, sep=",", header=-1, names=['sid','sequence'],converters={"sequence": literal_eval})
sids = list(data["sid"])
sequences = list(data["sequence"])
items_separated = False

import copper.dataprocessor as dp
seq = dp.discretize_sequences(sequences, items_separated)

import copper.fileprocessor as fp
u_db = fp.db_to_spmf(seq)
s_db = fp.readDB(u_db, options)

import copper.prefixspan as ps
import time
import copper.profiling as pro
mem_before = pro.get_process_memory()
mem_max_before = pro.get_max_resident_memory()
time_start = time.time()
result_mining = ps.prefixspan(s_db, options)
time_end = time.time()
mem_max_after = pro.get_max_resident_memory()
mem_after = pro.get_process_memory()
memory_max = mem_max_after - mem_max_before

result_mining_undiscretize = dp.undiscretize_sequences(data, result_mining)
fp.get_result_file(result_mining_undiscretize, options, time_start, time_end, mem_after, mem_before, mem_max_after, mem_max_before)
