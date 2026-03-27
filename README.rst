.. role:: raw-html(raw)
   :format: html

|Contributors| |Forks| |Stargazers| |Issues| |GPLv3.0 License| |Doc| |DOI|

.. _top:

.. image:: /docs/img/intro_light.png
   :class: only-light
.. image:: /docs/img/intro_dark.png
   :class: only-dark

MedAssociates to CSV file
==========================

A simple way to parse MedAssociate output file in tidy data :

* 1 row = 1 observation
* 1 col = 1 var

`Explore the docs » <https://med-to-csv.readthedocs.io/>`_

`View Demo <https://github.com/hedjour/med_to_csv>`_ ·
`Report Bug <https://github.com/hedjour/med_to_csv/issues>`_ ·
`Request Feature <https://github.com/hedjour/med_to_csv/issues>`_

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
           <li><a href="#make-executable">Make Executable</a></li>
         </ul>
       </li>
       <li>
         <a href="#usage">Usage</a>
         <ul>
           <li><a href="#Graphical-User-Interface">Graphical User Interface</a></li>
           <li><a href="#Command-Line-Interface">Command Line Interface</a></li>
           <li><a href="#config-file">Config file</a></li>
         </ul>
       </li>
       <li><a href="#roadmap">Roadmap</a></li>
       <li><a href="#contributing">Contributing</a></li>
       <li><a href="#license">License</a></li>
       <li><a href="#contact">Contact</a></li>
       <li><a href="#acknowledgements">Acknowledgements</a></li>
     </ol>
   </details>


About The Project
-----------------

This program parses MedAssociates data files and transforms them into tidy csv files,
containing the information selected by the user.

.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


Built With
^^^^^^^^^^

* `Python 3 <https://www.python.org/>`_
* `Gooey <https://github.com/chriskiehl/Gooey>`_

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
      pip install Gooey  # For graphical interface

Installation
^^^^^^^^^^^^

#. Clone the repository

   .. code-block:: bash

      git clone https://sourcesup.renater.fr/anonscm/git/medanalysis/medanalysis.git

#. Install the required packages

   .. code-block:: bash

      pip install numpy argparse yaml pandas
      pip install Gooey  # For graphical interface
      cd path/to/directory_of_git_clone

#. Then run one of the two lines below:

   .. code-block:: bash

      python setup.py install
      python setup.py install --user  # For windows users

   Or:

   .. code-block:: bash

      pip install .

Installation on Linux — other method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prerequisites:

- A Linux system with ``sudo`` privileges
- The latest release of ``med_to_csv`` downloaded from the `Releases <https://github.com/hedjour/med_to_csv/releases>`_ page

Steps
"""""

1. **Make the executable file runnable:**

   Open a terminal and navigate to your Downloads folder. Run the following command:

   .. code-block:: bash

      chmod +x ~/Downloads/portable_med_to_csv_gui_linux

2. **Move the executable to** ``/usr/local/bin``:

   .. code-block:: bash

      sudo mv ~/Downloads/portable_med_to_csv_gui_linux /usr/local/bin/

3. **Download and set up the application icon:**

   Download the ``config_icon.png`` file from the
   `source <https://github.com/hedjour/med_to_csv/blob/main/med_to_csv/img/config_icon.png?raw=true>`_
   and run:

   .. code-block:: bash

      sudo mv config_icon.png /usr/share/icons/med_to_csv_icon.png

4. **Create a desktop entry:**

   .. code-block:: bash

      sudo bash -c 'cat > /usr/share/applications/med_to_csv.desktop' << 'EOF'
      [Desktop Entry]
      Type=Application
      Name=med_to_csv
      Comment=Data Processing and Wrangling in Python
      Icon=/usr/share/icons/med_to_csv_icon.png
      Exec=/usr/local/bin/portable_med_to_csv_gui_linux
      Terminal=false
      StartupNotify=false
      Categories=Science;MedicalSoftware;X-DataProcessing;
      StartupWMClass=python
      EOF

5. **Set the correct permissions for the desktop file:**

   .. code-block:: bash

      sudo chmod 644 /usr/share/applications/med_to_csv.desktop

.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>

Make Executable (Portable)
^^^^^^^^^^^^^^^^^^^^^^^^^^

To make a GUI onefile executable, run these commands in terminal:

.. code-block:: bash

   cd path/to/directory_of_git_clone
   pyinstaller build_gui.spec

To make a CLI onefile executable, run these commands in terminal:

.. code-block:: bash

   cd path/to/directory_of_git_clone
   pyinstaller build_cli.spec

Data Organisation
-----------------

The file is just an output of MedAssociate software.
The path directory can contain sub-directories of sessions that contain
the raw data files, or just MedAssociate files directly.

.. warning::

   Your raw data directories must only contain MedAssociate output files.

Example of data organisation for batch run
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   ::

      Experiment directory/
      ├── dir 01/
      │   ├── file_med_associates_to_compil
      │   ├── file_med_associates_to_compil
      │   └── file_med_associates_to_compil
      └── dir 02/
          ├── file_med_associates_to_compil
          ├── file_med_associates_to_compil
          └── file_med_associates_to_compil

   Or:

   ::

      Experiment directory/
      ├── file_med_associates_to_compil
      ├── file_med_associates_to_compil
      └── file_med_associates_to_compil


Example
-------

Graphical User Interface
^^^^^^^^^^^^^^^^^^^^^^^^

Run the application and follow the steps on the interface:

.. code-block:: bash

   ./main_gui

Command Line Interface
^^^^^^^^^^^^^^^^^^^^^^

The software runs on the experiment directory that contains the directories containing
the raw data files, or on the file itself, and returns a CSV file:

.. code-block:: bash

   ./main_cli.py path_to_medassociate_file config_file.yml output_csv_file

.. warning::

   Your path must contain only ASCII characters (no accented characters such as: éèàï).

Config file
^^^^^^^^^^^

The config file is a necessary file that specifies the setup of your data to the software.
You can find an example in the ``config.yml`` file which contains all possibilities of setup.
You can mix 1-column file directories and annotated directory files in the experiment directory.

#. There are three types of parameters:

   * ``info_col`` : One column file
   * ``info_lab`` : Annotated file
   * ``options`` : Further options

#. For the first two types of parameters, indicate the information in this format: ``Key : Value``

   * Keys are the column names that you want in the output file.
   * Values are:

     * for ``infos_col``: row number - 1 (start index: 0)
     * for ``infos_lab``: letters used in the MedAssociate exercise
     * for ``infos_opt``: see next point

#. Options:

   * ``remove_zero_ending`` : ``True`` or ``False`` to keep or remove zeros at the end of arrays.
   * ``Cut`` : for cutting an output on a special character (usually a dot) into 2 columns.
      The value must be a list of lists of 4 elements:

        * key to cut
        * separator (usually the dot character)
        * column name of the first sub-element
        * column name of the second sub-element

      * ``Eval`` : for some columns whose values must be the result of a Python command
      (e.g. to get information from a path). Must be a Python dictionary with the key as
      column name and the value as a short command string.

#. The following keys are MedAssociate keywords, only usable with annotated files:

   * Start Date (automatically added)
   * End Date
   * Subject
   * Experiment
   * Group
   * Box
   * Start Time (automatically added)
   * End Time
   * MSN: MedAssociate exercise names

.. note::

   Templates are available in the ``config.yml`` file.

.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>


Roadmap
-------

* Add possibility for annotated file to not specify the YAML file and use YAML in parameter
  path with the same names as MPC names obtained from MSN.

.. raw:: html

   <p align="right">(<a href="#top">back to top</a>)</p>

FAQ
---

If you get the following error:

.. code-block:: python

   A problem has occurred while processing the data: local variable 'lab_folder' referenced before assignment

Have you filled your sub-directories with MedAssociates output files?

Contributing
------------

Contributions are what make the open-source community such an amazing place to learn, inspire,
and create. Any contributions you make are **greatly appreciated**.

If you have any suggestion that would improve this software, please fork the repository and
create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

#. Fork the Project
#. Create your Feature Branch (``git checkout -b feature/AmazingFeature``)
#. Commit your Changes (``git commit -m 'Add some AmazingFeature'``)
#. Push to the Branch (``git push origin feature/AmazingFeature``)
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
* Thanks to our old contributors: Ekter, Myriam Hanna.

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