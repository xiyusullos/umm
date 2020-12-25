import click
from click import echo

from src import C
from src.utils import Mirror


class MirrorCommand(click.Group):
    NAME = 'todo'
    DEFAULT = 'o' # official

    @staticmethod
    def format_mirror(name, url):
        return '%-15s %s' % (name, url)

    def prefix(self, mirror_name, current_mirror_name=None):
        '''format a prefix string to indicate the current using mirror

        :param mirror_name: string, the iterating mirror_name
        :param current_mirror_name: string, the current using mirror name
        :return string, '  ' or '* '
        '''
        current_mirror_name = current_mirror_name or self.current_mirror_name()
        return '* ' if mirror_name == current_mirror_name else '  '

    def current_mirror_name(self):
        # todo: need to override this if necessary
        return self.DEFAULT

    def cmd_ls(self):
        current_mirror_name = self.current_mirror_name()
        echo('  ' + self.format_mirror('[%s] name' % self.name, 'url'))
        echo('-' * 60)
        for k in self.mirror:
            echo(self.prefix(k, current_mirror_name) + self.mirror.format((k, self.mirror[k])))

    def cmd_use(self, mirror_name, is_local=False):
        # todo: must override this
        return echo('todo: use')

    def cmd_now(self):
        k = self.current_mirror_name() or ''
        return echo(self.mirror.format((k, self.mirror[k])))

    def __init__(self, name=None, commands=None, **attrs):
        name = name or self.NAME
        self.mirror = Mirror(C.MIRRORS.get(name, {}))

        super().__init__(name=name, commands=commands, **attrs)

        self.help = 'Manage %s mirrors.' % self.name

        @click.command('ls', short_help='List all available mirrors.')
        def ls():
            return self.cmd_ls()

        @click.command('use', short_help='Use the given mirror.')
        @click.option('-l', '--local', 'is_local', help='whether use the mirror in local', default=False, is_flag=True, show_default=True)
        @click.argument('mirror_name', type=click.STRING)
        def use(mirror_name, is_local=True):
            return self.cmd_use(mirror_name, is_local)

        @click.command('now', short_help='Show current using mirror.')
        def now():
            return self.cmd_now()

        self.add_command(ls)
        self.add_command(use)
        self.add_command(now)
