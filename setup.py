#!/usr/bin/env python

from setuptools import setup, find_packages

# with open('requirements.txt', encoding='utf-8') as f:
#     install_requires = f.read()

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

# with open('LICENSE', encoding='utf-8') as f:
#     license = f.read()

entry_points = {
    'console_scripts': [
        'tmd5 = md5.__main__:main'
    ]
}

setup(
    name='md5',
    version='1.0.0',
    description='Python implementation of MD5',
    long_description=readme,
    author='tama@ttk1.net',
    author_email='tama@ttk1.net',
    url='https://github.com/ttk1/md5',
    #license=license,
    #install_requires=install_requires,
    packages=find_packages(exclude=('test',)),
    entry_points=entry_points
)