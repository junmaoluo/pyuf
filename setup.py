#!/usr/bin/env python


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name = 'pyuf',
    version = '1.1',
    description = 'Python library for uFactory',
    author = 'Duke Fong',
    author_email = 'developer@ufactory.cc',
    url = "https://github.com/uarm-developer/pyuf",
    keywords = "pyuf swift uarm ufactory",
    packages = ['uf', 'uf.ufc', 'uf.utils', 'uf.comm', 'uf.swift', 'uf.wrapper'],
    install_requires = ['pyserial>=3.0'],
    long_description = open('README.md').read(),
    license = 'BSD'
)

