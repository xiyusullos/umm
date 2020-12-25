from click import echo

from src import C
from src.commands.base import MirrorCommand
from src.utils import run_cmd, set_locale


# https://docs.npmjs.com/cli/v6/commands/npm-config
# https://docs.npmjs.com/cli/v6/using-npm/config

# npm config set registry https://registry.npm.taobao.org
# npm config set registry https://registry.npm.taobao.org -g
# npm config set registry https://registry.npmjs.org -g

class Npm(MirrorCommand):
    NAME = 'npm'
    DEFAULT = 'npm'

    def current_mirror_name(self):
        out = run_cmd('npm config get registry'.split(' '))
        found_mirror = self.mirror.find_by_url(out)
        return found_mirror[0] if found_mirror else self.DEFAULT

    def cmd_use(self, mirror_name, is_local):
        if mirror_name not in self.mirror:
            return echo(C.INVALID_MIRROR_NAME)

        mirror_url = self.mirror[mirror_name]
        cmd_args = ['npm', 'config', 'set', 'registry', mirror_url]
        if not is_local:
            cmd_args.append('-g')
        out = run_cmd(cmd_args)


def test_npm():
    cli = Npm()
    print(cli.current_mirror_name())


cli = Npm()

if __name__ == '__main__':
    set_locale()
    cli()
