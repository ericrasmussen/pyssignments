__version__ = '0.01'

import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

setup(name='pyssignments',
      version=__version__,
      description='homework homework homework',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        'Intended Audience :: Developers',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        ],
      tests_require=['pkginfo', 'nose'],
      install_requires=['nose'],
)
