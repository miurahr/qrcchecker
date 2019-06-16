"""
Autogenerating a qrc file from the full contents of a directory tree
Copyright 2019 Hiroshi Miura
Copyright 2011 by Flavio Codeco Coelho
licese: GPL v3
"""
import argparse
import os

import qrcgen


def is_valid_dir(parser, arg):
    """
    check if the path entered is a valid directory
    """
    if not os.path.isdir(arg):
        parser.error("%s is not a valid directory"%arg)
    return arg


def main():
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
    qrcfile = qrcgen.QrcFile(prefix)
    qrcfile.scan(directories, excludes)
    qrcfile.write(resfile)
    return 0


if __name__=="__main__":
    exit(main())
