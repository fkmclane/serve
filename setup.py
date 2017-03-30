#!/usr/bin/env python3
from distutils.core import setup

from serve import name, version


setup(
    name=name,
    version=version,
    description='a simple autoindexing file server',
    license='MIT',
    author='Foster McLane',
    author_email='fkmclane@gmail.com',
    packages=['serve'],
    package_data={'serve': ['html/*.*']},
)
