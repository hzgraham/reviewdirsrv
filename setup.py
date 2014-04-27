#!/usr/bin/env python
import os
import sys

from distutils.core import setup

setup(
    name='ReviewDirsrv',
    version='0.1dev',
#    package_dir={ 'reviewdirsrv' },
    packages=['reviewdirsrv',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
    scripts=[
        'bin/analyzedirsrv'
        ]
)

