#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse
import glob

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def from_dir():
    special_files = glob.glob("*.txt")
    special_files += glob.glob("*.jpg")
    for spec in special_files:
        print os.path.abspath(spec)


def to_dir(dir):
    special_files = glob.glob("*.txt")
    special_files += glob.glob("*.jpg")
    if os.path.exists(dir):
        for spec in special_files:
            shutil.copy(spec, dir)
    else:
        os.makedirs(dir)
        for spec in special_files:
            shutil.copy(spec, dir)

def to_zip(zip_location):
    special_files = glob.glob("*.txt")
    special_files += glob.glob("*.jpg")
    paths = []
    for spec in special_files:
        paths.append(os.path.abspath(spec))
    cmd = "zip -j {0} {1}".format(str(zip_location), " ".join(paths))
    os.system(cmd)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', action="store_true", help='dest dir for special files')
    parser.add_argument('--tozip', action="store_true", help='dest zipfile for special files')
    parser.add_argument('dir', type=str)
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()
    directory = args.dir
    if args.todir:
        to_dir(directory)
    elif args.tozip:
        to_zip(directory)
    elif directory == '.':
        from_dir()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about 
    # how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
  
if __name__ == "__main__":
    main()
