#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must: pip install twine

import os
import sys
from shutil import rmtree

from setuptools import setup, Command, find_packages

from src.umm import C

here = os.path.abspath(os.path.dirname(__file__))

# Import the 'readme.md' and use it as the long-description.
# Note: this will only work if 'readme.md' is present in your MANIFEST.in file!
with open("readme.md", "r", encoding="utf-8") as f:
    long_description = f.read()


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        self.status('Publishing git tags…')
        os.system('git tag v{0}'.format(C.VERSION))
        os.system('git push --tags')

        sys.exit()


# Where the magic happens:
setup(
    name=C.NAME,
    version=C.VERSION,
    description=C.DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=C.AUTHOR,
    author_email=C.EMAIL,
    url=C.URL,
    python_requires='>=3.6.0',
    # If your package is a single module, use this instead of 'packages':
    py_modules=['umm'],

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir={'': 'src'},

    packages=find_packages('src'),

    entry_points={
        'console_scripts': [
            'umm=umm.main:cli'
        ],
    },
    install_requires=C.REQUIRES,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
