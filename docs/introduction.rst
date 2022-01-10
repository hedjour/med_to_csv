Introduction
=============

About
------

med_to_csv is a software that converts med associates data files into tidy data. 

Aim of the project
-------------------

This project aims at facilitating the wrangling and the analysis of data by parsing raw data files obtained from 
MedAssociates operant chambers, in a given folder, and creating a tidy CSV file containing the information required.

How does it work?
------------------
Since med associates allows to fill freely the information needed, the resulting data layout
will differ from user to user. In this software, the user should specify in a `config file <./config_file.html>`_ 
written in YAML:

#. **Which** information to retrieve (i.e naming specific variables) and
#. **Where** this information is present in the original data file (i.e. in which line the variable is written).

The software generates a CSV file in a table format where 
each variable mentionned by the user produces a column and each observation produces a row.

.. note:: If arrays are present, unique values are repeated to match the length of longest array.