#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["requests>=2"]

setup(
    name="PyCrowdTangle",
    version="0.0.1",
    author="Jose R. Zapata",
    author_email="jjrzg@hotmail.com",
    description="A Python Wrapper To Retrieve Data From The CrowdTangle API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/UPB-SS1/PyCrowdTangle",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
    keywords=['crowdtangle', 'wrapper-api'],
)