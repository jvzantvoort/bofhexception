#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup file for bofhexception."""

import sys
from setuptools import setup


def setup_package():
    needs_sphinx = {'build_sphinx', 'upload_docs'}.intersection(sys.argv)
    sphinx = ['sphinx'] if needs_sphinx else []
    setup(setup_requires=[] + sphinx)

if __name__ == "__main__":
    setup_package()
