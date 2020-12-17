Package Options
===============

Algorithm Configurations
------------------------

Original PrefixSpan
*******************

.. code-block:: python
   :linenos:

   options = {'threshold' : int or float}


**Descriptions**

- **threshold:** support of patterns

  - if threshold value is *integer* means the size of sequences (Absolute Support)
  - if threshold value is *float* means the percent of size of database (Ratio Support)

COPPER
******

.. code-block:: python
   :linenos:

   options = {'threshold' : int or float,
              'minSseq': int, 'maxSseq': int,
              'minSize': int, 'maxSize': int,
              'logic': string}


**Descriptions**

- **threshold:** support of patterns

  - if threshold value is *integer* means the size of sequences (Absolute Support)
  - if threshold value is *float* means the percent of size of database (Relative  Support)

- **minSseq:**  minimum itemset size constraint
- **maxSseq:**  maximum itemset size constraint
- **minSize:**  minimum pattern size constraint
- **maxSize:**  maximum pattern size constraint
- **logic:**  soft inclusion constraint

  - OR relation '(s1 | s2)'
  - AND relation '(s1 & s2)'

Prefixspan with time constraints (WinGap)
*****************************************

.. code-block:: python
   :linenos:

   options = {'threshold' : int or float, 'window' : int, 'gap' : int}

**Descriptions**

- **threshold:** support of patterns

  - if threshold value is *integer* means the size of sequences (Absolute Support)
  - if threshold value is *float* means the percent of size of database (Relative  Support)

- **window:**   maximum windows size between itemsets constraint
- **gap:**  maximum gap between itemsets constraint

COPPER with time constraints (WinCopper)
****************************************

.. code-block:: python
   :linenos:

   options = {'threshold' : int or float, 
              'minSseq': int, 'maxSseq': int,
	          'minSize': int, 'maxSize': int,
	          'window' : int, 'gap' : int,
	          'logic': string}


**Descriptions**

- **threshold:** support of patterns

  - if threshold value is an *integer* means the size of sequences (Absolute Support)
  - if threshold value is a *float* means the percent of size of database (Relative Support)

- **minSseq:**  minimum itemset size constraint
- **maxSseq:**  maximum itemset size constraint
- **minSize:**  minimum pattern size constraint
- **maxSize:**  maximum pattern size constraint
- **logic:**  soft inclusion constraint

  - OR relation '(s1 | s2)'
  - AND relation '(s1 & s2)'

- **window:**   maximum windows size between itemsets constraint
- **gap:**  maximum gap between itemsets constraint

Other Options
*************

.. code-block:: python
   :linenos:

   options = {'itemsSeparated': bool, 'dataDesc': string, 
              'resultFile': bool, 'test': bool}


**Descriptions**

- **itemsSeparated:** Flag of separation of itemsets

  - if itemsSeparated value is *True* means the sequence contain k-itemsets
  - if itemsSeparated value is *False* means the sequence only contain 1-itemsets **[Default]**

- **dataDesc:** Put describing name of dataset used or note in a name of results file
- **resultFile:** Flag of generation result file

  - if test value is *True* means the result file will be generated **[Default]**
  - if test value is *False* means the result file will not be generated

- **test:** Flag of generation of summary of tests file *(For Experimental Purpouses)*

  - if test value is *True* means the summary of test will be generated
  - if test value is *False* means the summary of test will not be generated **[Default]**

