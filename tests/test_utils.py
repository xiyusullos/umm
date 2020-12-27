import os
import re
import time
from importlib import reload

from src import C
from src.utils import Mirror, store_env_variable, is_windows, make_export_env

import pytest


def test_Mirror():
    mirror = Mirror(C.MIRRORS.get('pip'))
    assert mirror['o'] == 'https://pypi.python.org/simple/'

    mirror['o'] = 'abc'
    assert mirror['o'] == 'abc'


def test_store_env_variable():
    key = 'UMM_TEST_ENV'

    new_env = str(time.time())
    store_env_variable(key, new_env)
    if not is_windows():
        p = os.path.expanduser('~/.bashrc')
        with open(p, 'r') as f:
            s = f.read().rstrip('\n')
        s += '\n'
        prefix = make_export_env(key)
        pattern = prefix + r'(.*)\n'
        r = re.search(pattern, s)
        assert new_env == r.groups()[0]


if __name__ == '__main__':
    pass
