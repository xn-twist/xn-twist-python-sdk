#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('LICENSE') as license_file:
    license = license_file.read()

requirements = [
    'Requests'
]

test_requirements = [
    'Requests'
    'Pytest'
]

setup(
    name='xn-twist-python-sdk',
    version='5.0.0',
    description="Python SDK for XN-Twist's API",
    long_description=readme + '\n\n' + history,
    author="Floyd Hightower",
    author_email='',
    url='https://github.com/xn-twist/xn-twist-python-sdk',
    packages=find_packages(exclude=('tests', 'docs')),
    package_dir={'xn_twist_python_sdk':
                 'xn_twist_python_sdk'},
    include_package_data=True,
    install_requires=requirements,
    license=license,
    zip_safe=True,
    keywords='xn_twist_python_sdk',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
