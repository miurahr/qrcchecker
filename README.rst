=================================
qrc-checker - Qt QRC file checker
=================================


.. image:: https://travis-ci.org/miurahr/qrcchecker.svg?branch=master
    :target: https://travis-ci.org/miurahr/qrcchecker

.. image:: https://coveralls.io/repos/github/miurahr/qrcchecker/badge.svg
   :target: https://coveralls.io/github/miurahr/qrcchecker


This Script generates a qrc file (Qt Resource file) for the entire contents of a directory tree.


:Authors: Hiroshi Miura, Flavio Codeco Coelho
:Version: 0.3
:Status: Alpha


Usage
=====

.. code-block::

    qrcchecker [-h][-c][-u][-e exclude [-e exclude]...] qrcfilename directory [directory [directory] ...]


qrcfilename
    qrc filename to check.

directory
    A valid path, full or local. Can specify multiple directories.


This script take following options.

-e,--exclude   specify patterns to exclude from qrc listing.

-c,--create    create qrc file if not exist(Default: False).

-u,--update    update qrc file with suggested items(implies --create, Default: False).

-h,--help      show this help message and exit


License
=======

Check a qrc file with a directory tree.

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
