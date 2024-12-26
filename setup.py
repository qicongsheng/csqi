#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: qicongsheng
from setuptools import setup, find_packages
from pyutils import help

setup(
    name='csqi',
    version=help.get_version(),
    keywords='pyutils',
    description='Development tools for python',
    license='MIT License',
    url='https://github.com/qicongsheng/csqi',
    author='qicongsheng',
    author_email='qicongsheng@outlook.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[
        'loguru~=0.7.2'
    ]
)
