#!/usr/bin/env python
# _commit.py <filename>
import sys
import time
import os
from subprocess import check_output
import datetime


def main(filename):
    if filename.startswith('./'):
        filename = filename[2:]
    if filename.startswith('_'):
        return
    fdt = os.path.getctime(filename)
    fdt = datetime.datetime.fromtimestamp(fdt)
    cmd = 'git status --porcelain {}'.format(filename)
    r = check_output(cmd, shell=True).strip()
    cmd = 'git add {0}'.format(filename)
    r = check_output(cmd, shell=True).strip()
    cmd = 'git commit -m "Add/update {0}" --date \'{1}\' {0}'.format(filename, fdt)
    r = check_output(cmd, shell=True).strip()
    print 'commited', r
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
