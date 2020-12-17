# WinCOPPER

## Created by
**Author:** Agustin Guevara Cogorno <br />
**Maintainer:** Yoshitomi Maehara Aliaga<br />
**Contact Details:** ye.maeharaa@up.edu.pe <br />
**Institution:** Universidad del Pacifico
<br />

**Note:** use Python 2.7.*

## Description
Extension of COPPER algorithm with time constraints capabilities, improving the selection of interesting patterns for expert.

if you use a package please cite the following paper:

> Alatrista-Salas, H., Guevara-Cogorno, A., Maehara, Y. Nunez-del-Prado, M. (2020). Efficiently Mining Gapped and Window Constraint Frequent Sequential Patterns. *Proceedings 17th International Conference on Modeling Decisions for Artificial Intelligence* [[link]](https://link.springer.com/chapter/10.1007/978-3-030-57524-3_20)

Bibtex:
```
@inproceedings{alatrista2020efficiently,
  title={Efficiently Mining Gapped and Window Constraint Frequent Sequential Patterns},
  author={Alatrista-Salas, Hugo and Guevara-Cogorno, Agustin and Maehara, Yoshitomi and Nunez-del-Prado, Miguel},
  booktitle={International Conference on Modeling Decisions for Artificial Intelligence},
  pages={240--251},
  year={2020},
  organization={Springer}
}
```

## Install
if you would install in your environment
```
python setup.py install
```
if you would install in your development environment
```
python setup.py develop
```
you can install from github by pip
```
pip install git+https://github.com/bitmapup/prefixspanr/archive/v1.0.zip
```

```copper``` depends on the following packages which will be installed by pip during the installation process

- ```psutil```
- ```pandas```
- ```numpy```
- ```resources``` (Only in Linux-like OS)

## Usage
- First read a data file
    * Data should be read in csv format with structure following
  ```python
  import pandas as pd
  from ast import literal_eval
  path_res = "pei_dataset_modif.csv"
  data = pd.read_csv(path_res, sep=",", header=0, converters={"sequence": literal_eval})
  sids = list(data["sid"])
  sequences = list(data["sequence"])
  ```
  ```
  sid,sequence
  10,"['a' , ['a','b','c'] , ['a','c'] , 'd' , ['c','f']]"
  20,"[['a','d'] , 'c' , ['b','c'] , ['a','e']]"
  30,"[['e','f'] , ['a','b'] , ['d','f'] , 'c', 'b']"
  40,"['e' , 'g' , ['a','f'] , 'c' , 'b', 'c']"
  ```
    * Only the part of sequences will be processed without ids of sequences

- Next set options values with an options configuration
```python
# Absolute threshold 
threshold = 3
# Contains k-itemsets separated by commas
items_separated = False
# is a configuration of a Original PrefixSpan
options = {'threshold': threshold, 'itemsSeparated': items_separated}
```
- Mining dataset with algorithms depending the options configuration with a part of sequences, getting result of mining and generate a result file

```python
import copper

result_mining = copper.prefixspan(sequences, options)
print(result_mining)
```
```
[[['a'], 4, 1.0],
[['a', 'b'], 4, 1.0],
[['a', ['b', 'c']], 3, 0.75],
[['a', 'c'], 4, 1.0],
[['a', 'c', 'c'], 3, 0.75],
[['b'], 4, 1.0],
[[['b', 'c']], 3, 0.75],
[['b', 'c'], 3, 0.75],
[['c'], 4, 1.0],
[['c', 'c'], 3, 0.75],
[['d'], 3, 0.75],
[['d', 'c'], 3, 0.75],
[['e'], 3, 0.75],
[['f'], 3, 0.75]]
```

## Configuration Options

### Algorithm Configurations

**1) Original PrefixSpan**
```python
options = {'threshold' : int or float}
```
#### Descriptions
- **threshold:**  support of patterns
    * if threshold value is *integer* means the size of sequences (Absolute Support)
    * if threshold value is *float* means the percent of size of database (Ratio Support)

**2) COPPER**
```python
options = {'threshold' : int or float,
           'minSseq': int, 'maxSseq': int,
           'minSize': int, 'maxSize': int,
           'logic': string}
```
#### Descriptions
- **threshold:**  support of patterns
    * if threshold value is *integer* means the size of sequences (Absolute Support)
    * if threshold value is *float* means the percent of size of database (Relative  Support)
- **minSseq:**  minimum itemset size constraint
- **maxSseq:**  maximum itemset size constraint
- **minSize:**  minimum pattern size constraint
- **maxSize:**  maximum pattern size constraint
- **logic:**  soft inclusion constraint
    * OR relation '(s1 | s2)'
    * AND relation '(s1 & s2)'

**3) Prefixspan with time constraints (WinGap)**
```python
options = {'threshold' : int or float, 'window' : int, 'gap' : int}
```
#### Descriptions
- **threshold:**  support of patterns
    * if threshold value is *integer* means the size of sequences (Absolute Support)
    * if threshold value is *float* means the percent of size of database (Relative  Support)
- **window:**  maximum windows size between itemsets constraint
- **gap:**  maximum gap between itemsets constraint

**4) COPPER with time constraints (WinCopper)**
```python
options = {'threshold' : int or float,
           'minSseq': int, 'maxSseq': int,
           'minSize': int, 'maxSize': int,
           'window' : int, 'gap' : int,
           'logic': string}
```
#### Descriptions
- **threshold:**  support of patterns
    * if threshold value is an *integer* means the size of sequences (Absolute Support)
    * if threshold value is a *float* means the percent of size of database (Relative Support)
- **minSseq:**  minimum itemset size constraint
- **maxSseq:**  maximum itemset size constraint
- **minSize:**  minimum pattern size constraint
- **maxSize:**  maximum pattern size constraint
- **logic:**  soft inclusion constraint
    * OR relation '(s1 | s2)'
    * AND relation '(s1 & s2)'
- **window:**   maximum windows size between itemsets constraint
- **gap:**  maximum gap between itemsets constraint

###  Other Options
```python
options = {'itemsSeparated': bool, 'dataDesc': string,
           'resultFile': bool, 'test': bool}
```
#### Descriptions
- **itemsSeparated:**  Flag of separation of itemsets
    * if itemsSeparated value is *True* means the sequence only contain 1-itemsets
    * if itemsSeparated value is *False* means the sequence contain k-itemsets **[Default]**
- **dataDesc:**  Put describing name of dataset used or note in a name of results file
- **resultFile:** Flag of generation result file
    * if test value is *True* means the result file will be generated **[Default]**
    * if test value is *False* means the result file will not be generated
- **test:**  Flag of generation of summary of tests file *(For Experimental Purpouses)*
    * if test value is *True* means the summary of test will be generated
    * if test value is *False* means the summary of test will not be generated **[Default]**


## References
- Guevara-Cogorno, A., Flamand, C. y Alatrista-Salas, H. (2015). COPPER - Constraint OPtimized Prefixspan for Epidemiological Research. *Procedia Computer Science*, *63*, 433-438.  [[link]](http://www.sciencedirect.com/science/article/pii/S1877050915024990)
- Pei, J., Han, J., Mortazavi-Asl, B. y Pinto H. (2002). PrefixSpan,: mining sequential patterns efficiently by prefix-projected pattern growth. *Proceedings 17th International Conference on Data Engineering*. 215-224. [[link]](http://jayurbain.com/msoe/cs498-datamining/prefixspan_mining_sequential_patterns_by_prefix_projected_growth.pdf)


