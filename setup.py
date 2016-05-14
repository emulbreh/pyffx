from setuptools import setup, find_packages

import sys

with open('README.rst') as f:
    description = f.read()

setup(
    name='pyffx',
    url='http://github.com/emulbreh/pyffx/',
    version='0.1.0',
    packages=find_packages(),
    license=u'BSD License',
    author=u'Johannes Dollinger',
    description=u'pure Python format preserving encryption',
    long_description=description,
    install_requires=[
        'six',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)
