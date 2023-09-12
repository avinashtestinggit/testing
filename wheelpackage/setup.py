import setuptools
#from setuptools import setup, find_packages

setuptools.setup(
    name="mypackage",
    version="1.0.0",
    author="Avinash",
    author_email="avinash.shukla@capgemini.com",
    description='wheel test',
    packages=setuptools.find_packages(),
    classifiers=[
        "python:3",
    ],
    python_requires='>=3.7',
)