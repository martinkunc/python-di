#!/usr/bin/env python3
from setuptools import (
    setup,
    find_packages,
)
from os.path import splitext, basename
from glob import glob

if __name__ == "__main__":
    setup(name="test-app",
        packages=find_packages("src"),
        package_dir={'': 'src'},
        py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
        )
