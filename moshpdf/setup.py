import setuptools
from pathlib import Path

setuptools.setup(
    name="moshpdf",
    version=110.0,
    long_description="",
    packages=setuptools.find_packages(exclude=["tests", "data"])
)
