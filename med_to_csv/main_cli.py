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
import med_to_csv.path_verif as pv

def main() :
    """main function, calls expe_med_to_csv or file_med_to_csv depending on the path"""
    parser = argparse.ArgumentParser(prog="med_to_csv",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("path", type=str,
                        help="""Path to the group directory which contains data files from :
                                - Medassociate""")
    parser.add_argument("option", type=str, 
                        help= """Path to option config file.""")
    parser.add_argument("output", type=str,   
                        help= """Path output of the csv file""")
    # parser.add_argument("-v","--verbose", type=str, help= """Verbose mode""")
    args = parser.parse_args()
    
    #We test the presence of special characters:
    if not pv.test_ascii(args.option) :
        pv.print_error(args.option)
    elif not pv.test_ascii(args.output) :
        pv.print_error(args.option)
    elif not pv.test_ascii(args.path) :
        pv.print_error(args.path)

    if args.output is not None and args.output[-3:] != "csv":
        output_file = f"{args.output}.csv"
    else:
        output_file = args.output
    #load user parameters
    with open(args.option, "r") as ymlfile:
        opt_dic = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    parser = argparse.ArgumentParser(prog="med_to_csv",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    if ptah.isdir(args.path):
        # print(f"path={args.path}, notes={args.notes}, sortie={args.sortie}, echo={args.verbose}")
        expe_med.main(path=args.path, output_file = output_file, opt=opt_dic)
    else:
        df_res = file_med.read_path(args.path, opt_dic)
        df_res.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()
