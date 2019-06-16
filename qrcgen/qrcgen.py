#!/usr/bin/env python
"""
Autogenerating a qrc file from the full contents of a directory tree
Copyright 2019, Hiroshi Miura
Copyright 2011, Flavio Codeco Coelho
licese: GPL v3
"""

import bisect
import fnmatch
import os
import re


class Resources():

    def __init__(self, prefix):
        self.prefix = prefix
        self.resources = []

    def scan(self, directories, exclude_pattern):
        """
        Scan tree starting from directories and generate sorted resources
        """
        if not isinstance(directories, list):
            raise TypeError
        if exclude_pattern is not None:
            if not isinstance(exclude_pattern, list):
                raise TypeError
        excludes = exclude_pattern or ['*.cpp', '*.hpp', '*.c', '*.h']
        excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'
        for direc in directories:
            for path, dirs, files in os.walk(direc):
                files = [(os.path.join(path, f), f) for f in files]
                for p, f in files:
                    if not re.match(excludes, p) and not re.match(excludes, f):
                        e = os.path.relpath(p)
                        bisect.insort(self.resources, e)

    def write(self, qrcfile):
        """
        Write to the qrc file under the prefix specified
        """
        with open(qrcfile, 'w') as f:
            f.write('<RCC>\n    <qresource prefix="%s">\n' % self.prefix)
            for r in self.resources:
                f.write('        <file>%s</file>\n' % r)
            f.write('    </qresource>\n</RCC>\n')
