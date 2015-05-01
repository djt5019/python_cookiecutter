#!/usr/bin/env python
import codecs
import sys

from setuptools import setup, find_packages

import {{cookiecutter.project_name}}


def read_requirements_file(filename):
    """Read pip-formatted requirements from a file."""
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()
                if not line.startswith('#')]

setup(
    name='{{cookiecutter.project_name}}',
    description='{{cookiecutter.short_description}}',
    version={{cookiecutter.project_name}}.__version__,
    packages=find_packages(exclude=['tests', 'tests.*']),
    test_suite='nose.collector',
    include_package_data=True,
    long_description=codecs.open('README.rst', encoding='utf-8').read(),
    install_requires=read_requirements_file('requirements.txt'),
    tests_require=read_requirements_file('test-requirements.txt'),
    author='Dan Tracy.',
    author_email='djt5019@gmail.com',
    url='https://github.com/djt5019/{{cookiecutter.project_name}}',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
