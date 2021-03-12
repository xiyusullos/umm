from click import echo

from .base import MirrorCommand
from .. import C
from ..utils import run_cmd, set_locale


# https://goproxy.io/docs/getting-started.html
# https://goproxy.cn/

class Golang(MirrorCommand):
    """go 1.13+ is recommended"""

    NAME = 'golang'

    def current_mirror_name(self):
        is_ok, out = run_cmd('go env GOPROXY')
        out = out.replace(',direct', '')
        found_mirror = self.mirror.find_by_url(out)
        return found_mirror[0] if found_mirror else self.DEFAULT

    def cmd_use(self, mirror_name, is_local=False):
        if mirror_name not in self.mirror:
            return echo(C.INVALID_MIRROR_NAME)

        is_ok, out = run_cmd('go env -w GO111MODULE=on')
        cmd = f'go env -w GOPROXY={self.mirror[mirror_name]},direct'
        run_cmd(cmd)
        is_ok, out = run_cmd(cmd)


def test():
    cli = Golang()
    print(cli.current_mirror_name())


cli = Golang()

if __name__ == '__main__':
    set_locale()
    cli()
