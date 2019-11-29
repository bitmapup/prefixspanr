import csv
#import matplotlib.pyplot as plt

transactions = []

path_res='german_encoded.csv'

with open(path_res) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        transactions.append(row)

from pymining import itemmining
relim_input = itemmining.get_relim_input(transactions)
item_sets = itemmining.relim(relim_input, min_support=2)

from pymining import assocrules
rules = assocrules.mine_assoc_rules(item_sets, min_support=2, min_confidence=0.5)

itemsets = open('itemsets.txt', 'w')
for item in item_sets:
    itemsets.write(item)
itemsets.close()

rulesassoc = open('rules.txt', 'w')
for rule in rules:
    rulesassoc.write(rule)
rulesassoc.close()
