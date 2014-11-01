#!/usr/bin/env python

from distutils.core import setup

setup(name='Craftbook',
      version='1.4.0',
      #description='',
      author='Ben Schwabe',
      author_email='bschwabe@suturesoft.com',
      url='http://www.suturesoft.com',
      scripts=['craftbook_stable.py'],
      data_files=[('icon.ico'),('data.xml'),('version.txt')]
     )
