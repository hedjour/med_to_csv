.. role:: raw-html(raw)
   :format: html

   
|Contributors| |Forks| |Stargazers| |Issues| |MIT License|

.. raw:: html

   <div id="top"></div>
   <h3 align="center">MedAssociates to CSV file</h3>

     <p align="center">
       A simple way to parse MedAssociate output file in tidy data :
       <ul>
         <li> 1 row = 1 observation
         <li> 1 col = 1 var
       </ul>
       <br />
       <a href="https://github.com/hedjour/med_to_csv"><strong>Explore the docs »</strong></a>
       <br />
       <br />
       <a href="https://github.com/hedjour/med_to_csv">View Demo</a>
       ·
       <a href="https://github.com/hedjour/med_to_csv/issues">Report Bug</a>
       ·
       <a href="https://github.com/hedjour/med_to_csv/issues">Request Feature</a>
     </p>
   </div>


:raw-html:`<!-- TABLE OF CONTENTS -->`


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


:raw-html:`<!-- ABOUT THE PROJECT -->`

About The Project
-----------------

This program parses MedAssociates data files and transforms them into tidy csv files, containing the information needed and given by each user


.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


Built With
^^^^^^^^^^


* `Python 3 <https://www.python.org/>`_
* `Gooey <https://github.com/chriskiehl/Gooey>`_


.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


:raw-html:`<!-- GETTING STARTED -->`

Getting Started
---------------

To get a local copy up and running follow these simple steps.

Prerequisites
^^^^^^^^^^^^^

This is an example of how to list things you need to use the software and how to install them.

* pip

   .. code-block:: bash

      pip install numpy argparse yaml pandas
      pip install Gooey #For graphical interface

Installation
^^^^^^^^^^^^


#. Clone the repo

   .. code-block:: bash
      
      git clone https://sourcesup.renater.fr/anonscm/git/medanalysis/medanalysis.git

#. Install the required packages

   .. code-block:: bash

      pip install numpy argparse yaml pandas
      pip install Gooey #For graphical interface


.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


:raw-html:`<!-- USAGE EXAMPLES -->`

Usage
-----

Graphical User Interface
^^^^^^^^^^^^^^^^^^^^^^^^

Run the application and follow the steps on the interface

.. code-block:: sh

       ./main_gui

Command Line Interface
^^^^^^^^^^^^^^^^^^^^^^

Runs on the experiment directory that contains the directories containing the raw data files or on the file itself and returns a csv file 

.. code-block:: sh

       ./main_cli.py path_to_medassociate_file config_file.yml output_csv_file

Config file
^^^^^^^^^^^

The config file is a necessary file that gives the setup of your data to the soft.
You can find as an example the config.yml which contains all possibilities of setup.
You can mixe 1 col file dir and labelled dir file in experiment dir.


#. 
   There are three types of parameters:


   * info_col : One column file
   * info_lab : labelled file
   * options : further options

#. 
   For the first two types of parameters.
    You need to indicate the information in this format: "Key : Value"


   * Keys are the column names that you want in the output file
   * Values are:

     * for infos_col: row number - 1 (Start index :0)
     * for infos_lab: letters used in medAssociate exercise
     * for infos_opt: (see next point)

#. 
   Options:


   * remove_zero_ending : True or False to keep or remove Zeros at the end of arrays
   * Cut : for cutting an output on a special character usually a dot into 2 columns. The value must be a list of list of 4 elements :

     * key to cut
     * separator usually the dot character
     * Col names of first sub-element
     * Col names of second sub-element

   * Eval : for some columns the values must be the result of a Python command line (e.g to get information in a path). It's necessarly a python dictionary with Key as column name and value a short command line as a string.

#. 
   The following Keys are med associate keywords only usable with labelled file :


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


:raw-html:`<!-- ROADMAP -->`

Roadmap
-------


* Add possibility for labelled file to not precise the yml file and use yml in param path whith same
  names of MPC name get from MSN []
* Add a GUI  [x]
* Add possibility of filtering directories [x]
* Add CLI usage [x]
* Made an easy installable version for Mac | Windows | Gnu-Linux [x]


.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


:raw-html:`<!-- CONTRIBUTING -->`

Contributing
------------

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!


#. Fork the Project
#. Create your Feature Branch (\ ``git checkout -b feature/AmazingFeature``\ )
#. Commit your Changes (\ ``git commit -m 'Add some AmazingFeature'``\ )
#. Push to the Branch (\ ``git push origin feature/AmazingFeature``\ )
#. Open a Pull Request


.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


:raw-html:`<!-- LICENSE -->`

License
-------

Distributed under the xxx License. See ``LICENSE.txt`` for more information.


.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


:raw-html:`<!-- CONTACT -->`

Contact
-------


* Jean-Emmanuel Longueville - jean.emmanuel.longueville@univ-poitiers.fr
* Myriam Hanna - myriam.hanna@univ-poitiers.fr
* Marcello Solinas

Project Link: `https://github.com/hedjour/med_to_csv <https://github.com/hedjour/med_to_csv>`_


.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


:raw-html:`<!-- ACKNOWLEDGMENTS -->`

Acknowledgments
---------------


* ` <>`_
* ` <>`_
* ` <>`_


.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


:raw-html:`<!-- MARKDOWN LINKS & IMAGES -->`
:raw-html:`<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->`

.. |Contributors| image:: https://img.shields.io/github/contributors/hedjour/med_to_csv.svg?style=for-the-badge
   :target: https://github.com/hedjour/med_to_csv/graphs/contributors
.. |Forks| image:: https://img.shields.io/github/forks/hedjour/med_to_csv.svg?style=for-the-badge
   :target: https://github.com/hedjour/med_to_csv/network/members
.. |Stargazers| image:: https://img.shields.io/github/stars/hedjour/med_to_csv.svg?style=for-the-badge
   :target: https://github.com/hedjour/med_to_csv/stargazers
.. |Issues| image:: https://img.shields.io/github/issues/hedjour/med_to_csv.svg?style=for-the-badge
   :target: https://github.com/hedjour/med_to_csv/issues
.. |MIT License| image:: https://img.shields.io/github/license/hedjour/med_to_csv.svg?style=for-the-badge
   :target: https://github.com/hedjour/med_to_csv/blob/master/LICENSE.txt