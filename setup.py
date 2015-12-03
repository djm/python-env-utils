# -*- coding: utf-8 -*-
"""Setup file for env_utils."""
import os
from os.path import join, dirname, normpath, abspath
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(normpath(join(abspath(__file__), os.pardir)))

setup(
    name="env_utils",
    version="1.0.1",
    packages=['env_utils'],
    include_package_data=True,
    install_requires=[],
    license="MIT",
    description="Utility functions to make it easier to work with os.environ",
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    url='https://github.com/yunojuno/python-env-utils',
    author="Hugo Rodger-Brown",
    author_email='hugo@yunojuno.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
