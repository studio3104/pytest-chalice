#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-chalice',
    version='0.0.1',
    author='Satoshi SUZUKI',
    author_email='studio3104.com@gmail.com',
    maintainer='Satoshi SUZUKI',
    maintainer_email='studio3104.com@gmail.com',
    license='MIT',
    url='https://github.com/studio3104/pytest-chalice',
    description='A set of py.test fixtures for AWS Chalice',
    long_description=read('README.rst'),
    py_modules=['pytest_chalice'],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=[
        'chalice>=1.8.0',
        'pytest>=3.5.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'chalice = pytest_chalice',
        ],
    },
)
