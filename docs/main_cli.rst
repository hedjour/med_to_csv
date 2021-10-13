Command line interface 
==================================

How to use it
---------------------
You can use med_to_csv in CLI or GUI.
Here we develop the cli interface.
This interface take 3 parameters :

* 1rst is the path to your directory or file output of Medassociate
* 2nd is the path to the `config file <./config_file.html>`_
* 3rd is the path to the output file need to end by .csv

Call example :
----------------------

.. code-block:: bash

    med_to_csv_cli my_result_dir my_config_file.yml output_file.csv

ou 

.. code-block:: bash

    med_to_csv_cli my_result_file my_config_file.yml output_file.csv



Details
---------

.. automodule:: med_project.main_cli
   :members: