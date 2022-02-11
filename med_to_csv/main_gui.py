#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Main module to run the right script with the given options
"""

import argparse
from os import path as ptah
import yaml
import med_to_csv.expe_med_to_csv as expe_med
import med_to_csv.file_med_to_csv as file_med
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
Oops your data have disappeared
    OH  good news 
You forgot to give me your data
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
                         description = """This software converts med associates data files into a unique csv file.
                         
For more information about the config file please check the README or documentation.
You must indicate a path or a file with your data otherwise the software will return an error.
""")
    parser.add_argument("option", type=str, 
                        help= """Path to option config file.""", widget="FileChooser")
    parser.add_argument("output", type=str,   
                        help= """Path output of the csv file""", widget="FileSaver")
    parser.add_argument("-p","--path", type=str,
                        help="""
Option to indicate a path to the group directory which contains data files from : Medassociates
                        """, widget="DirChooser")
    parser.add_argument("-f", "--file", type=str,
                        help="""Option to indicate a unique file and not a directory.""",
                        widget="FileChooser", 
                        # gooey_options={ 'validator': {
                        #     'test': 'user_input is None and args.path is None',
                        #     'message': 'Choose a file or a directory'
                        #     } }
                        )
    # parser.add_argument("-v","--verbose", type=str, help= """Verbose mode""")

    args = parser.parse_args()
    #load user parameters
    with open(args.option, "r") as ymlfile:
        opt_dic = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    parser = argparse.ArgumentParser(prog="med_to_csv",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    print(f"File : {args.file} | Path :{args.path}")
    if args.output is not None and args.output[-3:] != "csv":
        output_file = f"{args.output}.csv"
    else:
        output_file = args.output
    if args.file is not None:
        print("arg.file")
        df_res = file_med.read_path(args.file, opt_dic)
        df_res.to_csv(output_file, index=False)
    elif args.path is not None :
        print("arg.ptah")
        expe_med.main(path=args.path, output_file = output_file, opt=opt_dic)
    else:
        raise Exception(BOOM)

if __name__ == "__main__":
    main()
