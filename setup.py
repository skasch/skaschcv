#!/usr/bin/env python
# encoding: utf-8
"""
setup.py

Created by Romain Mondon-Cancel on 2018-01-18.
"""
from setuptools import setup

setup(
    name='skaschcv',
    packages=['skaschcv'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
