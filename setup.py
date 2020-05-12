
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pycerthole',
    version='0.1',
    description='Unofficial python 3 library to manage data from https://hole.cert.pl/',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/TheArqsz/pycerthole',
    author='Arqsz',
    author_email='arqsz@protonmail.com',
    keywords='security',
    install_requires=['requests==2.23.0', 'bs4==0.0.1'],
    license='MIT',
    packages=['pycerthole'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)