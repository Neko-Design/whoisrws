#!/usr/bin/env python
"""
whoisrws
==============

A Python Client for the ARIN WHOIS Webservice.

:license: APACHE2, see LICENSE for more details.
"""

from setuptools import setup, find_packages
import os

cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
readme_text = open(os.path.join(cwd, 'README.md')).read()

setup(
    name='whoisrws',
    version='0.1.0',
    author='Ewen McCahon',
    author_email='hi@ewenmccahon.me',
    url='https://github.com/Neko-Design/whoisrws',
    long_description=readme_text,
    long_description_content_type="text/markdown",
    license='apache2',
    description='A Python Client for the ARIN WHOIS Webservice.',
    packages=find_packages(),
    install_requires=[
        'requests',
        'murl',
        'IPy'
    ],
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)