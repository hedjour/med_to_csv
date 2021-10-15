try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name = "med_tocsv",
    version = "1.0",
    author = "Jean-Emmanuel Longueville, Myriam Hanna",
    author_email = "jean.emmanuel.longueville(@)univ-poitiers.fr",
    description = "A module that converts MedAssociates data to csv files",
    license = "",
    url = "https://sourcesup.renater.fr/anonscm/git/medanalysis/medanalysis.git",
    packages= find_packages(),
    install_requires=['pandas',
                      'numpy',
                      'argparse',
                      'pyaml',
                      'gooey',],
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: ",
    ],
    entry_points={
        'console_scripts':  ['med_to_csv-cli = med_to_csv.main_cli:main',
                             'med_to_csv-gui = med_to_csv.main_gui:main',]
        },
    data_files=[
        ('lib/python3.9/dist-packages/med_to_csv/img',
            ['med_to_csv/img/config_icon.png','med_to_csv/img/program_icon.png' ])
        ],
)