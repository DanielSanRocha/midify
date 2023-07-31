#!/usr/bin/env python

from distutils.core import setup

setup(name='midify',
    version='0.3.0',
    packages=['midify'],
    description='Command line tool for converting Audio to MIDI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Daniel Santana',
    author_email='danielsantanarocha@gmail.com',
    url='https://github.com/DanielSanRocha/midify',
    scripts=['midify/midify'],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha'
    ],
    install_requires=['click>=8.0.0', 'pretty-midi>=0.2.10', 'scipy>=1.0.0', 'numpy>=1.24.0', 'librosa>=0.10.0']
)
