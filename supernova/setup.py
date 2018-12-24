import os
from setuptools import find_packages
from setuptools import setup

requires = [
    'pandas==0.22.0'
]

tests_requires = [
    'pytest',
    'pytest-spark'
]
setup(name='hallmarkfe',
      version='0.1s',
      description='hallmarkfe package',
      url='https://github.com/pingali/hallmark', 
      author='Venkata Pingali',
      author_email='pingali@scribbledata.io', 
      license='None',
      install_requires=requires,
      tests_requires=tests_requires,
      packages=find_packages('src'),
      package_dir={'': 'src'},
      zip_safe=True,
      include_package_data=True,
      entry_points={
          'Contrib.asset': ['hallmarkfe=hallmarkfe'],
      },
)
