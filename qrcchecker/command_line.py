"""
Autogenerating a qrc file from the full contents of a directory tree
Copyright 2019 Hiroshi Miura
Copyright 2011 by Flavio Codeco Coelho
licese: GPL v3
"""
import argparse
import os

from qrcchecker.qrcfile import Resources


def is_valid_dir(parser, arg):
    """
    check if the path entered is a valid directory
    """
    if not os.path.isdir(arg):
        parser.error("%s is not a valid directory" % arg)
    return arg


def main():
    parser = argparse.ArgumentParser(description='Generates a qrc (Qt resource file) on a directory tree.',
                                     epilog='A directory.qrc file will be generated in the current directory')
    parser.add_argument('qrcfile', help='qrc filename')
    parser.add_argument('directory', nargs='+', metavar='directory',
                        type=lambda x: is_valid_dir(parser, x),
                        help='A valid dir, full or relative.')
    parser.add_argument('-p', '--prefix', metavar='prefix', type=str,
                        help='The prefix in the qrc file under which the resources will be available.')
    parser.add_argument('-c', '--craete', action='store_true', help='create when not exist qrcfile')
    parser.add_argument('-e', '--exclude', action='append', metavar='exclude', type=str,
                        help='Pattern(s) to exclude')

    args = parser.parse_args()
    directories = args.directory  # should be a list of directory
    excludes = args.exclude  # should be a list of exclude expressions
    try:
        qt_resources = Resources(args.qrcfile, args.prefix, args.create).scan(directories, excludes)
        if args.create:
            qt_resources.write()
    except OSError:
        return(1)
    else:
        return(0)


if __name__ == "__main__":
    exit(main())
