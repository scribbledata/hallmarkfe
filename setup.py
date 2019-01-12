# -*- coding: utf-8 -*-
"""setup.py"""

import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

class Tox(TestCommand):
    user_options = [('tox-args=', 'a', 'Arguments to pass to tox')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        import shlex
        if self.tox_args:
            errno = tox.cmdline(args=shlex.split(self.tox_args))
        else:
            errno = tox.cmdline(self.test_args)
        sys.exit(errno)


def read_content(filepath):
    with open(filepath) as fobj:
        return fobj.read()


classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
]


long_description = (
    read_content("README.rst") +
    read_content(os.path.join("docs/source", "CHANGELOG.rst")))

requires = [
    'setuptools',
    'pyspark',
    'click',
    'sphinx-click',
    'texttable',
    'itertoolz',
    'cytoolz',
    'pandas',
    'pytest-cov',
    'PyYAML',
    'coveralls'
]

tests_requires = [
    'pytest',
    'pytest-spark'
]
extras_require = {
    'reST': ['Sphinx'],
    }
if os.environ.get('READTHEDOCS', None):
    extras_require['reST'].append('recommonmark')

setup(name='hallmarkfe',
      version='0.1.0',
      description='Standardized feature specification and implementation',       
      long_description=long_description,
      author='Venkata Pingali',
      author_email='pingali@scribbledata.io',
      url='https://github.com/pingali/hallmarkfe',
      classifiers=classifiers,
      packages=['hallmarkfe'],
      data_files = [("", ["LICENSE.txt"])],            
      install_requires=requires,
      include_package_data=True,
      extras_require=extras_require,
      tests_require=['tox'],
      cmdclass={'test': Tox},
      entry_points={
          'console_scripts': ['hfe=hallmarkfe.cli:main'],          
      },      
)
