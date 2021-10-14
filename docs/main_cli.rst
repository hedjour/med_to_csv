Command line interface 
==================================

How to use it
---------------------
You can use med_to_csv in CLI or GUI.
Here we develop the cli interface.
This interface takes 3 parameters :

* 1st is the path to your directory or file output of Medassociate
* 2nd is the path to the `config file <./config_file.html>`_
* 3rd is the path to the output file which must end by .csv

Call example
----------------------
Run the following command on the file or directory containing the datas

.. code-block:: bash

    med_to_csv_cli my_results my_config_file.yml output_file.csv

Details
---------

.. automodule:: med_project.main_cli
   :members: