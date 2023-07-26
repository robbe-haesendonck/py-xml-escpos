#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyxmlescpos',
    version='0.2.1',
    description='Print XML-defined Receipts on ESC/POS Receipt Printers',
    long_description=long_description,
    long_description_content_type='text/x-rst',  # Adjust the content type as needed

    # The project's main homepage.
    url='https://github.com/fvdsn/py-xml-escpos',
    download_url='https://github.com/fvdsn/py-xml-escpos/archive/0.2.1.tar.gz',  # Correct the download URL

    # Author details
    author='Frédéric van der Essen & Manuel F Martinez',
    author_email='fvdessen+x@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Printing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    # What does your project relate to?
    keywords='printing receipt xml escpos',

    # You can just specify the packages manually here if your project is simple.
    # Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # List run-time dependencies here.
    # These will be installed by pip when your project is installed.
    install_requires=['python-escpos==3.0a9', 'six'],

    # List additional groups of dependencies here (e.g. development dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    # extras_require = {
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

    # If there are data files included in your packages that need to be installed, specify them here.
    # If using Python 2.6 or less, then these have to be included in MANIFEST.in as well.
    # package_data={
    #   'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some cases, you may need to place data files outside of your packages.
    # See http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the "scripts" keyword.
    # Entry points provide cross-platform support and allow pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #    'console_scripts': [
    #        'sample=sample:main',
    #    ],
    # },
)