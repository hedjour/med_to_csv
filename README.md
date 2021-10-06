<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


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



<!-- TABLE OF CONTENTS -->
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


<!-- ABOUT THE PROJECT -->
## About The Project
This program parses MedAssociates data files and transforms them into tidy csv files, containing the information needed and given by each user


<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python 3](https://www.python.org/)
* [Gooey](https://github.com/chriskiehl/Gooey)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* pip
  ```sh
      pip install numpy argparse yaml pandas
      pip install Gooey #For graphical interface
  ```

### Installation

1. Clone the repo
   ```sh
      git clone https://sourcesup.renater.fr/anonscm/git/medanalysis/medanalysis.git
   ```
2. Install the required pip packages
   ```sh
      pip install numpy argparse yaml pandas
      pip install Gooey #For graphical interface
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Graphical User Interface
Run the application and follow the steps on the interface
  ```sh
    ./main_gui
  ```
### Command Line Interface
Runs on the experiment directory that contains the directories containing the raw data files or on the file itself and returns a csv file 
  ```sh
    ./main_cli.py path_to_medassociate_file config_file.yml output_csv_file
  ```


### Config file

The config file is a necessary file that gives the setup of your data to the soft.
You can find as an example the config.yml which contains all possibilities of setup.
You can mixe 1 col file dir and labelled dir file in experiment dir.

1. There are three types of parameters:
    * info_col : One column file
    * info_lab : labelled file
    * options : further options

2. For the first two types of parameters.
    You need to indicate the information in this format: "Key : Value"
    * Keys are the column names that you want in the output file
    * Values are:
      * for infos_col: row number - 1 (Start index :0)
      * for infos_lab: letters used in medAssociate exercise
      * for infos_opt: (see next point)

3. Options:
    * remove_zero_ending : True or False to keep or remove Zeros at the end of arrays
    * Cut : for cutting an output on a special character usually a dot into 2 columns. The value must be a list of list of 4 elements :
      * key to cut
      * separator usually the dot character
      * Col names of first sub-element
      * Col names of second sub-element
    * Eval : for some columns the values must be the result of a Python command line (e.g to get information in a path). It's necessarly a python dictionary with Key as column name and value a short command line as a string.

4. The following Keys are med associate keywords only usable with labelled file :
    * Start Date (automatically added)
    * End Date
    * Subject
    * Experiment
    * Group
    * Box
    * Start Time (automatically added)
    * End Time
    * MSN: Medassociate exercice names

Note: Templates are available in the config.yml file

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

* Add possibility for labelled file to not precise the yml file and use yml in param path whith same
 names of MPC name get from MSN []
* Add a GUI  [x]
* Add possibility of filtering directories [x]
* Add CLI usage [x]
* Made an easy installable version for Mac | Windows | Gnu-Linux [x]

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the xxx License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

* Jean-Emmanuel Longueville - jean.emmanuel.longueville@univ-poitiers.fr
* Myriam Hanna - myriam.hanna@univ-poitiers.fr
* Marcello Solinas

Project Link: [https://github.com/hedjour/med_to_csv](https://github.com/hedjour/med_to_csv)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/hedjour/med_to_csv.svg?style=for-the-badge
[contributors-url]: https://github.com/hedjour/med_to_csv/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hedjour/med_to_csv.svg?style=for-the-badge
[forks-url]: https://github.com/hedjour/med_to_csv/network/members
[stars-shield]: https://img.shields.io/github/stars/hedjour/med_to_csv.svg?style=for-the-badge
[stars-url]: https://github.com/hedjour/med_to_csv/stargazers
[issues-shield]: https://img.shields.io/github/issues/hedjour/med_to_csv.svg?style=for-the-badge
[issues-url]: https://github.com/hedjour/med_to_csv/issues
[license-shield]: https://img.shields.io/github/license/hedjour/med_to_csv.svg?style=for-the-badge
[license-url]: https://github.com/hedjour/med_to_csv/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
