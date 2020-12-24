# Package meta-data.
import os

NAME = 'umm'
DESCRIPTION = 'A toolkit to manager the fastest mirror of various tools, such as pip, npm, composer and etc.'
URL = 'https://github.com/xiyusullos/umm'
EMAIL = 'i@aponder.top'
AUTHOR = 'aponder'
VERSION = '0.1.0'

# What packages are required for this module to be executed?
REQUIRES = [
    'click',
]


HOME = os.getenv('HOME')
VIRTUAL_ENV = os.getenv('VIRTUAL_ENV')
