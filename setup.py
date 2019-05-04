#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

long_description = """\
Asciitext version of "A New Hope", available from Towel.blinkenlights.nl

Original Work   : Simon Jansen ( http://www.asciimation.co.nz/ )

Telnetification : Sten Spans ( http://blinkenlights.nl/ )

Terminal Tricks : Mike Edwards (pf-asciimation@mirkwood.net)

The hard work was done by Simon and Mike and Sten.
I just made a Python wrapper for the Telnet application.
"""

setup(
    packages=find_packages(),
    package_data={
        'george_lucas': ['data/*']
    },
    name='george_lucas',
    version='0.2.0',
    description='Plays "A New Hope" on import',
    long_description=long_description,
    author = "Dillon Niederhut",
    author_email = "dillon.niederhut@gmail.com",
    url = "https://github.com/deniederhut/george_lucas",
    license = "MIT"
)
