import platform
import subprocess

from click import echo

from src import C

SYSTEM = platform.system()
MACHINE = platform.machine()


def is_windows(): return 'Windows' == SYSTEM


def is_linux(): return 'Linux' == SYSTEM


def is_mac(): return 'Darwin' == SYSTEM


def is_64bit(): return 'x86_64' == MACHINE


class Mirror():
    def __init__(self, mirror=None):
        self.data = mirror or {}

    def format(self, mirror):
        if len(mirror) == 2:
            return '%-15s %s' % mirror

        return ''

    def echo_mirrors(self):
        '''List all available mirrors'''
        for k in self.data:
            echo(self.format((k, self.data[k])))

    def find_by_url(self, mirror_url):
        '''Find a mirror whose url equals to mirror_url.

        :return (mirror_name, mirror_url)
        '''
        mirror_url = mirror_url.strip()
        for k in self.data:
            if self.data[k] == mirror_url:
                return (k, mirror_url)
        return None

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, mirror_name):
        return mirror_name in self.data

    def __getitem__(self, mirror_name):
        return self.data.get(mirror_name, '')

    def __setitem__(self, mirror_name, mirror_url):
        self.data[mirror_name] = mirror_url

    def save(self, file_path):
        # todo: maybe not necessary
        pass


def test_Mirror():
    mirror = Mirror(C.MIRRORS.get('npm'))
    print(mirror['npm'])
    mirror['npm'] = 'abc'
    print(mirror['npm'], 'npm' in mirror, 'a' in mirror)
    print(mirror)


def run_cmd(args):
    p = subprocess.run(args=args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return (0 == p.returncode, p.stdout.decode('utf-8'))


def set_locale(local='en_US.UTF-8'):
    import os
    os.environ['LC_ALL'] = os.environ['LANG'] = local


if __name__ == '__main__':
    print(SYSTEM, MACHINE)

    test_Mirror()
