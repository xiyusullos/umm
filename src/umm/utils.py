import os
import pipes
import platform
import re
import subprocess

from click import echo

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


def run_cmd(cmd):
    p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    is_ok = 0 == p.returncode
    output = (p.stdout if is_ok else p.stderr).decode('utf-8').strip('\n')
    return (is_ok, output)


def set_locale(local='en_US.UTF-8'):
    import os
    os.environ['LC_ALL'] = os.environ['LANG'] = local


def make_export_env(key, value=None):
    s = 'export %s=' % key
    if value is not None:
        s += pipes.quote(str(value))
    return s


def store_env_variable(key, value):
    if is_windows():
        run_cmd('setx /M %s "%s"' % (key, value))
    else:
        p = os.path.expanduser('~/.bashrc')
        with open(p, 'r') as f:
            s = f.read().rstrip('\n')
        s += '\n'  # if the target is the last one, without a \n will fail to search
        prefix = make_export_env(key)
        new_env = make_export_env(key, value)
        pattern = prefix + r'(.*)\n'
        r = re.search(pattern, s)
        if r:  # env alreay exists
            old_env = prefix + r.groups()[0]
            cmd = 'sed -i -e "s/%s/%s/" %s' % (old_env, new_env, p)
            run_cmd(cmd)
        else:
            cmd = 'echo "%s" >> "%s"' % (new_env, p)
            run_cmd(cmd)


if __name__ == '__main__':
    print(SYSTEM, MACHINE)
