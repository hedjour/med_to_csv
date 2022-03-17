#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Add on module to have some code to evitate repetition
"""

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

def print_error(var:str):
    try:
        raise SyntaxError(f"""This path contains some special characters like (éàèïë) :\n {var}""")
    except SyntaxError as e:
        print(e.args)
        
#test_ascii = lambda ele: len(ele) == len(ele.encode())
def test_ascii (ele):
    return len(ele) == len(ele.encode()) 