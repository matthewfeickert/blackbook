from setuptools import setup, find_packages
import unittest
import doctest
import os

requirements = ["black>=18.9b0"]

setup(
    name="blackbook",
    version="0.0.1",
    install_requires=requirements,
    author="Nikoleta Glynatsi, Vince Knight, Henry Wilde",
    author_email=("glynatsine@cardiff.ac.uk"),
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="",
    license="The MIT License (MIT)",
    description="`Black` for Jupyter notebooks.",
)
