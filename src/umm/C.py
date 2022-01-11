import os
import platform

import yaml

# Package meta-data.
VERSION = '0.6.1'
NAME = 'umm'
DESCRIPTION = 'A toolkit to manager the fastest mirror of various tools, such as pip, npm, composer and etc.'
URL = 'https://github.com/xiyusullos/umm'
EMAIL = 'i@aponder.top'
AUTHOR = 'aponder'

# What packages are required for this module to be executed?
REQUIRES = [
    'click',
    'PyYAML',
]
# Package meta-data. #end#


HERE = os.path.dirname(__file__)

_HOME_str = 'HOMEPATH' if platform.system() == 'Windows' else 'HOME'
HOME = os.getenv(_HOME_str)
VIRTUAL_ENV = os.getenv('VIRTUAL_ENV', HOME)

MIRRORS = yaml.safe_load(open(os.sep.join([HERE, 'mirrors.yml'])))


# some constants
INVALID_MIRROR_NAME = 'Invalid mirror name'

if __name__ == '__main__':
    print(MIRRORS)
