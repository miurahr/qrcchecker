#!/usr/bin/env python
"""
Autogenerating a qrc file from the full contents of a directory tree
Copyright 2019 Hiroshi Miura
Copyright 2011 by Flavio Codeco Coelho
licese: GPL v3
"""

import argparse
import bisect
import fnmatch
import os
import re


class QrcFile():

    def __init__(self, prefix):
        self.prefix = prefix
        self.resources = []

    def scan(self, directories, exclude_pattern):
        """
        Scan tree starting from directories
        """
        excludes = exclude_pattern or ['.+\.cpp', '.+\.hpp', '.+.c', '.+\.h', '\..+']
        excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'

        for direc in directories:
            for path, dirs, files in os.walk(direc):
                files = [os.path.join(path, f) for f in files]
                for f in files:
                    if not re.match(excludes, f):
                        bisect.insort(self.resources, f)

    def write(self, qrcfile):
        """
        Write to the qrc file under the prefix specified
        """
        with open(qrcfile, 'w') as f:
            f.write('<RCC>\n    <qresource prefix="%s">\n'%self.prefix)
            for r in self.resources:
                f.write('        <file>%s</file>\n'%r)
            f.write('    </qresource>\n</RCC>\n')


def is_valid_dir(parser, arg):
    """
    check if the path entered is a valid directory
    """
    if not os.path.isdir(arg):
        parser.error("%s is not a valid directory"%arg)
    return arg


def run():
    parser = argparse.ArgumentParser(description='Generates a qrc (Qt resource file) on a directory tree.',
                                     epilog='A directory.qrc file will be generated in the current directory')
    parser.add_argument('prefix', metavar='prefix', type=str,
                        help='The prefix in the qrc file under which the resources will be available.')
    parser.add_argument('directory', nargs='+', metavar='directory',
                        type=lambda x: is_valid_dir(parser, x),
                        help='A valid dir, full or relative.')
    parser.add_argument('-e','--exclude', action='append',metavar='exclude', type=str,
                        help='Pattern(s) to exclude' )
    parser.add_argument('-o', '--output', help='output qrc filename')

    args = parser.parse_args()
    prefix = args.prefix or '/'
    directories = args.directory
    excludes = args.exclude
    if args.output is not None:
        resfile = args.output
    elif len(directories) == 1:
        resfile = os.path.split(directories[0])[-1]
    else:
        resfile = 'resources.qrc'
    qrcfile = QrcFile(prefix)
    qrcfile.scan(directories, excludes)
    qrcfile.write(resfile)
    return 0


if __name__=="__main__":
    exit(run())
