#!/usr/bin/env python3
from setuptools import setup

setup(
    name='antennasim',
    version='0.0',
    author='Steve Burns',
    author_email='smburns47@gmail.com',
    url='https://github.com/stevenmburns/antennasim/',
    license='BSD-3-Clause',
    packages=['antennasim'],
    python_requires='>=3.10',
    install_requires=[
        'numpy',
        'scipy',
        'pytest',
    ],
)
