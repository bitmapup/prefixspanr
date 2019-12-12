# Contraints OPtimized PrefixSpan with Time Constrains

## Created by
**Author:** Agustin Guevara-Cogorno <br />
**Maintainer:** Yoshitomi Maehara <br />
**Contact Details:** ye.maeharaa@up.edu.pe <br />
**Institution:** Universidad del Pacifico
<br /><br />

**Note:** use Python 2.7.*

## Description
Extension of COPPER with time constraints capabilities, improving 

## Option Configurations
### Original PrefixSpan
```python
options = {'threshold' : number}
```

### COPPER
```python
options = {'threshold' : number, 'minSseq': number, 'maxSseq': number, minSize': int, 'maxSize': number, 'logic': string}
```

### Prefixspan with time constraints (WinGap)
```python
options = {'threshold' : ratio, 'window' : number, 'gap' : number}
```

### COPPER with time constraints (WinCopper)
```python
options = {'threshold' : int or float, 'minSseq': int, 'maxSseq': int, 'minSize': int, 'maxSize': int,
           window' : number, 'gap' : number, 'logic': string}
```

## Requirements
- Data should be readed in csv format
- Only the part of sequences will be processed without identificator of sequences

## How to use
- First read a data file
- Next set options values with an options configuration
```python
   # if threshold is a float this is a ratio of the length of database
   # otherwise if is a integer is a length of pattern
   threshold = 0.2
   # is a configuration of a Original PrefixSpan
   options = {'threshold': threshold}
```
- Now should be encode dataset

```python
    import copper.dataprocessor as dp
    # set of items = {'a', 'b', 'c'}
    # items_separated means if items are separated by colons (True)
    # e.g sequences = [['a',b','c'], ['a', 'b']]
    items_separated = True
    # otherwise the itemsets are separated by colons (False) [Default]
    # e.g sequences = [['ab', 'a', 'bc'], ['aa', 'bc']]
    items_separated = False
    seq = dp.discretize_sequences(sequences, items_separated)
```

- Convert discretized dataset to spmf format

```python
    import copper.fileprocessor as fp
    u_db = fp.db_to_spmf(seq)
```

- Read dataset converted

```python
    s_db = fp.readDB(u_db, options)
```

- Mining dataset with algoritms depending the options configuration

```python
    import copper.prefixspan as ps
    import time
    start = time.time()
    result_mining = ps.prefixspan(s_db, options)
    end = time.time()
    # this part measure time to processing, but this is optional
```

- Decode dataset with original values

```python
   result_mining_undiscretize = dp.undiscretize_sequences(data, result_mining)
```

- Can obtain a result file with patterns mined and some important informations

```python
   fp.get_result_file(result_mining_undiscretize, start, end, options)
```

## References
- Guevara-Cogorno, A., Flamand, C. y Alatrista-Salas, H. (2015). COPPER - Constraint OPtimized Prefixspan for Epidemiological Research. *Procedia Computer Science*, *63*, 433-438.  [[link]](http://www.sciencedirect.com/science/article/pii/S1877050915024990)
- Pei, J., Han, J., Mortazavi-Asl, B. y Pinto H. (2002). PrefixSpan,: mining sequential patterns efficiently by prefix-projected pattern growth. *Proceedings 17th International Conference on Data Engineering*. 215-224. [ [link]](http://jayurbain.com/msoe/cs498-datamining/prefixspan_mining_sequential_patterns_by_prefix_projected_growth.pdf)
- 
