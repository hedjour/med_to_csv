#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Main module to run the right script with the given options
"""

import argparse
from os import path as ptah
import yaml
import med_project.expe_med_to_csv as expe
import med_project.file_med_to_csv as file
from gooey import Gooey, GooeyParser
BOOM = r"""
     _.-^^---....,,--
 _--                  --_
<                        >
|                        |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :|
______.,-#%&$@%#&#~,._____
    KAA-BOOOOOOM -
Oups your data have desapear
    OH  good new 
You miss to give me your data
"""

@Gooey( program_name= "med_to_csv",
        image_dir=f'{ptah.dirname(ptah.realpath(__file__))}/img/',
        monospace_display=True,
        default_size=(900,650),
        header_show_title = False,
        header_height=100,
        menu=[{
            'name': 'Help',
            'items': [{
                    'type': 'Link',
                    'menuTitle': 'Documentation',
                    'url': 'https://www.readthedocs.com/foo'
                },{
                    'type': 'AboutDialog',
                    'menuTitle': 'About',
                    'name': 'med_to_csv',
                    'description': 'MedAssociate output file to CSV file',
                    'version': '1.0.0',
                    'copyright': '2021',
                    'website': 'https://github.com/hedjour/',
                    'developer': """
                                    * JE Longueville,
                                    * M. Hanna,
                                    * N. Mulac,
                                    * M. Solinas""",
                    'license': 'Cecill' #Add the texte of the license
                }]
        }]
    )
def main() :
    """main function, to display a select file/directory window"""
    parser = GooeyParser(prog="med_to_csv", 
                         formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                         description = """This software wrangling your data to a unique csv file.
                         
For more information about the config file please see the README or documentation.
You must to indicate a path or a file with your data in other case the software will return an error.
""")
    parser.add_argument("option", type=str, 
                        help= """Path to option config file.""", widget="FileChooser")
    parser.add_argument("output", type=str,   
                        help= """Path output of the csv file""", widget="FileSaver")
    parser.add_argument("-p","--path", type=str,
                        help="""
Option to indicate a path to the group directory which contains data files from : Medassociate
                        """, widget="DirChooser")
    parser.add_argument("-f", "--file", type=str,
                        help="""Option to indicate a unique file and not a directory.""",
                        widget="FileChooser", 
                        gooey_options={ 'validator': {
                            'test': 'user_input is None and args.path is None',
                            'message': 'Choose a file or a directory'
                            } })
    # parser.add_argument("-v","--verbose", type=str, help= """Verbose mode""")

    args = parser.parse_args()
    #load user parameters
    with open(args.option, "r") as ymlfile:
        opt_dic = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    parser = argparse.ArgumentParser(prog="med_to_csv",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    if args.file is not None:
        df_res = file.read_path(args.path, opt_dic)
        df_res.to_csv(args.file, index=False)
    elif args.path is not None :
        expe.main(path=args.path, output_file = args.output, opt=opt_dic)
    else:
        raise Exception(BOOM)

if __name__ == "__main__":
    main()
