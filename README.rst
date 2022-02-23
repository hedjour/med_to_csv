.. role:: raw-html(raw)
   :format: html

|Contributors| |Forks| |Stargazers| |Issues| |GPLv3.0 License| |Doc| |DOI|

.. _top:

.. image:: /docs/img/intro_light.png#gh-light-mode-only
.. image:: /docs/img/intro_dark.png#gh-dark-mode-only

MedAssociates to CSV file
==========================

A simple way to parse MedAssociate output file in tidy data :
   * 1 row = 1 observation
   * 1 col = 1 var
   

`Explore the docs » <https://med-to-csv.readthedocs.io/>`_

`View Demo <https://github.com/hedjour/med_to_csv>`_ ·
`Report Bug <https://github.com/hedjour/med_to_csv/issues>`_ ·
`Request Feature <https://github.com/hedjour/med_to_csv/issues>`_

.. TABLE OF CONTENTS
.. .. contents:: Table of Contents
..    :depth: 2

.. raw:: html

   <details open="open">
     <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
     <ol>
       <li>
         <a href="#about-the-project">About The Project</a>
         <ul>
           <li><a href="#built-with">Built With</a></li>
         </ul>
       </li>
       <li>
         <a href="#getting-started">Getting Started</a>
         <ul>
           <li><a href="#prerequisites">Prerequisites</a></li>
           <li><a href="#installation">Installation</a></li>
           <li><a href="#make-executable">Make Executable</a> </li>
         </ul>
       </li>
       <li>
         <a href="#usage">Usage</a></li>
         <ul>
           <li><a href="#Graphical-User-Interface">Graphical User Interface</a></li>
           <li><a href="#Command-Line-Interface">Command Line Interface</a></li>
           <li><a href="#config-file">Config file</a></li>
         </ul>
       <li><a href="#roadmap">Roadmap</a></li>
       <li><a href="#contributing">Contributing</a></li>
       <li><a href="#license">License</a></li>
       <li><a href="#contact">Contact</a></li>
       <li><a href="#acknowledgements">Acknowledgements</a></li>
     </ol>
   </details>


About The Project
-----------------

This program parses MedAssociates data files and transforms them into tidy csv files, containing the information selected by the user

.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


Built With
^^^^^^^^^^


* `Python 3 <https://www.python.org/>`_
* `Gooey <https://github.com/chriskiehl/Gooey>`_

.. `back to top <#top>_`

.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


Getting Started
---------------

To get a local copy up and running follow these simple steps.

Prerequisites
^^^^^^^^^^^^^

This is an example of how to list things you need to use the software and how to install them.

* pip

   .. code-block:: bash

      pip install numpy argparse pyaml pandas
      pip install Gooey #For graphical interface

Installation
^^^^^^^^^^^^


#. Clone the repository

   .. code-block:: bash
      
      git clone https://sourcesup.renater.fr/anonscm/git/medanalysis/medanalysis.git

#. Install the required packages

   .. code-block:: bash

      pip install numpy argparse yaml pandas
      pip install Gooey #For graphical interface
      cd path/to/directory_of_git_clone
and one of the two lines below :
   .. code-block:: bash
      
      python setup.py install 
      python setup.py install --user #For windows users
or
   .. code-block:: bash
      
      pip install .


.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>

Make Executable (Portable)
^^^^^^^^^^^^^^^^^^^^^^^^^^

To make a gui onefile executable run these commands in terminal.

   .. code-block:: bash

      cd path/to/directory_of_git_clone
      pyinstaller build_gui.spec 

To make a cli onefile executable run these commands in terminal.

   .. code-block:: bash

      cd path/to/directory_of_git_clone
      pyinstaller build_cli.spec

Example
-----------------

Graphical User Interface
^^^^^^^^^^^^^^^^^^^^^^^^

Run the application and follow the steps on the interface

   .. code-block:: bash

      ./main_gui

Command Line Interface
^^^^^^^^^^^^^^^^^^^^^^

The software runs on the experiment directory that contains the directories containing the raw data files or on the file itself and returns a csv file 

   .. code-block:: bash

      ./main_cli.py path_to_medassociate_file config_file.yml output_csv_file

Config file
^^^^^^^^^^^

The config file is a necessary file that specifies the setup of your data to the software.
You can find as an example the config.yml which contains all possibilities of setup.
You can mix 1 col file dir and annotated directory file in experiment dir.


#. There are three types of parameters:

   * info_col : One column file
   * info_lab : annotated file
   * options : further options

#. For the first two types of parameters.
   You need to indicate the information in this format: "Key : Value"

   * Keys are the column names that you want in the output file
   * Values are:

     * for infos_col: row number - 1 (Start index :0)
     * for infos_lab: letters used in medAssociate exercise
     * for infos_opt: (see next point)

#. Options:

   * remove_zero_ending : True or False to keep or remove Zeros at the end of arrays
   * Cut : for cutting an output on a special character usually a dot into 2 columns. The value must be a list of list of 4 elements :

     * key to cut
     * separator usually the dot character
     * Col names of first sub-element
     * Col names of second sub-element

   * Eval : for some columns the values must be the result of a Python command line (e.g to get information in a path). It must be a python dictionary with Key as column name and value a short command line as a string.

#. The following Keys are med associate keywords only usable with annotated file :

   * Start Date (automatically added)
   * End Date
   * Subject
   * Experiment
   * Group
   * Box
   * Start Time (automatically added)
   * End Time
   * MSN: Medassociate exercice names

.. note:: Templates are available in the config.yml file


.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>



Roadmap
-------


* Add possibility for annotated file to not specify the YAML file and use YAML in parameter path with the same
  names as MPC name obtained from MSN []

.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


Contributing
------------

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have any suggestion that would improve this software, please fork the repository and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!


#. Fork the Project
#. Create your Feature Branch (\ ``git checkout -b feature/AmazingFeature``\ )
#. Commit your Changes (\ ``git commit -m 'Add some AmazingFeature'``\ )
#. Push to the Branch (\ ``git push origin feature/AmazingFeature``\ )
#. Open a Pull Request

.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


License
-------

Distributed under the GPL v3.0 License. See ``LICENSE.txt`` for more information.


.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


Contact
-------


* Jean-Emmanuel Longueville - jean.emmanuel.longueville@univ-poitiers.fr
* Myriam Hanna - myriam.hanna@univ-poitiers.fr
* Marcello Solinas

Project Link: `https://github.com/hedjour/med_to_csv <https://github.com/hedjour/med_to_csv>`_


.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


Acknowledgments
---------------


* `IRESP <https://iresp.net/>`_: This work was supported by a grant from the IRESP « IRESP-19-ADDICTIONS-20 » to MS
* `LNEC <https://lnec.labo.univ-poitiers.fr/>`_
* `Université de Poitiers <https://univ-poitiers.fr>`_
* `INSERM <https://inserm.fr>`_
* `Logo FreeVector.com <https://www.freevector.com/smiling-rat-logo>`_

.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


.. MARKDOWN LINKS & IMAGES 
.. https://www.markdownguide.org/basic-syntax/#reference-style-links

.. |Contributors| image:: https://img.shields.io/github/contributors/hedjour/med_to_csv.svg?style=for-the-badge
   :target: https://github.com/hedjour/med_to_csv/graphs/contributors
.. |Forks| image:: https://img.shields.io/github/forks/hedjour/med_to_csv.svg?style=for-the-badge
   :target: https://github.com/hedjour/med_to_csv/network/members
.. |Stargazers| image:: https://img.shields.io/github/stars/hedjour/med_to_csv.svg?style=for-the-badge
   :target: https://github.com/hedjour/med_to_csv/stargazers
.. |Issues| image:: https://img.shields.io/github/issues/hedjour/med_to_csv.svg?style=for-the-badge
   :target: https://github.com/hedjour/med_to_csv/issues
.. |GPLv3.0 License| image:: https://img.shields.io/github/license/hedjour/med_to_csv.svg?style=for-the-badge
   :target: https://github.com/hedjour/med_to_csv/blob/master/LICENSE
.. |Doc| image:: https://readthedocs.org/projects/med-to-csv/badge/?version=latest
   :target: https://med-to-csv.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. |DOI| image:: https://zenodo.org/badge/447657017.svg
   :target: https://zenodo.org/badge/latestdoi/447657017