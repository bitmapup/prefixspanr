# -*- coding: utf-8 -*-
# Hugo Alatrista Salas - UP
# https://github.com/bartdag/pymining

from pymining import itemmining

transactions = (('a', 'b', 'c'), ('b'), ('a'), ('a', 'c', 'd'), ('b', 'c'), ('b', 'c'))

from pymining import itemmining
relim_input = itemmining.get_relim_input(transactions)
item_sets = itemmining.relim(relim_input, min_support=2)
for itemset in item_sets:
	print itemset

from pymining import assocrules
rules = assocrules.mine_assoc_rules(item_sets, min_support=2, min_confidence=0.5)
for rule in rules:
	print rule 

import pandas as pd
import matplotlib.pyplot as plt

data = "Datos_Compras.csv"
df = pd.read_csv(data, sep=",", decimal=".")

print df