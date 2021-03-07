# WinCOPPER

## Created by
**Author:** Agustin Guevara-Cogorno <br />
**Advisors** Hugo Alatrista-Salas and Miguel Nuñez-del-Prado <br />
**Maintainer:** Yoshitomi Maehara Aliaga <br />
**Contact Details:** h.alatristas@up.edu.pe <br />
**Institution:** Universidad del Pacifico / Pontificia Universidad Católica del Perú
<br />

**Note:** use Python 2.7.*

## Description
WinCOPPER [3] is an extension of COPPER algorithm [1], originally developed to extract sequential patterns [2] under items-inclusion constraint. New WinCOPPER incorporates - also - time constraints capabilities, improving the extraction of useful patterns.

If WinCopper is used in your experimentations, please, we will be grateful if you cite us:

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
### Install WinCOPPER thought Source Code
You can clone the Github repository, or you can download the code source. For both options, WinCOPPER could be installed using the following instructions:
```
python setup.py install
```
Also, if you prefer to install WinCOPPER in your development environment, you can use this:
```
python setup.py develop
```
### Install WinCopper thought PIP
A simple way to install WinCOPPER is through PIP:
```
pip install git+https://github.com/bitmapup/prefixspanr.git
```
Also, you can select a specific version o  WinCOPPER through the instruction.
```
pip install git+https://github.com/bitmapup/prefixspanr.git@v1.0
```

```wincopper``` depends on the following packages. Please, be sure that these packages are correctly installed before installing WinCOPPER.

- ```psutil```
- ```pandas```
- ```numpy```
- ```resources``` (Only in Linux-like OS)

## WinCopper usage example
1. Read the CSV dataset (an example of the input file is shown in the example folder). 
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

2. Set the WinCOPPER options values with (see next section).
```python
# Absolute threshold 
threshold = 3
# Contains k-itemsets separated by commas
items_separated = False
# is a configuration of a Original PrefixSpan
options = {'threshold': threshold, 'itemsSeparated': items_separated}
```
3. Mine the dataset with WinCOPPER incorporating the options settled in the previous step.

```python
import wincopper as wc
# Run algorithm
result_mining = wc.prefixspan(sequences, options)

for l in result_mining:
    print(l)
```
```
['<a>', 4, 1.0]
['<a><b>', 4, 1.0]
['<a><c>', 4, 1.0]
['<a><c><b>', 3, 0.75]
['<a><c><c>', 3, 0.75]
['<b>', 4, 1.0]
['<b><c>', 3, 0.75]
['<c>', 4, 1.0]
['<c><b>', 3, 0.75]
['<c><c>', 3, 0.75]
['<d>', 3, 0.75]
['<d><c>', 3, 0.75]
['<e>', 3, 0.75]
['<f>', 3, 0.75]
```

## Configuration Options

It is worth noting that, WinCOPPER includes capabilities of PrefixSpam [2] and Copper [1] algorithms.

### Algorithm Configurations

**1) Original PrefixSpan [2] **
```python
options = {'threshold' : int or float}
```
#### Descriptions
- **threshold:**  support of patterns
    * If the threshold value is an *integer*, WinCopper assumes that an Absolute Support is using.
    * If the threshold value is a *float*, WinCopper assumes that a Relative Support is using.

**2) COPPER**
```python
options = {'threshold' : int or float,
           'minSseq': int, 'maxSseq': int,
           'minSize': int, 'maxSize': int,
           'logic': string}
```
#### Descriptions
- **threshold:**  support of patterns
    * If the threshold value is an *integer*, WinCopper assumes that an Absolute Support is using.
    * If the threshold value is a *float*, WinCopper assumes that a Relative Support is using.
- **minSseq:**  minimum itemset size constraint (itemset size)
- **maxSseq:**  maximum itemset size constraint (itemset size)
- **minSize:**  minimum pattern size constraint (subsequence size)
- **maxSize:**  maximum pattern size constraint (subsequence size)
- **logic:**  soft inclusion constraint
    * OR relation '(s1 | s2)'
    * AND relation '(s1 & s2)'

**3) Prefixspan with time constraints (WinGap)**
```python
options = {'threshold' : int or float, 'window' : int, 'gap' : int}
```
#### Descriptions
- **threshold:**  support of patterns
    * If the threshold value is an *integer*, WinCopper assumes that an Absolute Support is using.
    * If the threshold value is a *float*, WinCopper assumes that a Relative Support is using.
- **window:**  maximum windows size between itemsets 
- **gap:**  maximum gap between itemsets

**4) WinCOPPER (Copper with time constraints)**
```python
options = {'threshold' : int or float,
           'minSseq': int, 'maxSseq': int,
           'minSize': int, 'maxSize': int,
           'window' : int, 'gap' : int,
           'logic': string}
```
#### Descriptions
- **threshold:**  support of patterns
    * If the threshold value is an *integer*, WinCopper assumes that an Absolute Support is using.
    * If the threshold value is a *float*, WinCopper assumes that a Relative Support is using.
- **minSseq:**  minimum itemset size constraint (itemset size)
- **maxSseq:**  maximum itemset size constraint (itemset size)
- **minSize:**  minimum pattern size constraint (subsequence size)
- **maxSize:**  maximum pattern size constraint (subsequence size)
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
- **itemsSeparated:**  Flag for separation of itemsets
    * If the itemsSeparated value is *True*, patterns will contain only 1-itemsets
    * If the itemsSeparated value is *False*, patterns will contain k-itemsets **[Default]**
- **dataDesc:**  Allows fixing a name to the results file.
- **resultFile:** Flag for generating a results file
    * If the resultFile value is *True*, a file with the extracted patterns will be generated. **[Default]**
    * If the resultFile value is *False*, a file will not be generated.
- **test:**  Flag for generating a summary of tests file *(for experimentation purpouses)*
    * If the test value is *True*, a summary of test will be generated
    * If the test value is *False*, a summary of test will not be generated **[Default]**


## References
- [1] Guevara-Cogorno, A., Flamand, C. y Alatrista-Salas, H. (2015). COPPER - Constraint OPtimized Prefixspan for Epidemiological Research. *Procedia Computer Science*, *63*, 433-438.  [[link]](http://www.sciencedirect.com/science/article/pii/S1877050915024990)
- [2] Pei, J., Han, J., Mortazavi-Asl, B. y Pinto H. (2002). PrefixSpan,: mining sequential patterns efficiently by prefix-projected pattern growth. *Proceedings 17th International Conference on Data Engineering*. 215-224. [[link]](http://jayurbain.com/msoe/cs498-datamining/prefixspan_mining_sequential_patterns_by_prefix_projected_growth.pdf)
- [3] Alatrista-Salas H., Guevara-Cogorno A., Maehara Y., Nunez-del-Prado M. (2020) Efficiently Mining Gapped and Window Constraint Frequent Sequential Patterns. In: Torra V., Narukawa Y., Nin J., Agell N. (eds) Modeling Decisions for Artificial Intelligence. MDAI 2020. Lecture Notes in Computer Science, vol 12256. Springer, Cham. [[link]](https://doi.org/10.1007/978-3-030-57524-3_20)


