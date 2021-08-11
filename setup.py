from setuptools import setup

with open('requirements.txt') as handle:
    REQUIRES = handle.read().splitlines()

setup(
    install_requires=REQUIRES,
)
