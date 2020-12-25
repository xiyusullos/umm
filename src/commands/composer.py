import re

from click import echo

from src import C
from src.commands.base import MirrorCommand
from src.utils import run_cmd, set_locale


# composer config -g repo.packagist composer https://packagist.phpcomposer.com
# composer config repo.packagist composer https://packagist.phpcomposer.com

class Composer(MirrorCommand):
    NAME = 'composer'

    def current_mirror_name(self):
        cmd_args = 'composer config -l'.split(' ')
        is_ok, out = run_cmd(cmd_args)
        if not is_ok:
            cmd_args.append('-g')
            is_ok, out = run_cmd(cmd_args)

        pattern = r'\[repositories\.packagist\.org\.url\] (.*)\n'
        url = re.search(pattern, out).groups()[0]
        url.replace('?', '')
        found_mirror = self.mirror.find_by_url(url)
        return found_mirror[0] if found_mirror else self.DEFAULT

    def cmd_use(self, mirror_name, is_local=False):
        if mirror_name not in self.mirror:
            return echo(C.INVALID_MIRROR_NAME)

        mirror_url = self.mirror[mirror_name]
        cmd_args = []
        if not is_local:
            cmd_args = ['composer', 'config', '-g', 'repo.packagist', 'composer', mirror_url]
        else:
            cmd_args = ['composer', 'config', 'repo.packagist', 'composer', mirror_url]

        out = run_cmd(cmd_args)


def test_npm():
    cli = Composer()
    print(cli.current_mirror_name())


cli = Composer()

if __name__ == '__main__':
    set_locale()
    # cli()

    print(cli.current_mirror_name())