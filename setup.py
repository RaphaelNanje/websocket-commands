import re
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import and use built-in open()
from io import open as io_open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))


def readall(*args):
    with io_open(path.join(here, *args), encoding="utf-8") as fp:
        return fp.read()


metadata = dict(
    re.findall(r"""__([a-z]+)__ = "([^"]+)""", readall("websocket_commands", "__init__.py"))
)
setup(
    name='websocket-commands',
    version=metadata['version'],
    packages=['websocket_commands'],
    url='http://github.com/en-lofty/websocket-commands.git',
    license='',
    author='raphael',
    author_email='rtnanje@gmail.com',
    description='A library that makes communicating between frontend and backend websockets simple.',
    install_requires=['']
)
