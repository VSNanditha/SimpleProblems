#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Copy Special Python Exercise
# ----------------------------
#
# The Copy Special exercise goes with the file-system and external commands material in the Python Utilities section.
# This exercise is in the "copyspecial" directory within google-python-exercises (download google-python-exercises.zip
# if you have not already, see Set Up for details). Add your code in copyspecial.py.
#
# The copyspecial.py program takes one or more directories as its arguments. We'll say that a "special" file is one
# where the name contains the pattern __w__ somewhere, where the w is one or more word chars. The provided main()
# includes code to parse the command line arguments, but the rest is up to you. Write functions to implement the
# features below and modify main() to call your functions.
#
# Suggested functions for your solution(details below):
# * get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory
# * copy_to(paths, dir) given a list of paths, copies those files into the given directory
# * zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile
#
# Part A (manipulating file paths)
# --------------------------------
# Gather a list of the absolute paths of the special files in all the directories. In the simplest case, just print
# that list (here the "." after the command is a single argument indicating the current directory). Print one absolute
# path per line.
#
# $ ./copyspecial.py .
# /Users/nparlante/pycourse/day2/xyz__hello__.txt
# /Users/nparlante/pycourse/day2/zz__something__.jpg
#
# We'll assume that names are not repeated across the directories (optional: check that assumption and error out if
# it's violated).
#
# Part B (file copying)
# ---------------------
# If the "--todir dir" option is present at the start of the command line, do not print anything and instead copy the
# files to the given directory, creating it if necessary. Use the python module "shutil" for file copying.
#
# $ ./copyspecial.py --todir /tmp/fooby .
# $ ls /tmp/fooby
# xyz__hello__.txt        zz__something__.jpg
#
# Part C (calling an external program)
# ------------------------------------
# If the "--tozip zipfile" option is present at the start of the command line, run this command: "zip -j zipfile
# <list all the files>". This will create a zipfile containing the files. Just for fun/reassurance, also print the
# command line you are going to do first (as shown in lecture).
#
# $ ./copyspecial.py --tozip tmp.zip .
# Command I'm going to do:zip -j tmp.zip /Users/nparlante/pycourse/day2/xyz__hello__.txt
# /Users/nparlante/pycourse/day2/zz__something__.jpg
#
#
# If the child process exits with an error code, exit with an error code and print the command's output.
# Test this by trying to write a zip file to a directory that does not exist.

import sys
import re
import os
import shutil
import subprocess
import zipfile

"""Copy Special exercise
"""


def get_sherror(status):
    stat, message = status[0], status[1]
    if stat != 0:
        print(message)
        # exit(0)


def get_special_paths(dir):
    if os.path.exists(dir):
        pattern = r'[a-zA-Z0-9]+__\w+__'
        special_files = [file for file in os.listdir(dir) if re.match(pattern, file)]
        special_abs_paths = [os.path.abspath(file) for file in special_files]
        return special_abs_paths
    else:
        print('Directory path is invalid: ', dir)
        sys.exit(0)


def copy_to(paths, todir):
    if not os.path.exists(todir):
        os.mkdir(todir)
    for spl_file in paths:
        print('copying file', spl_file, 'to', todir)
        get_sherror(subprocess.getstatusoutput(shutil.copy(spl_file, todir)))
    sys.exit(0)


def zip_to(paths, zippath):
    if not os.path.exists(zippath):
        os.mkdir(zippath)
    for file in paths:
        print('zipping file', file, 'to', zippath)
        with zipfile.ZipFile(zippath + '/myzip.zip', 'a') as myzip:
            path, filename = os.path.split(file)
            myzip.write(filename)
            # get_sherror(subprocess.getstatusoutput(myzip.write(filename)))


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    for dir in args:
        special_files = get_special_paths(dir)

        if todir != '':
            copy_to(special_files, todir)

        if tozip != '':
            zip_to(special_files, tozip)


if __name__ == "__main__":
    main()
