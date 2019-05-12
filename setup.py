from setuptools import setup, find_packages

import io
import sys

with io.open("README.rst", encoding="utf-8") as f:
    description = f.read()

setup(
    name="pyffx",
    url="http://github.com/emulbreh/pyffx/",
    version="0.3.0",
    packages=find_packages(),
    license=u"MIT License",
    author=u"Johannes Dollinger",
    description=u"pure Python format preserving encryption",
    long_description=description,
    install_requires=["six"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
)
