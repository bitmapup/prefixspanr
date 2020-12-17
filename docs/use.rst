How to use
==========

- Data should be read in csv format with structure following.
- Only the part of sequences will be processed without his identificators.

.. Is possible use files in SPMF format with some arranges.

::

   sid,sequence
   10,"['a' , ['a','b','c'] , ['a','c'] , 'd' , ['c','f']]"
   20,"[['a','d'] , 'c' , ['b','c'] , ['a','e']]"
   30,"[['e','f'] , ['a','b'] , ['d','f'] , 'c', 'b']"
   40,"['e' , 'g' , ['a','f'] , 'c' , 'b', 'c']"

- First read a data file

.. code-block:: python
   :linenos:

   import pandas as pd
   from ast import literal_eval
   data = pd.read_csv("pei_example.csv" , sep=",", header=0,
                       converters={"sequence": literal_eval})
   sids = list(data["sid"])
   sequences = list(data["sequence"])

- Next set options values with an options configuration

.. code-block:: python
   :linenos:
    
   # use absolute threshold
   threshold = 3
   # Items separated by colons 
   items_separated = True
   # is a configuration of Original PrefixSpan
   options = {'threshold': 2, 'itemsSeparated': True}

- Mining dataset with algorithms depending the options configuration with a part of sequences, getting result of mining and generate a result file 

.. code-block:: python
   :linenos:
   
   import copper.prefixspan as ps
   result_mining = ps.prefixspan(sequences, options)
   print(result_mining)

Results:

::

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