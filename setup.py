import os
from setuptools import find_packages
from setuptools import setup

requires = [
    'pandas==0.22.0',
    'pyspark'
]

tests_requires = [
    'pytest',
    'pytest-spark'
]
setup(name='hallmarkfe',
      version='0.1s',
      description='Standardized feature specification and implementation', 
      url='https://github.com/pingali/hallmarkfe', 
      author='Venkata Pingali',
      author_email='pingali@scribbledata.io', 
      data_files = [("", ["LICENSE.txt"])],      
      install_requires=requires,
      tests_requires=tests_requires,
      packages=['hallmarkfe'],
      zip_safe=True,
      include_package_data=True,
      entry_points={
          'console_scripts': ['hfe=hallmarkfe.cli:main'],          
      },
)
