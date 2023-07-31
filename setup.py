#!/usr/bin/env python

from distutils.core import setup

setup(name='midify',
    version='0.1.1',
    description='Command line tool for converting Audio to MIDI.',
    author='Daniel Santana',
    author_email='danielsantanarocha@gmail.com',
    url='https://github.com/DanielSanRocha/midify',
    scripts=['midify/midify'],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha'
    ]
)
