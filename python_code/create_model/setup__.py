#!/usr/bin/env python
# coding=utf-8

from distutils.core import setup, Extension

module = Extension('pr', sources = ['py.c'])

setup(name = 'Pr test', version = '1.0', ext_modules = [module])