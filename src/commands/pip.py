import configparser
import os
from urllib.parse import urlparse

import click
from click import echo

from src import C
from src.utils import Mirror, is_windows

# https://pip.pypa.io/en/stable/user_guide/#config-file

MIRRORS = {
    "pypi": "https://pypi.python.org/simple/",
    "tuna": "https://pypi.tuna.tsinghua.edu.cn/simple",
    "douban": "http://pypi.douban.com/simple/",
    "aliyun": "https://mirrors.aliyun.com/pypi/simple/",
    "ustc": "https://mirrors.ustc.edu.cn/pypi/web/simple",
}

MIRROR = Mirror(MIRRORS)

CONFIG_FILE = 'pip.ini' if is_windows() else 'pip.conf'
CONFIG_FOLDER = 'pip' if is_windows() else '.pip'
CONFIG_PATH_GLOBAL = os.sep.join([C.HOME, CONFIG_FOLDER, CONFIG_FILE])
CONFIG_PATH_LOCAL = os.sep.join([C.VIRTUAL_ENV, CONFIG_FOLDER, CONFIG_FILE])


def ensure_section(config, section_name):
    if not config.has_section(section_name):
        config.add_section(section_name)


def load_config(is_local=False):
    '''Load the pip config file'''
    config = configparser.ConfigParser()
    if is_local:
        config.read(CONFIG_PATH_LOCAL)
    else:
        config.read(CONFIG_PATH_GLOBAL)

    return config


@click.group('pip')
def cli():
    '''Manage pip mirrors. '''
    pass


@cli.command('ls', short_help=MIRROR.echo_mirrors.__doc__)
def ls():
    MIRROR.echo_mirrors()


@cli.command('now')
def now():
    '''Show current mirror.'''
    default_mirror = ('pypi', MIRROR.get('pypi'))
    config = load_config()
    if config.has_section('global'):
        mirror_url = config.get('global', 'index-url')
        mirror = MIRROR.find_mirror(mirror_url)
        if mirror:
            return echo(MIRROR.format_mirror(mirror))

    echo(MIRROR.format_mirror(default_mirror))


@cli.command('use')
@click.argument('mirror_name', type=click.STRING)
def use(mirror_name):
    '''Use the given mirror.'''
    is_local = False

    mirror_url = MIRROR.get(mirror_name)
    if mirror_url is None:
        return echo('Invalid mirror name.')

    url_info = urlparse(mirror_url)
    host = url_info.netloc

    config = load_config(is_local=is_local)
    ensure_section(config, 'global')
    config.set('global', 'index-url', mirror_url)

    ensure_section(config, 'install')
    config.set('install', 'trusted-host', host)

    with open(CONFIG_PATH_LOCAL if is_local else CONFIG_PATH_GLOBAL, 'w') as f:
        config.write(f)


if __name__ == '__main__':
    cli()
