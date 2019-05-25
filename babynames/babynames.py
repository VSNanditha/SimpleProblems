#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
from collections import defaultdict

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    file = open(filename, 'r')

    regex_year = r'(Popularity in )(\d{4})'
    text = file.read()
    year = re.search(regex_year, text).group(2)

    regex_namerank = r'<td>(\d+)</td><td>([a-zA-Z]+)</td><td>([a-zA-z]+)</td>'
    nameranks = re.findall(regex_namerank, text)

    nameranks_dict = defaultdict(int)
    for tuple in nameranks:
        (rank, boy, girl) = tuple
        nameranks_dict[boy] = rank if nameranks_dict[boy] == 0 or rank < nameranks_dict[boy] else nameranks_dict[boy]
        nameranks_dict[girl] = rank if nameranks_dict[girl] == 0 or rank < nameranks_dict[girl] else nameranks_dict[girl]

    string = year + '\n' + '\n'.join(key + ' ' + nameranks_dict[key] for key in sorted(nameranks_dict.keys()))
    return string


def main():
    args = sys.argv[1:]
    if not args:
        print ('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    for file in args:
        extract = extract_names(file)
        if summary:
            summary_file = open(file + '.summary', 'w')
            summary_file.write(extract)
            summary_file.close()
        else:
            print(extract)


if __name__ == '__main__':
    main()
