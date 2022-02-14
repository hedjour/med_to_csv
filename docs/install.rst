Getting Started
================

To get a local copy up and running follow these simple steps

Requirements
-------------
* Python >= 3.6

Installation
-------------
Open a terminal and copy the following command lines.

#. Clone the repository

   .. code-block:: bash
      
      git clone https://sourcesup.renater.fr/anonscm/git/medanalysis/medanalysis.git

#. Install the required packages

   .. code-block:: bash

      pip install numpy argparse pyaml pandas
      pip install Gooey #For graphical interface

#. Install software
   
   .. code-block:: bash

      python setup.py install #On gnu-linux |MacOs Systems
      python setup.py install --user #On windows Sytems
or
   .. code-block:: bash
      
      pip install .
