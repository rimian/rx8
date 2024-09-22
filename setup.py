from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="rx8",
    version="0.1",
    packages=find_packages(),
    install_requires=required,
    author="Rimian Perkins",
    author_email="rimian.p@gmail.com",
    description="Console for screen",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rimian/rx8",
)
