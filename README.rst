==============================
qrcgen - Qt QRC file generator
==============================

This Script generates a qrc file (Qt Resource file) for the entire contents of a directory tree.

:Authors: Hiroshi Miura, Flavio Codeco Coelho
:Version: 0.3
:Status: Alpha


Usage
=====

.. code-block::

    qrcgen.py [-h] [-o qrcfilename] [-e exclude [-e exclude]...] prefix directory [directory [directory] ...]


prefix
    The prefix in the qrc file under which the resources will be available.

directory
    A valid path, full or local. Can specify multiple directories.


This script take following options.

-o,--output    specify output qrc filename.
    If output option is not specified, a `<directory>.qrc` file or `resources.qrc` in the current directory
    will be generated when multiple directories are specified.
    File entries in generated qrc file are sorted in ascendent order.

-e,--exclude   specify patterns to exclude from qrc listing.

-h,--help  show this help message and exit


License
=======


Autogenerating a qrc file from the full contents of a directory tree

Copyright 2019 (C) Hiroshi Miura

Copyright 2011 (C) Flavio Codeco Coelho

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
