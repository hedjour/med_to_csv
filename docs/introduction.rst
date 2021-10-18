Introduction
=============

About
------

med_to_csv is a software that converts med associates data files into tidy data. 

Aim of the project
-------------------

This project aims to facilitate the wrangling and, later on, the analysis of med associates
resulting data by parsing several types of raw data files obtained from med associates and 
creating a tidy CSV file containing the information required.

How does it work
-----------------
Since med associates allows to fill freely the information needed, the resulting data layout
will differ from user to user. In this software, the user should specify **which** information 
to keep and **where** this information is present, in a `config file <./config_file.html>`_ 
written in YAML. The software generates a CSV file in a table format where 
each variable mentionned by the user forms a column and each observation forms a row.

.. note:: If arrays are present, unique values are repeated to match the length of longest array.