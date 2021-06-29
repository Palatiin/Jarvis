# 28.6.2021
# returns list of valid modules

import os
import re

## Static analysis of module source code
#  all specifics that have to be met are specified in comment of class Module
# @param module name of module source file (module.py)
# @return Logical value, whether module's structure is valid
def validate_module(module: str) -> bool:
    # TODO
    pass


## Loads module-like source files
# @param directory where modules are stored
# @return list of valid modules
def load_modules(directory: str = "modules/") -> list:
    suffix_pattern = re.compile(".*\.\w+$")
    dir_modules = os.listdir("./"+directory)
    valid_modules = []

    # first check: only files ending with .py are allowed
    for dirname in dir_modules:
         # skipping files that do not meet structure
        if re.search(suffix_pattern, dirname): 
            continue

        module_files = os.listdir("./"+directory+dirname):
        module_source = dirname + ".py"
        
        # skipping modules that do not have source file with the same name as it's directory
        if module_source not in module_files: 
            continue

        # TODO

    print(valid_modules)
    
