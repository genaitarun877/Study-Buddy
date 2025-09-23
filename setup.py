from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="study-buddy",
    version="0.1",
    author="Tarun",
    packages=find_packages(),
    install_requires = requirements,
)