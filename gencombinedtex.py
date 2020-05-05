#!/usr/bin/python

import re
import sys

def replace_input_clause_in_tex_file(tex_file_path):
    file_content = get_file_content(tex_file_path)
    p = re.compile('input\s*{(.*)\s*}\s*\\n')
    imported_file_names = p.findall(file_content)
    while len(imported_file_names) > 0:
    
        for imported_file_name in imported_file_names:
            imported_file_content = replace_input_clause_in_tex_file(imported_file_name + '.tex')
            replaced_string = '\\input{' + imported_file_name + '}'
            file_content = file_content.replace(replaced_string, imported_file_content)

        imported_file_names = p.findall(file_content)
    return file_content

def get_file_content(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        return data

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You have to pass the main latex file as a parameter. E.x: python gencombinetex.py main.tex")
        exit(1)
    latex_main_file = sys.argv[1]
    file_content = replace_input_clause_in_tex_file(latex_main_file)
    with open('main_all_in_one.tex', 'w') as file:
        file.write(file_content)

    print('Done successfully')
