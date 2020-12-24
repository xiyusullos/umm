import platform

from click import echo

SYSTEM = platform.system()
MACHINE = platform.machine()


def is_windows(): return 'Windows' == SYSTEM


def is_linux(): return 'Linux' == SYSTEM


def is_mac(): return 'Darwin' == SYSTEM


def is_64bit(): return 'x86_64' == MACHINE


class Mirror():
    def __init__(self, mirror=None):
        self.mirrors = mirror if mirror is not None else {}

    def format_mirror(self, mirror):
        if len(mirror) == 2:
            return '%-15s %s' % mirror

        return ''

    def exist(self, mirror_name):
        return mirror_name in self.mirrors

    def echo_mirrors(self):
        '''List all available mirrors'''
        for k in self.mirrors:
            echo(self.format_mirror((k, self.mirrors[k])))

    def find_mirror(self, mirror_url):
        '''Find a mirror whose url equals to mirror_url.'''

        for k in self.mirrors:
            if self.mirrors[k] == mirror_url:
                return (k, mirror_url)
        return None

    def get(self, mirror_name):
        return self.mirrors.get(mirror_name, None)

    def set(self, mirror_name, mirror_url):
        self.mirrors.setdefault(mirror_name, mirror_url)

    def save(self, file_path):
        # todo: maybe not necessary
        pass


if __name__ == '__main__':
    print(SYSTEM, MACHINE)
