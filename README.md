# Contraints OPtimized PrefixSpan with Time Constrains

## Created by
**Author:** Agustin Guevara-Cogorno <br />
**Maintainer:** Yoshitomi Maehara <br />
**Contact Details:** ye.maeharaa@up.edu.pe <br />
**Institution:** Universidad del Pacifico
<br />

**Note:** use Python 2.7.*

# Dependencies

- psutil
- pandas
- numpy
- resources (Only in Linux)

## Description
Extension of COPPER with time constraints capabilities, improving the selection of interesting patterns for expert

## Options
### Algorithm Configurations

**1) Original PrefixSpan**
```python
options = {'threshold' : number}
```
#### Descriptions
- **threshold:** support of patterns
  * if threshold value is *integer* means the size of sequences (Absolute Support)
  * if threshold value is *float* means the percent of size of database (Ratio Support)

**2) COPPER**
```python
options = {'threshold' : number, 'minSseq': number, 'maxSseq': number, 'minSize': number, 'maxSize': number, 'logic': string}
```
#### Descriptions
- **threshold:** support of patterns
  * if threshold value is *integer* means the size of sequences (Absolute Support)
  * if threshold value is *float* means the percent of size of database (Relative  Support)
- **minSseq:**  minimum itemset size constraint
- **maxSseq:**  maximum itemset size constraint
- **minSize:**  minimum pattern size constraint
- **maxSize:**  maximum pattern size constraint
- **logic:**    soft inclusion constraint
  * OR relation '(s1 | s2)'
  * AND relation '(s1 & s2)'

**3) Prefixspan with time constraints (WinGap)**
```python
options = {'threshold' : number, 'window' : number, 'gap' : number}
```
#### Descriptions
- **threshold:** support of patterns
  * if threshold value is *integer* means the size of sequences (Absolute Support)
  * if threshold value is *float* means the percent of size of database (Relative  Support)
- **window:**   maximum windows size between itemsets constraint
- **gap:**      maximum gap between itemsets constraint

**4) COPPER with time constraints (WinCopper)**
```python
options = {'threshold' : number, 'minSseq': number, 'maxSseq': number, 'minSize': number, 'maxSize': number, 'window' : number, 'gap' : number, 'logic': string}
```
#### Descriptions
- **threshold:** support of patterns
  * if threshold value is *integer* means the size of sequences (Absolute Support)
  * if threshold value is *float* means the percent of size of database (Relative Support)
- **minSseq:**  minimum itemset size constraint
- **maxSseq:**  maximum itemset size constraint
- **minSize:**  minimum pattern size constraint
- **maxSize:**  maximum pattern size constraint
- **logic:**    soft inclusion constraint
  * OR relation '(s1 | s2)'
  * AND relation '(s1 & s2)'
- **window:**   maximum windows size between itemsets constraint
- **gap:**      maximum gap between itemsets constraint

###  Other Options
```python
options = {'itemsSeparated': boolean}
```
#### Descriptions
- **itemsSeparated:** Flag of separation of itemsets
  * if itemsSeparated value is *True* means the sequence contain k-itemsets 
  * if itemsSeparated value is *False* means the sequence only contain 1-itemsets  

## Requirements
- Data should be readed in csv format
- Only the part of sequences will be processed without identificators of sequences

## How to use
- First read a data file
- Next set options values with an options configuration
```python
   # if threshold is a float this is a ratio of the length of database (Relative  Support)
   # otherwise if is a integer is a length of pattern (Absolute Support)
   threshold = 0.2
   # Items separated examples
   # set of items = {'a', 'b', 'c'}
   # items_separated means if items are separated by colons (True)
   # e.g sequences = [['a',b','c'], ['a', 'b']]
   # otherwise the itemsets are separated by colons (False) [Default]
   # e.g sequences = [[['a','b'], 'a', ['b','c']], [['a','a'], ['b','c']]]
   items_separated = True
   # is a configuration of a Original PrefixSpan
   options = {'threshold': threshold, 'itemsSeparated': items_separated}
```
- Mining dataset with algorithms depending the options configuration with a part of sequences, getting result of mining and generate a result file 

```python
    result_mining = ps.prefixspan(sequences, options)
    # if do not assign a variable only obtain the result file
    print(result_mining)
```

## References
- Guevara-Cogorno, A., Flamand, C. y Alatrista-Salas, H. (2015). COPPER - Constraint OPtimized Prefixspan for Epidemiological Research. *Procedia Computer Science*, *63*, 433-438.  [[link]](http://www.sciencedirect.com/science/article/pii/S1877050915024990)
- Pei, J., Han, J., Mortazavi-Asl, B. y Pinto H. (2002). PrefixSpan,: mining sequential patterns efficiently by prefix-projected pattern growth. *Proceedings 17th International Conference on Data Engineering*. 215-224. [ [link]](http://jayurbain.com/msoe/cs498-datamining/prefixspan_mining_sequential_patterns_by_prefix_projected_growth.pdf)
