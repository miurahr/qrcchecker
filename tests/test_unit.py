import os

from qrcgen.qrcgen import Resources

current_path = os.path.dirname(__file__)


def test_default():
    os.chdir(current_path)
    targets = ["resources"]
    res = Resources("prefix")
    res.scan(targets, None)
    for f in res.resources:
        assert f in [ 'resources/res.ini', 'resources/example.ico', 'resources/gen.py']
        assert f not in ['resources/exmaple.cpp']


def test_exclude_py():
    os.chdir(current_path)
    targets = ["resources"]
    exclude = ["gen.py", "example.cpp"]
    res = Resources("prefix")
    res.scan(targets, exclude)
    for f in res.resources:
        assert f in [ 'resources/res.ini', 'resources/example.ico']
        assert f not in ['resources/gen.py', 'resources/exmaple.cpp']
